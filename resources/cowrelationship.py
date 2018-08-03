from flask_restful import Resource
from models.cowrelationship import CowRelationship


class CowRelationshipList(Resource):
    def get(self):
        return {'cowrelationships': list(map(lambda x: x.json(), CowRelationship.query.all()))}