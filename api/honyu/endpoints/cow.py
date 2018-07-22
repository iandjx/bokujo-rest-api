from flask_restplus import Api, Resource, fields
from flask_restplus import api, reqparse
from models.cowmodel import CowModel
from api.restplus import api

ns = api.namespace('cows', description='TODO operations')

cow = api.model('Cow', {
    'pub_id': fields.String(readOnly=True, description='Government ID'),
    'private_id': fields.String(required=True, description='Bokujo ID'),
})

@ns.route('/')
class Cow(Resource):
    '''Shows all cows in he farm'''
    @ns.doc('list_cows')
    @ns.marshal_list_with(cow)
    def get(self):
        '''List all tasks'''
        cows = CowModel.query.all()
        return cows

    @ns.doc('create_cow')
    @ns.expect(cow)
    @ns.marshal_with(cow, code=201)
    def post(self):
        '''Create a new task'''
        data = api.payload
        cow = CowModel(data['pub_id'], data['private_id'])
        try:
            cow.save_to_db()
        except:
            return {"message": "An error occurred inserting the cow."}, 500

        return cow.json(), 201