from db import db


class CowModel(db.Model):
    __tablename__ = "cows"

    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.String(20))
    private_id = db.Column(db.String(10))
    heredity = db.Column(db.String(10))
    vaccines = db.relationship('VaccineModel', lazy='dynamic') #this necessitates explicit queries to link 2 tables



    def __init__(self, private_id, pub_id, heredity):
        self.pub_id = pub_id
        self.private_id = private_id
        self.heredity = heredity

    def json(self):
        return {'pub_id': self.pub_id,
                'private_id': self.private_id,
                'heredity': self.heredity,
                'vaccines': [vaccine.json() for vaccine in self.vaccines.all()]
                # 'artificial_inseminations': [artificial_insemination.json() for artificial_insemination in
                #                              self.artificial_inseminations.all()]
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