from db import db
from models.problems.testmodel import TestModel


class ModelInherit(TestModel):
    __tablename__ = "inheritmodel"
    id = db.Column(db.Integer, db.ForeignKey('tests.id'), primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'))

    __mapper_args__ = {'polymorphic_identity': 'mastitis'}

    def __init__(self, name, age, is_real, has_penis, date_diagnosed, date_cured, date_treated, cow_id):
        super().__init__(name, age, is_real, date_diagnosed, date_cured, date_treated)
        self.cow_id = cow_id
        self.has_penis = has_penis

    def json(self):
        return {'name': self.name,
                'age': self.age,
                'is_real': self.is_real,
                'has_penis': self.has_penis,
                'date_diagnosed': self.date_diagnosed,
                'date_cured': self.date_cured,
                'date_treated': self.date_treated,
                'cow_id': self.cow_id
                }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
