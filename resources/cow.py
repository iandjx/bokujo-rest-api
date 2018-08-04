from models.cow import CowModel
from flask_restful import Resource, reqparse
from models.cowrelationship import CowRelationship

class Cow(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pub_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('heredity',
                        type=str,
                        required=True,
                        help="Choose either holstein, wagyu or f1",
                        choices=('holstein', 'wagyu', 'f1')
                        )
    parser.add_argument('mother_private_id',
                        type=str,
                        required=True)
    parser.add_argument('type_of_delivery',
                        type=str,
                        help="")
    parser.add_argument('current_pen',
                        type=str,
                        help="")


    def get(self, private_id):
        cow = CowModel.find_by_private_id(private_id)
        if cow:
            return cow.json()
        return {'message': 'Cow not found'}, 404

    def post(self, private_id):
        if CowModel.find_by_private_id(private_id):
            return {'message': "Private ID  '{}' is already being used.".format(private_id)}, 400

        data = Cow.parser.parse_args()
        cowrelationship = CowRelationship(private_id, data['mother_private_id'])
        cowrelationship.save_to_db()

        cow = CowModel(private_id=private_id,
                       cow_relationship_id=cowrelationship.id,
                       heredity=data['heredity'],
                       pub_id=data['pub_id'],
                       type_of_delivery=data['type_of_delivery'],
                       current_pen=data['current_pen']
                       )
        try:
            cow.save_to_db()
        except:

            return {"message": "An error occurred inserting the cow."}, 500
        return cow.json(), 201


class CowList(Resource):
    def get(self):
        return {'cows': list(map(lambda x: x.json(), CowModel.query.all()))}

    # @ns.doc('create_cow')




