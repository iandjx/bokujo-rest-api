from db import db


class CowModel(db.Model):
    __tablename__ = "cows"

    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.String(20))
    private_id = db.Column(db.String(10))
    heredity = db.Column(db.String(10))
    type_of_delivery = db.Column(db.String)
    current_pen = db.Column(db.String)

    cow_relationship_id = db.Column(db.Integer, db.ForeignKey('cowrelationships.id'))
    cow_relationship = db.relationship('CowRelationship')

    vaccines = db.relationship('VaccineModel', lazy='dynamic')
    sickness = db.relationship('SicknessModel', lazy='dynamic')

    def __init__(self, private_id, pub_id, heredity, cow_relationship_id, type_of_delivery, current_pen):
        self.pub_id = pub_id
        self.private_id = private_id
        self.heredity = heredity
        self.cow_relationship_id = cow_relationship_id
        self.type_of_delivery = type_of_delivery
        self.current_pen = current_pen

    def json(self):
        return {'pub_id': self.pub_id,
                'private_id': self.private_id,
                'heredity': self.heredity,
                'vaccines': [vaccine.json() for vaccine in self.vaccines.all()],
                'sickness': [sickness.json() for sickness in self.sickness.all()],
                'cow_relationship_id': self.cow_relationship_id,
                'type_of_delivery': self.type_of_delivery,
                'current_pen': self.current_pen
                }

    @classmethod
    def find_by_private_id(cls, private_id):
        return cls.query.filter_by(private_id=private_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


# SELECT cows.id AS cows_id, cows.pub_id AS cows_pub_id,
#        cows.private_id AS cows_private_id, cows.heredity AS cows_heredity,
#        cows.cow_relationship_id AS cows_cow_relationship_id
#        FROM cows
#        WHERE cows.private_id = G124
#        LIMIT 1 OFFSET 0
