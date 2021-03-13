from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import Todo
from models import TodoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['MYSQL_USER'] = 'roothello'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'flask-react-practice'

app.config.from_pyfile('config.py')


db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_method = request.method
    todos = TodoModel.query.all()
    if request.method == 'POST':
        first_name = request.form['first_name']
        return redirect(url_for('name', first_name=first_name))
    return render_template('hello.html', list_of_names=['Chris', 'Pizza', 'Ben'],
                           request_method=request_method,
                           todos=todos)


@app.route('/name/<string:first_name>')
def name(first_name):
    return first_name


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        todo = TodoModel(content=todo_form.content.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('todo.html', form=todo_form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<string:name>')
def greet(name):
    return "hello " + name


if __name__ == '__main__':
    app.run(debug=True)
