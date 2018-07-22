from db import db
from models.enums import heredityenum

class CowModel(db.Model):

    __tablename__ = "cow"
    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.String(20))
    private_id = db.Column(db.String(10))
    heredity = db.Column(db.String(10))

    def __init__(self, pub_id, private_id, heredity):
        self.pub_id = pub_id
        self.private_id = private_id
        self.heredity = heredity

    def __repr__(self):
        return 'public id : {}, private id : {}'.format(self.pub_id, self.private_id)

    def json(self):
        return {'pub_id': self.pub_id, 'private_id': self.private_id}

    @classmethod
    def find_by_private_id(cls, private_id):
        return cls.query.filter_by(id=private_id).first()
