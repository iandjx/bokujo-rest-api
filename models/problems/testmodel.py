from db import db


class TestModel(db.Model):
    __tablename__ = "tests"

    id = db.Column(db.Integer, primary_key=True)
    date_diagnosed = db.Column(db.BigInteger)
    date_cured = db.Column(db.BigInteger)
    date_treated = db.Column(db.BigInteger)
    problem_type = db.Column(db.String(30))
    __mapper_args__ = {
        'polymorphic_identity': 'test',
        'polymorphic_on': problem_type}

    def __init__(self, name,age, is_real, date_diagnosed, date_cured, date_treated):
        self.name = name
        self.age = age
        self.is_real = is_real
        self.date_diagnosed = date_diagnosed
        self.date_cured = date_cured
        self.date_treated = date_treated

    def json(self):
        return{'name': self.name,
               'age': self.age,
               'is_real': self.is_real}

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
