from db import db


class ProblemModel(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)
    date_diagnosed = db.Column(db.BigInteger)
    date_treated = db.Column(db.BigInteger)
    date_cured = db.Column(db.BigInteger)
    problem_type = db.Column(db.String(32), nullable=False)
    pub_id = db.Column(db.String, db.ForeignKey('cows.pub_id'))

    __mapper_args__ = {'polymorphic_on': problem_type,
                       'polymorphic_identity': 'problem'}

    def __init__(self, date_diagnosed, date_treated, date_cured, pub_id):
        self.date_diagnosed = date_diagnosed
        self.date_treated = date_treated
        self.date_cured = date_cured
        self.pub_id = pub_id

    def json(self):
        return {
                'date_diagnosed': self.date_diagnosed,
                'date_treated': self.date_treated,
                'date_cured': self.date_cured,
                'pub_id': self.pub_id
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
