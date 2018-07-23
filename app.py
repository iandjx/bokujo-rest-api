from flask import Flask, Blueprint
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from api.restplus import api
from api.endpoints.cow import ns as cow_namespace
from api.endpoints.vaccine import ns as vaccine_namespace

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
app.wsgi_app = ProxyFix(app.wsgi_app)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(cow_namespace)
api.add_namespace(vaccine_namespace)
app.register_blueprint(blueprint)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)