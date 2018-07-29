from flask_restplus import Resource, reqparse
from models.user import UserModel
from api.restplus import api
from api.core.serializers import user
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import safe_str_cmp

ns = api.namespace('user', description='User')

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )


@ns.route('/register')
class UserRegister(Resource):

    @ns.expect(user)
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


@ns.route('/<int:user_id>')
class User(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the users.
    """
    def get(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200

    def delete(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200

@ns.route('/login')
class UserLogin(Resource):

    @ns.expect(user)
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        # this is what the `authenticate()` function did in security.py
        if user and safe_str_cmp(user.password, data['password']):
            # identity= is what the identity() function did in security.py—now stored in the JWT
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {"message": "Invalid Credentials!"}, 401