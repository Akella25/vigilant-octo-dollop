from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello {}!'.format(username)

@app.route('/error')
def raise_error():
    raise RuntimeError('Jast for fan')


@app.route('/task/', methods=['GET','POST'])
def task():
    return 'Task view'

