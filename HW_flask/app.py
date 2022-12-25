from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

from model import Visitor
from settings import *

menu = [
    {'name': 'Home', 'url': ''},
    {'name': 'Invitation', 'url': 'invitation'},
    {'name': 'Visitors', 'url': 'visitors'},
    {'name': 'Feedback', 'url': 'feedback'},
]


@app.route('/')
def index():
    return render_template(
        'index.html', title='Party', menu=menu
    )


@app.route('/invitation')
def invitation():
    return render_template('invitation.html', title='Invitation', menu=menu)


@app.route('/invite', methods=['POST'])
def invite():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']
    email = request.form['email']

    new_visitor = Visitor(
        firstname=firstname,
        lastname=lastname,
        age=age,
        email=email,
    )

    db.session.add(new_visitor)
    db.session.commit()

    return redirect('/visitors')


@app.route('/visitors')
def visitors():
    list_visitors = Visitor.query.all()
    return render_template(
        'visitors.html', title='Visitors', list=list_visitors, menu=menu
    )


@app.route('/feedback')
def fb():
    return render_template('feedback.html', title='Feedback', menu=menu)


if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)
