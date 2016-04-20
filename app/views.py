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
    print(request.method)
    return repr(db)


@app.route('/getvalue/', methods=['GET', 'POST'])
def get_value():
    tag = request.values.get('tag')
    value = db.get(tag, '')
    print(request.method)

    # tag = 'hello'
    # value = 'Asdf'
    # /return "hello"
    return json.dumps(['VALUE', tag, value])


@app.route('/tinywebdb/storeavalue/', methods=['GET', 'POST'])
def store_value():
    values = request.values
    tag = values.get('tag')
    value = values.get('value')
    print(request.method + "store")
    db[tag] = value
    print (db)

    return json.dumps(['STORED', tag, value])

@app.route('/storeavalue/', methods=['GET', 'POST'])
def store_value_2():
    # global i
    # i = i+1
    values = request.values
    tag = values.get('tag')
    value = values.get('value')
    tag = 'hello'
    value = 'Asdf'

    print(request.method + "store")
    db[tag] = value
    print (db)

    return json.dumps(['STORED', tag, value])

