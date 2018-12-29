from models.cow import CowModel
from flask_restful import Resource, reqparse


class Cow(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('private_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('mother_id',
                        type=str,
                        required=True)
    parser.add_argument('current_pen',
                        type=str,
                        help="")

    def get(self, pub_id):
        cow = CowModel.find_by_pub_id(pub_id)
        # TODO: change to find_by_pub_id
        if cow:
            return cow.json()
        return {'message': 'Cow not found'}, 404

    def post(self, pub_id):
        if CowModel.find_by_pub_id(pub_id):
            # TODO: change to find_by_pub_id
            return {'message': "Pub ID  '{}' is already being used.".format(pub_id)}, 400
        data = Cow.parser.parse_args()

        cow = CowModel(private_id=data['private_id'],
                       pub_id=pub_id,
                       current_pen=data['current_pen'],
                       mother_id=data['mother_id']
                       )
        print(cow.json())
        try:
            cow.save_to_db()
        except:
            return {"message": "An error occurred inserting the cow."}, 500
        return cow.json(), 201


class CowList(Resource):
    def get(self):
        return {'cows': list(map(lambda x: x.json(), CowModel.query.all()))}





