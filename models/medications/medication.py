from db import db


class MedicationModel(db.Model):
    __tablename__ = "medications"

    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(20))
    date_started = db.Column(db.BigInteger)
    date_stopped = db.Column(db.BigInteger)
    # TODO: change DateTime to BigINT
    medication_type = db.Column(db.String(32), nullable=False)
    __mapper_args__ = {'polymorphic_on': medication_type,
                       'polymorphic_identity': 'medication'}

    def __init__(self, medicine_name, date_started, date_stopped):
        self.medicine_name = medicine_name
        self.date_started = date_started
        self.date_stopped = date_stopped

    def json(self):
        return {'medicine_name': self.medicine_name,
                'date_started': self.date_started,
                'date_stopped': self.date_stopped
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