from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240))

    def __str__(self):
        return self.content + self.id


db.create_all()

todo1 = TodoModel(content="I want to eat")
db.session.add(todo1)

todo2 = TodoModel(content="Second todo")
db.session.add(todo2)

db.session.commit()

# todos = TodoModel.query.all()
# print(todos[1].content)
