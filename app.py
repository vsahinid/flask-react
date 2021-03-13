from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    request_method = request.method
    return render_template('base.html', list_of_names=['Chris', 'Pizza', 'Ben'], request_method=request_method)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<string:name>')
def greet(name):
    return "hello " + name


if __name__ == '__main__':
    app.run(debug=True)
