from app import app, db
from app import login_manager
from flask import render_template, request, redirect
from app.models import Items, Users
from datetime import datetime
from flask.ext.login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import json
from flask import Flask, request
from forms import addProductForm


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


@app.route('/items')
def items():
    items = Items.query.all()
    return render_template('items.html', items=items)

@app.route('/view_item/<int:item_id>', methods=['GET', 'POST'])
def view_item(item_id):
    item = Items.query.get(item_id)
    return render_template('viewitem.html', item=item)



@app.route('/item/add', methods=['GET', 'POST'])
def add_item():
    form = addProductForm(request.form, csrf_enabled=True)
    item_id = 1
    if request.method == 'POST' :
		item = Items(name=form.name.data, photo=form.photo.data, price=form.price.data, item_description=form.item_description.data);
		db.session.add(item )
		db.session.commit()
		item_id = item.id
		return redirect('view_item/' + str(item_id))
    print("add item:")
    return render_template('additem.html', form=form)


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

