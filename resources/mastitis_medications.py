from models.medications.mastitis_medications import MastitisMedicationModel
from flask_restful import Resource, reqparse
from models.problems.mastitismodel import MastitisModel


class MastitisMedication(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('medicine_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_started',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_stopped',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('mastitis_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    def get(self, _id):
        mastitis_medication = MastitisMedicationModel.find_by_id(_id)
        if mastitis_medication:
            return mastitis_medication.json()
        return {'message': 'Mastitis medication not found'}, 404

    def post(self, _id):
        data = MastitisMedication.parser.parse_args()
        mastitis = MastitisModel.find_by_id(_id)
        if mastitis is None:
            return {"message": "Ailment doesn't exist"}
        mastitis_medication = MastitisMedicationModel(**data, mastitis_id=_id)
        try:
            mastitis_medication.save_to_db()
        except:
            return {"message": "An error occurred inserting the mastitis medication."}, 500

        return mastitis_medication.json(), 201


class MastitisMedicationList(Resource):
    def get(self):
        return {'mastitis_medications': list(map(lambda x: x.json(), MastitisMedication.query.all()))}



