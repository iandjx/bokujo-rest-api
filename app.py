from flask import Flask, Blueprint
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from api.restplus import api
from api.endpoints.cows import ns as cow_namespace
from api.endpoints.vaccine import ns as vaccine_namespace
from api.endpoints.artificialinsemination import ns as artifical_insemination_namespace
from api.endpoints.user import ns as user_namespace
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
app.wsgi_app = ProxyFix(app.wsgi_app)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

# api = Api(app, authorizations=authorizations)

blueprint = Blueprint('api', __name__, url_prefix='/api')

api.init_app(blueprint)
api.add_namespace(cow_namespace)
api.add_namespace(vaccine_namespace)
api.add_namespace(artifical_insemination_namespace)
api.add_namespace(user_namespace)
app.register_blueprint(blueprint)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)