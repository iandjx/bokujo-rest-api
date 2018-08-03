import os

from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT
from resources.cow import Cow, CowList
from resources.vaccine import Vaccine
from resources.sickness import Sickness
from resources.medication import Medication
from resources.cowrelationship import CowRelationshipList

app = Flask(__name__)
# Get database URL from Heroku if available else use sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'jose'
api = Api(app)


api.add_resource(Cow, '/cow/<string:private_id>')
api.add_resource(CowList, '/cows')
api.add_resource(Vaccine, '/cow/<string:private_id>/vaccine')
api.add_resource(Sickness, '/cow/<string:private_id>/sickness')
api.add_resource(Medication, '/cow/sickness/<int:_id>/medication')
api.add_resource(CowRelationshipList, '/cows/cowrelationships')

# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)