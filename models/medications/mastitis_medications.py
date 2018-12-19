from db import db
from models.medications.medication import MedicationModel


class MastitisMedicationModel(MedicationModel):
    __tablename__ = "mastitis_medications"

    mastitis_id = db.Column(db.Integer, db.ForeignKey('mastitis.id'))

    id = db.Column(db.Integer, db.ForeignKey('medications.id'), primary_key=True)
    __mapper_args = {'polymorphic_identity': 'mastitis_medication'}

    def __init__(self, medicine_name, date_started, date_stopped, mastitis_id ):
        super().__init__(medicine_name, date_started, date_stopped)
        self.mastitis_id = mastitis_id

    def json(self):
        return {'medicine_name': self.medicine_name,
                'date_started': self.date_started,
                'date_stopped': self.date_stopped,
                'mastitis_id': self.mastitis_id}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()