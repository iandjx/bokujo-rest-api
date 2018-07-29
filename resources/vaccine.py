from models.vaccine import VaccineModel
from flask_restful import Resource, reqparse
from models.cow import CowModel

class Vaccine(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('vaccine_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_given',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )

    def post(self, private_id):
        data = Vaccine.parser.parse_args()
        cow = CowModel.find_by_private_id(private_id)
        if cow is None:
            return {"message": "Cow doesn't exist"}
        vaccine = VaccineModel(**data, cow_id=cow.id)

        try:
            vaccine.save_to_db()
        except:
            return {"message": "An error occurred inserting the vaccine."}, 500

        return vaccine.json(), 201





