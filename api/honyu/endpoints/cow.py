from flask_restplus import Api, Resource, fields
from flask_restplus import api, reqparse
from models.cowmodel import CowModel

api = Api()
ns = api.namespace('cow', description='Operations related to blog categories')

cow = api.model('Cow', {
    'pub_id': fields.String(readOnly=True, description='Government ID'),
    'private_id': fields.String(required=True, description='Bokojo ID'),
})


@ns.route('/')
class Cow(Resource):
    parser = reqparse.RequestParser()

    @api.marshal_list_with(cow)
    def get(self):
        return {'cows': [cow.json() for x in CowModel.query.all()]}

    @api.expect(cow)
    def post(self):
        data = Cow.parser.parse_args()
        x = CowModel(**data)
        x.save_to_db()
        return x.json(), 201
