from db import db


class TestModel(db.Model):
    __tablename__ = "tests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    is_real = db.Column(db.Boolean)
    person_type = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity': 'test',
        'polymorphic_on': person_type}

    def __init__(self, name,age, is_real):
        self.name = name
        self.age = age
        self.is_real = is_real

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
