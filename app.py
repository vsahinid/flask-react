from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html', list_of_names=['Chris', 'Pizza', 'Ben'])


@app.route('/<string:name>')
def greet(name):
    return "hello " + name


if __name__ == '__main__':
    app.run(debug=True)
