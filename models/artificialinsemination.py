from db import db
from datetime import datetime


class ArtificialInseminationModel(db.Model):
    __tablename__ = "artificialinseminations"

    id = db.Column(db.Integer, primary_key=True)
    semen = db.Column(db.String(20))
    date_given = db.Column(db.Integer)

    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    #cow = db.relationship('CowModel', backref=db.backref('vaccines', lazy='dynamic'))
    # cow = db.relationship('CowModel', back_populates='vaccines')

    def __init__(self, semen, cow_id, date_given):
        self.semen = semen
        self.date_given = date_given
        self.cow_id = cow_id

    def json(self):
        return {'semen': self.semen, 'date_given': self.date_given, 'cow_id': self.cow_id}


