from flask_restful import Resource, reqparse

from models.cow import CowModel
from models.problems.mastitismodel import MastitisModel
from datetime import datetime
import arrow


class Mastitis(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date_diagnosed',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True)
    parser.add_argument('date_cured',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True)
    parser.add_argument('date_treated',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True)
    # parser.add_argument('pub_id',
    #                     type=str,
    #                     required=True)
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

    def get(self, pub_id):
        mastitis = MastitisModel.find_mastitis_on_pub_id(pub_id)
        # TODO: change to find if there is existing ailment
        if mastitis:
            return mastitis.json()
        return {'message': 'Mastitis not found'}, 404

    def post(self, pub_id):
        # TODO: post attribute should be pub_id
        # TODO: change to find if there is existing ailment
        data = Mastitis.parser.parse_args()
        if MastitisModel.find_existing_mastitis(pub_id):
            return {'message': 'Existing mastitis is not cured yet'}, 400
        mastitis = MastitisModel(
            date_diagnosed=arrow.get(data['date_diagnosed']).timestamp,
            date_cured=arrow.get(data['date_cured']).timestamp,
            date_treated=arrow.get(data['date_treated']).timestamp,
            is_left_back_affected=data['is_left_back_affected'],
            is_right_back_affected=data['is_right_back_affected'],
            is_right_front_affected=data['is_right_front_affected'],
            is_left_front_affected=data['is_left_front_affected'],
            pub_id=pub_id
        )
        try:
            mastitis.save_to_db()
        except Exception as e:

            return {e}, 500

        return mastitis.json(), 201


class MastitisList(Resource):
    def get(self):
        return {'mastitis': list(map(lambda x: x.json(), MastitisModel.query.all()))}
