from db import db
from models.cow import CowModel
from models.sickness import SicknessModel


class MedicationModel(db.Model):
    __tablename__ = "medications"

    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(20))
    date_given = db.Column(db.Integer)

    sickness_id = db.Column(db.Integer, db.ForeignKey('sickness.id'))
    sickness = db.relationship('SicknessModel')

    def __init__(self, medicine_name, sickness_id, date_given):
        self.medicine_name = medicine_name
        self.date_given = date_given
        self.sickness_id = sickness_id

    def json(self):
        return {'medicine_name': self.medicine_name,
                'date_given': self.date_given
                }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

