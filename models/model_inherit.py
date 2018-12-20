from db import db
from models.testmodel import TestModel


class ModelInherit(TestModel):
    __tablename__ = "inheritmodel"
    id = db.Column(db.Integer, db.ForeignKey('tests.id'), primary_key=True)
    has_penis = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': 'male'}

    def __init__(self, name, age, is_real, has_penis):
        super().__init__(name, age, is_real)
        self.has_penis = has_penis

    def json(self):
        return {'name': self.name,
               'age': self.age,
               'is_real': self.is_real,
               'has_penis': self.has_penis}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()