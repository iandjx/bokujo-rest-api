from db import db


class CalfModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.String(20))
    private_id = db.Column(db.String(10))

    medical_history = db.relationship('ProblemModel', lazy='dynamic')

    def __init__(self, pub_id):
        self.pub_id = pub_id

