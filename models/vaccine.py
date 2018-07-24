from db import db
from datetime import datetime


class VaccineModel(db.Model):

    __tablename__ = "vaccines"
    id = db.Column(db.Integer, primary_key=True)
    vaccine_name = db.Column(db.String(20))
    date_given = db.Column(db.DateTime)

    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    #cow = db.relationship('CowModel', backref=db.backref('vaccines', lazy='dynamic'))
    # cow = db.relationship('CowModel', back_populates='vaccines')
    def __init__(self, vaccine_name, cow_id, date_given=None):
        self.vaccine_name = vaccine_name
        if date_given is None:
            date_given = datetime.now()
        self.date_given = date_given
        self.cow_id = cow_id

    def __repr__(self):
        return 'vaccine name : {}, date_given : {}, private_id[] '.format(self.vaccine_name, self.date_given, self.cow_id)

    def json(self):
        return {'vaccine_name': self.vaccine_name, 'date_given': self.date_given}


