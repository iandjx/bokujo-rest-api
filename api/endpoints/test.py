from flask_restplus import Resource
from api.restplus import api
from flask import request
from api.core.serializers import test
from models.test import TestModel

ns = api.namespace('test', description='test')

@ns.route('/<string:name>')
class Test(Resource):
    @ns.doc('list Tests')
    @ns.marshal_with(test)
    def get(self, name):
        if TestModel.query.filter_by(name=name).first():
            return TestModel.query.filter_by(name=name).first()
        return {'message not exist'}

    @ns.doc('create Test')
    @ns.expect(test)
    @ns.marshal_with(test, code=201)
    def post(self, name):
        new_test = TestModel(name)
        new_test.save_to_db()
        return new_test
