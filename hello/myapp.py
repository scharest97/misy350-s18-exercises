from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/users/<string:name>')
def users(name) :
    return render_template('users.html', name=name)


if __name__ == '__main__':
    app.run()
