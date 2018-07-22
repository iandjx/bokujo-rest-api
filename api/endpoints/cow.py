from flask_restplus import Resource
from api.restplus import api
from api.core.serializers import cow
from flask import request
from api.core.business import create_cow, find_cow
from api.core.parsers import heredity_arguments

ns = api.namespace('cows', description='Cow Operations')


@ns.route('/')
class Cow(Resource):
    '''Shows all cows in he farm'''
    @ns.doc('list_cows')
    @api.expect(heredity_arguments)
    @ns.marshal_list_with(cow)
    def get(self):
        '''List all cows'''
        args = heredity_arguments.parse_args(request)
        return find_cow(args)

    @ns.doc('create_cow')
    @ns.expect(cow)
    @ns.marshal_with(cow, code=201)
    def post(self):
        '''Create a new cow'''
        create_cow(request.json)

        return request.json, 201


