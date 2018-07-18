from db import db


class ProblemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calf_id = db.Column(db.Integer, db.ForeignKey('calf.id'))
    calf = db.relationship('CalfModel')
    problem = db.Column(db.String(100))

    def __init__(self, pub_id):
        self.pub_id = pub_id

