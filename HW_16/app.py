from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/user')
def user():
    return 'My name is Alexander!'


@app.route('/user/<username>')
def user_name(username):
    return f'User {username}'


app.run()
