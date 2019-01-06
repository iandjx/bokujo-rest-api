import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.cow import Cow, CowList
from resources.mastitis import Mastitis
from resources.mastitis_medications import MastitisMedication
from resources.user import UserRegister, User, UserLogin


app = Flask(__name__)
# Get database URL from Heroku if available else use sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'jose'
api = Api(app)
jwt = JWTManager(app)


api.add_resource(Cow, '/cow/<string:pub_id>')
api.add_resource(CowList, '/cows')
api.add_resource(MastitisMedication, '/cow/mastitis/medication/<int:mastitis_id>')
api.add_resource(Mastitis, '/cow/mastitis/<string:pub_id>')
# TODO: mastitis should take pub_id
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')


# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)