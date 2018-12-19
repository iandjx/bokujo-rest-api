from flask_restful import Resource, reqparse
from models.problems.mastitismodel import MastitisModel
from datetime import datetime


class Mastitis(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('problem_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_diagnosed',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_treated',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_cured',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('is_right_front_affected',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('is_left_front_affected',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('is_right_back_affected',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('is_left_back_affected',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('cow_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    def get(self, _id):
        mastitis = MastitisModel.find_by_id(_id)
        if mastitis:
            return mastitis.json()
        return {'message': 'Mastitis not found'}, 404

    def post(self, _id):
        if MastitisModel.find_by_id(_id):
            return {'message': 'Ailment already exists'}, 400

        data = Mastitis.parser.parse_args()

        mastitis = MastitisModel(problem_name=data['problem_name'],
                                 date_diagnosed=data['date_diagnosed'],
                                 date_cured=data['date_cured'],
                                 is_left_back_affected=data['is_left_back_affected'],
                                 is_right_back_affected=data['is_right_back_affected'],
                                 is_right_front_affected=data['is_right_front_affected'],
                                 is_left_front_affected=data['is_left_front_affected'],
                                 date_treated=data['date_treated'],
                                 cow_id=data['cow_id'],
                                 mastitis_id)
        try:
            mastitis.save_to_db()
        except Exception as e:

            return {e}, 500

        return mastitis.json(), 201


class MastitisList(Resource):
    def get(self):
        return {'mastitis': list(map(lambda x: x.json(), MastitisModel.query.all()))}



