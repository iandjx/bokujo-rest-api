from models.testmodel import TestModel
from flask_restful  import Resource, reqparse


class Test(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('is_real',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank."
                        )

    def get(self, name):
        test = TestModel.find_by_name(name)
        if test:
            return test.json()
        return {'message': 'Cow not found'}, 404

    def post(self, name):
        data = Test.parser.parse_args()
        print(data['age'])
        test = TestModel(name=name,
                         age=data['age'],
                         is_real=data['is_real'])

        try:
            test.save_to_db()
        except:
            return {"message": "An error occurred inserting the cow."}, 500

        return test.json(), 201

