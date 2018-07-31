from db import db
from models.cow import CowModel

class SicknessModel(db.Model):
    __tablename__ = "sickness"

    id = db.Column(db.Integer, primary_key=True)
    diagnosis = db.Column(db.String(20))
    date_diagnosed = db.Column(db.Integer)
    is_cured = db.Column(db.Boolean)
    cure_date = db.Column(db.Integer)

    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'))
    cow = db.relationship('CowModel')

    medications = db.relationship('MedicationModel', lazy='dynamic')

    def __init__(self, diagnosis, date_diagnosed, is_cured, cure_date, cow_id):
        self.diagnosis = diagnosis
        self.date_diagnosed = date_diagnosed
        self.is_cured = is_cured
        self.cure_date = cure_date
        self.cow_id = cow_id


    def json(self):
        return {'diagnosis': self.diagnosis,
                'date_diagnosed': self.date_diagnosed,
                'is_cured': self.is_cured,
                'cure_date': self.cure_date,
                'medications': [medication.json() for medication in self.medications.all()]
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_all(cls, private_id):
        return {'sickness': list(map(lambda x: x.json(), SicknessModel.
                                     query.
                                     join(CowModel).
                                     filter(CowModel.private_id == private_id).all()))}


