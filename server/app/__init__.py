from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.secret_key = "secret"

Bootstrap(app)


# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="<MDiana>",
#     password="<dyannna123>",
#     hostname="<MDiana.mysql.pythonanywhere-services.com>",
#     databasename="<MDiana$db>",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://MDiana:dyannna123@MDiana.mysql.pythonanywhere-services.com/MDiana$db"
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

# db = web.database(dbn = 'mysql', db = 'MDiana$db', user = 'MDiana', pw = 'dyannna123', host='mysql.pythonanywhere-services.com', port=3306)

db.create_all()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)



login_manager = LoginManager()
login_manager.init_app(app)

from app import views, models


