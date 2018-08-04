from db import db

class CowRelationship(db.Model):
    __tablename__= "cowrelationships"

    id = db.Column(db.Integer, primary_key=True)
    mother_private_id = db.Column(db.String)
    child_private_id = db.Column(db.String)

    relationships = db.relationship('CowModel', lazy='dynamic')

    def __init__(self, child_private_id, mother_private_id):
        self.child_private_id = child_private_id
        self.mother_private_id = mother_private_id

    def json(self):
        return {'child_private_id': self.child_private_id,
                'mother_private_id': self.mother_private_id
                }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

