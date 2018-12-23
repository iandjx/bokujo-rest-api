from models.model_inherit import ModelInherit
from flask_restful import Resource, reqparse


class Inherit(Resource):
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
    parser.add_argument('has_penis',
                        type=bool,
                        required=True
                        )

    def get(self,name):
        inherit = ModelInherit.find_by_name(name)
        if inherit:
            return inherit.json()
        return {'message': 'Cow not found'}, 404

    def post(self,name):
        data = Inherit.parser.parse_args()
        inherit = ModelInherit(name=name,
                               age=data['age'],
                               is_real=data['is_real'],
                               has_penis=data['has_penis'])

        try:
                inherit.save_to_db()
        except Exception as e:
                return {e}, 500