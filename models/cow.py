from db import db


class CowModel(db.Model):

    __tablename__ = "cow"
    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.String(20))
    private_id = db.Column(db.String(10))
    heredity = db.Column(db.String(10))

    # vaccines_given = db.relationship('VaccineModel', lazy='dynamic') this necessitates explicit queries to link 2 tables
    # vaccines = db.relationship('VaccineModel', back_populates='cow') similar to backref but requires backpopulates also in vaccinemodel
    vaccines = db.relationship('VaccineModel', backref='cow')
    artificial_inseminations = db.relationship('ArtificialInseminationModel', backref='cow')

    def __init__(self, pub_id, private_id, heredity):
        self.pub_id = pub_id
        self.private_id = private_id
        self.heredity = heredity

    def __repr__(self):
        return 'public id : {}, private id : {}'.format(self.pub_id, self.private_id)

    def json(self):
        return {'pub_id': self.pub_id, 'private_id': self.private_id, 'vaccines_given': self.vaccines_given}

    @classmethod
    def find_by_private_id(cls, private_id):
        return cls.query.filter_by(private_id=private_id).first()