from models.medication import MedicationModel
from flask_restful import Resource, reqparse
from models.sickness import SicknessModel
from models.cow import CowModel

class Medication(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('medicine_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_given',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )

    def post(self, _id):
        data = Medication.parser.parse_args()
        sickness = SicknessModel.find_by_id(_id)
        if sickness is None:
            return {"message": "Ailment doesn't exist"}
        medication = MedicationModel(**data, sickness_id=_id)
        try:
            medication.save_to_db()
        except:
            return {"message": "An error occurred inserting the vaccine."}, 500

        return medication.json(), 201





