from models.medications.mastitis_medications import MastitisMedicationModel
from flask_restful import Resource, reqparse
from models.problems.mastitismodel import MastitisModel
from datetime import datetime
import arrow


class MastitisMedication(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('medicine_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_started',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('date_stopped',
                        type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                        required=True,
                        help="This field cannot be left blank."
                        )

    # TODO: Change int to DateTime

    def get(self, mastitis_id):
        mastitis = MastitisModel.find_by_id(mastitis_id)
        # TODO: change to find if ailment is treated or not
        if mastitis is None:
            return {"message": "Ailment doesn't exist"}
        print(mastitis.json())
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        data = parser.parse_args()
        _id = data['id']
        mastitis_medication = MastitisMedicationModel.find_by_id(_id)
        if mastitis_medication:
            return mastitis_medication.json()
        return {'message': 'Mastitis medication not found'}, 404

    def post(self, mastitis_id):
        data = MastitisMedication.parser.parse_args()
        mastitis = MastitisModel.find_by_id(mastitis_id)
        # TODO: change to find if ailment is treated or not
        if mastitis is None:
            return {"message": "Ailment doesn't exist"}
        print(mastitis.json())
        mastitis_medication = MastitisMedicationModel(
            medicine_name=data['medicine_name'],
            date_started=arrow.get(data['date_started']).timestamp,
            date_stopped=arrow.get(data['date_stopped']).timestamp,
            mastitis_id=mastitis_id)

        print(mastitis_medication.json())
        try:
            mastitis_medication.save_to_db()
        except Exception as e:

            return {e}, 500

        return mastitis_medication.json(), 201

    def put(self, mastitis_id):
        data = MastitisMedication.parser.parse_args()

        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        data_id = parser.parse_args()
        _id = data_id['id']
        mastitis_medication = MastitisMedicationModel.find_by_id(_id)

        if mastitis_medication:
            mastitis_medication.medicine_name=data['medicine_name'],
            mastitis_medication.date_started=arrow.get(data['date_started']).timestamp,
            mastitis_medication.date_stopped=arrow.get(data['date_stopped']).timestamp,
            mastitis_medication.mastitis_id=mastitis_id
        else:
            mastitis_medication = MastitisMedicationModel(
                medicine_name=data['medicine_name'],
                date_started=arrow.get(data['date_started']).timestamp,
                date_stopped=arrow.get(data['date_stopped']).timestamp,
                mastitis_id=mastitis_id)

        mastitis_medication.save_to_db()

        return mastitis_medication.json()
class MastitisMedicationList(Resource):
    def get(self):
        return {'mastitis_medications': list(map(lambda x: x.json(), MastitisMedication.query.all()))}
