from db import db

class TodoDAO(db.Model):

    __tablename__ = 'TodoTasks'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    task = db.Column(db.String)

    def __init__(self, number, task):
        self.number = number
        self.task = task

    def json(self):
        return {'number': self.number, 'task': self.task}

    @classmethod
    def find_by_id(cls, number):
        return cls.query.filter_by(id=number).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # def create(self, data):
    #     todo = data
    #     todo['id'] = self.counter = self.counter + 1
    #     self.todos.append(todo)
    #     return todo
    #
    # def update(self, id, data):
    #     todo = self.get(id)
    #     todo.update(data)
    #     return todo
    #
    # def delete(self, id):
    #     todo = self.get(id)
    #     self.todos.remove(todo)