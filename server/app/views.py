from app import app, db
from app import login_manager
from flask import render_template, request, redirect
from app.models import Items, Users
from datetime import datetime
from flask.ext.login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import json
from flask import Flask, request


@login_manager.user_loader
def load_user(userid):
	user = Users.query.get(userid)
	return user


@app.route('/')
def hello_world():

    print("Hello")
    print(request.method)
    return "Hello Dianaaaaaaaaaa"
    # return repr(db)


@app.route('/hello_server', methods=['GET', 'POST'])
def hello_server():
    if request.method == 'POST':
        return "posted " + request.values
    return "nothing"


@app.route('/add_product')
def add_product():
    print("add product")

@app.route('/getvalue/', methods=['GET', 'POST'])
def get_value():
    # tag = request.values.get('tag')
    # value = db.get(tag, '')

    print(request.method)

    # tag = 'hello'
    # value = 'Asdf'
    # /return "hello"
    # /return json.dumps(['VALUE', tag, value])

    if(request.method == 'POST'):
        center_name = "a"
        email = "s"
        password = "s"
        tel_nr = 233
        address = "sd"
        center_description = "sd"
        user = Users(center_name=center_name, email=email, password=password, tel_nr=tel_nr, address=address, center_description=center_description)
        db.session.add(user)
        db.session.commit()
        return "post value:" + str(request.values)

    elif(request.method == 'GET'):
        return "get value:" + str(request.values)

    return "nothing"


@app.route('/storeavalue/', methods=['GET', 'POST'])
def store_value():
    # global i
    # i = i+1
    values = request.values
    # tag = values.get('tag')
    # value = values.get('value')
    tag = 'user'
    value = 'Asdf'

    if tag == 'user':
        user_add = User(name='')

    print(request.method + "store")
    # db[tag] = value
    # print (db)

    return json.dumps(['STORED', tag, value])

