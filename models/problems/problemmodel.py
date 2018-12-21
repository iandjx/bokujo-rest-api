from db import db


class ProblemModel(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)
    date_diagnosed = db.Column(db.DateTime(timezone=True))
    date_treated = db.Column(db.DateTime(timezone=True))
    date_cured = db.Column(db.DateTime(timezone=True))
    problem_type = db.Column(db.String(32), nullable=False)
    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'))

    __mapper_args__ = {'polymorphic_on': problem_type,
                       'polymorphic_identity': 'problem'}

    def __init__(self,
                 date_diagnosed,
                 date_treated,
                 date_cured,
                 cow_id):
        self.date_diagnosed = date_diagnosed
        self.date_treated = date_treated
        self.date_cured = date_cured
        self.cow_id = cow_id

    def json(self):
        return {
                'date_diagnosed': self.date_diagnosed,
                'date_treated': self.date_treated,
                'date_cured': self.date_cured,
                'cow_id': self.cow_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
