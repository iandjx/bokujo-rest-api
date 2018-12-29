from flask_restful import Resource, reqparse
from models.problems.problem import ProblemModel
from datetime import datetime
import arrow


class Problem(Resource):

    parser = reqparse.RequestParser()
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
    parser.add_argument('cow_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    def get(self, _id):
        problem = ProblemModel.find_by_id(_id)
        if problem:
            return problem.json()
        return {'message': 'Cow not found'}, 404

    def post(self, _id):
        data = Problem.parser.parse_args()
        problem = ProblemModel(
            date_diagnosed=arrow.get(data['date_diagnosed']).timestamp,
            date_treated=arrow.get(data['date_treated']).timestamp,
            date_cured=arrow.get(data['date_cured']).timestamp,
            cow_id=data['cow_id']
            )
        try:
            problem.save_to_db()
        except Exception as e:

            return {e}, 500

        return problem.json(), 201

