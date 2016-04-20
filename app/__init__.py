from flask import Flask 
from flask.ext.script import Manager 
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.secret_key = "secret"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/handmadeGoods.db'
# 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/diana/handmadeGoods/handmadeGoods.db'
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////home/corina/dodo/app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)



login_manager = LoginManager()
login_manager.init_app(app)

from app import views, models


