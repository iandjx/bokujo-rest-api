from db import db


class CowModel(db.Model):
    __tablename__ = "cows"

    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.String(20), unique=True)
    private_id = db.Column(db.String(10))
    current_pen = db.Column(db.String)
    mother_id = db.Column(db.Integer)
    problems = db.relationship('ProblemModel', lazy='dynamic')
    # inherits = db.relationship('ModelInherit', lazy='dynamic')

    def __init__(self, private_id, pub_id, current_pen, mother_id):
        self.pub_id = pub_id
        self.private_id = private_id
        self.mother_id = mother_id
        self.current_pen = current_pen

    def json(self):
        return {'pub_id': self.pub_id,
                'private_id': self.private_id,
                'current_pen': self.current_pen,
                'mother_id': self.mother_id
                }

    @classmethod
    def find_by_pub_id(cls, pub_id):
        return cls.query.filter_by(pub_id=pub_id).first()
        # TODO: change find_by_private_id to find_by_pub_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


