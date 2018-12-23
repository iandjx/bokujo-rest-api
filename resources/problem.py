from models.testmodel import TestModel
from flask_restful import Resource, reqparse
from models.problems.problemmodel import ProblemModel
from datetime import datetime
from arrow import arrow

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
            date_diagnosed=data['date_diagnosed'],
            date_treated=data['date_treated'],
            date_cured=data['date_cured'],
            cow_id=data['cow_id']
        )
        print(data['date_diagnosed'].timestamp())
        print(datetime.fromtimestamp(data['date_diagnosed'].timestamp()).strftime('%c'))
        try:
            problem.save_to_db()
        except Exception as e:

            return {e}, 500

        return problem.json(), 201

