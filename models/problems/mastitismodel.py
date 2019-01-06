from db import db
from models.problems.problem import ProblemModel
from sqlalchemy import and_

class MastitisModel(ProblemModel):
    __tablename__ = "mastitis"

    is_right_front_affected = db.Column(db.Boolean)
    is_left_front_affected = db.Column(db.Boolean)
    is_right_back_affected = db.Column(db.Boolean)
    is_left_back_affected = db.Column(db.Boolean)

    id = db.Column(db.Integer, db.ForeignKey('problems.id'), nullable=False, primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'mastitis'}

    mastitis_medications = db.relationship('MastitisMedicationModel', lazy='dynamic')

    def __init__(self, is_right_front_affected, is_left_front_affected, is_right_back_affected, is_left_back_affected,
                 pub_id, date_diagnosed, date_treated, date_cured):
        super().__init__(date_diagnosed, date_treated, date_cured, pub_id)
        self.is_right_back_affected = is_right_back_affected
        self.is_left_back_affected = is_left_back_affected
        self.is_left_front_affected = is_left_front_affected
        self.is_right_front_affected = is_right_front_affected

    def json(self):
        return {
            'date_diagnosed': self.date_diagnosed,
            'date_treated': self.date_treated,
            'date_cured': self.date_cured,
            'is_right_front_affected': self.is_right_front_affected,
            'is_left_front_affected': self.is_left_front_affected,
            'is_right_back_affected': self.is_right_back_affected,
            'is_left_back_affected': self.is_left_back_affected,
            'pub_id': self.pub_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_existing_mastitis(cls, pub_id):
        return cls.query.filter(and_(cls.date_cured.is_(None), pub_id == pub_id)).first()
        # TODO: change find_by_id to find for if an existing ailment exists

    @classmethod
    def find_mastitis_on_pub_id(cls, pub_id):
        return cls.query.filter_by(pub_id=pub_id).first()
