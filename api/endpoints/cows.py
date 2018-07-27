from flask_restplus import Resource
from api.restplus import api
from api.core.serializers import cow, cow_with_vaccine, basic_cow
from flask import request
from api.core.business import create_cow, find_cow
from api.core.parsers import heredity_arguments
from models.cow import CowModel
from flask_jwt_extended import jwt_required

ns = api.namespace('cows', description='Cow Operations')


@ns.route('/')
class Cows(Resource):
    '''Shows all cows in he farm'''
    @ns.doc('list_cows')
    @api.expect(heredity_arguments)
    @ns.marshal_with(cow_with_vaccine)
    @jwt_required
    def get(self):
        '''List all cows'''
        args = heredity_arguments.parse_args()
        print(args)
        return find_cow(args)

    @ns.doc('create_cow')
    @ns.expect(basic_cow)
    @ns.marshal_with(cow, code=201)
    def post(self):
        '''Create a new cow'''
        create_cow(request.json)

        return request.json, 201


@ns.route('/<string:private_id>')
class Cow(Resource):
    @ns.doc('individual_cow_data')
    @ns.expect()
    @ns.marshal_with(cow)
    def get(self, private_id):
        return CowModel.find_by_private_id(private_id)

    # @ns.doc('create_cow')




