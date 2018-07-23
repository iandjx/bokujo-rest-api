from flask_restplus import Resource
from api.restplus import api
from api.core.serializers import vaccine
from flask import request
from api.core.business import find_vaccine,give_vaccine

ns = api.namespace('vaccines', description='Cow Operations')


@ns.route('/')
class Vaccine(Resource):
    '''Shows all vaccinen'''
    @ns.doc('list_vaccine')
    @ns.marshal_list_with(vaccine)
    def get(self):
        '''List all vaccines given'''
        return find_vaccine()

    @ns.doc('give_vaccine')
    @ns.expect(vaccine)
    @ns.marshal_with(vaccine, code=201)
    def post(self):
        '''Create a new cow'''
        give_vaccine(request.json)

        return request.json, 201


