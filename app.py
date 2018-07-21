from flask import Flask
from flask_restplus import Api, Resource, fields, reqparse
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from api.honyu.endpoints.cow import CowModel
from todomodel import *

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})
@app.before_first_request
def create_tables():
    db.create_all()


# DAO = TodoDAO()
# DAO.create({'task': 'Build an API'})
# DAO.create({'task': '?????'})
# DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    parser = reqparse.RequestParser()
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        tasks = TodoDAO.query.all()
        return tasks

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        data = api.payload
        print(data)
        todo = TodoDAO(data['id'], data['task'])
        try:
            todo.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return todo.json(), 201


# @ns.route('/<int:id>')
# @ns.response(404, 'Todo not found')
# @ns.param('id', 'The task identifier')
# class Todo(Resource):
#     '''Show a single todo item and lets you delete them'''
#     @ns.doc('get_todo')
#     @ns.marshal_with(todo)
#     def get(self, id):
#         '''Fetch a given resource'''
#         return DAO.find_by_id(id)
#
#     @ns.doc('delete_todo')
#     @ns.response(204, 'Todo deleted')
#     def delete(self, id):
#         '''Delete a task given its identifier'''
#         DAO.delete(id)
#         return '', 204
#
#     @ns.expect(todo)
#     @ns.marshal_with(todo)
#     def put(self, id):
#         '''Update a task given its identifier'''
#         return DAO.update(id, api.payload)
#

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)