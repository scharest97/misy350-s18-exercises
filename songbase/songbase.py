from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form-basics')
def formbasics():
    return render_template('form-basics.html')

@app.route('/form-demo')
def form_demo():
    first_name= request.args.get('first_name')
    return first_name

@app.route('/user')
def user():
    return "this is the page for users"

if __name__ == '__main__':
    app.run()
