from models.sickness import SicknessModel
from flask_restful import Resource, reqparse, inputs
from models.cow import CowModel


class Sickness(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('diagnosis',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_diagnosed',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('is_cured',
                        type=inputs.boolean,
                        required=False,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('cure_date',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )

    def post(self, private_id):
        data = Sickness.parser.parse_args()
        cow = CowModel.find_by_private_id(private_id)
        sickness = SicknessModel(**data, cow_id=cow.id)

        try:
            sickness.save_to_db()
        except:
            return {"message": "An error occurred inserting the sickness."}, 500

        return sickness.json(), 201





