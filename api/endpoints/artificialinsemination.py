from flask_restplus import Resource
from api.restplus import api
from api.core.serializers import artificial_insemination
from flask import request
from api.core.business import find_artificial_insemination, inseminate_cow

ns = api.namespace('artifical_insemination', description='Artificial Insemination')


@ns.route('/')
class ArtificialInsemination(Resource):
    '''Shows all vaccines'''
    @ns.doc('list_AIs')
    @ns.marshal_with(artificial_insemination)
    def get(self):
        '''List all vaccines given'''
        return find_artificial_insemination()

    @ns.doc('give_vaccine')
    @ns.expect(artificial_insemination)
    @ns.marshal_with(artificial_insemination, code=201)
    def post(self):
        '''Inseminate cow'''
        inseminate_cow(request.json)

        return request.json, 201


