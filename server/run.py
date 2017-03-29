from app import app, db

from flask import Flask
# from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.login import LoginManager


app = Flask(__name__)


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<MDiana>",
    password="<dyannna123>",
    hostname="<mysql.server>",
    databasename="<MDiana$db>",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

# db = web.database(dbn = 'mysql', db = 'MDiana$db', user = 'MDiana', pw = 'dyannna123', host='mysql.pythonanywhere-services.com', port=3306)

# db.create_all()
migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_commw3qand('db', MigrateCommand)



# login_manager = LoginManager()
# login_manager.init_app(app)

from app import views, models


