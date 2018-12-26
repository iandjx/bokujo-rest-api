from models.problems.model_inherit import ModelInherit
from flask_restful import Resource, reqparse
from datetime import datetime
import arrow

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
    parser.add_argument('date_diagnosed',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True)
    parser.add_argument('date_cured',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True)
    parser.add_argument('date_treated',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True)
    # parser.add_argument('cow_id',
    #                     type=int,
    #                     required=True)

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
                               has_penis=data['has_penis'],
                               date_diagnosed=arrow.get(data['date_diagnosed']).timestamp,
                               date_cured=arrow.get(data['date_cured']).timestamp,
                               date_treated=arrow.get(data['date_treated']).timestamp
                               # cow_id=data['cow_id']
                               )

        try:
                inherit.save_to_db()
        except Exception as e:
                return {e}, 500
        return  inherit.json(), 201