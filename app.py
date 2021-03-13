from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_method = request.method
    if request.method == 'POST':
        first_name = request.form['first_name']
        return redirect(url_for('name', first_name=first_name))
    return render_template('hello.html', list_of_names=['Chris', 'Pizza', 'Ben'], request_method=request_method)


@app.route('/name/<string:first_name>')
def name(first_name):
    return first_name


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<string:name>')
def greet(name):
    return "hello " + name


if __name__ == '__main__':
    app.run(debug=True)
