from db import db
from models.problems.problems import Problems


class MastitisModel(db.Model):
    __tablename__ = "mastitis"

    is_right_front_affected = db.Column(db.Boolean)
    is_left_front_affected = db.Column(db.Boolean)
    is_right_back_affected = db.Column(db.Boolean)
    is_left_back_affected = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True)

    # id = db.Column(db.Integer, db.ForeignKey('problems.id'), nullable=False, primary_key=True)
    # __mapper_args__ = {'polymorphic_identity': 'mastitis'}

    mastitis_medications = db.relationship('MastitisMedicationModel', lazy='dynamic')

    def __init__(self, is_right_front_affected, is_left_front_affected, is_right_back_affected, is_left_back_affected):
        # super().__init__(cow_id, problem_name)
        #                  # date_diagnosed,
        #                  # date_treated,
        #                  # date_cured)
        self.is_right_back_affected = is_right_back_affected
        self.is_left_back_affected = is_left_back_affected
        self.is_left_front_affected = is_left_front_affected
        self.is_right_front_affected = is_right_front_affected

    def json(self):
        return{
               # 'date_diagnosed': self.date_diagnosed,
               # 'date_treated': self.date_treated,
               # 'date_cured': self.date_cured,
               'is_right_front_affected': self.is_right_front_affected,
               'is_left_front_affected': self.is_left_front_affected,
               'is_right_back_affected': self.is_right_back_affected,
               'is_left_back_affected': self.is_left_back_affected
               }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
