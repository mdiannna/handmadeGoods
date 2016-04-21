from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, IntegerField, PasswordField, SubmitField
# from wtforms.ext.sqlalchemy.fields import QuerySelectField

from models import Items, Users

class addProductForm(Form):
    name = TextField('Name:')
    photo = TextField('Link to photo:')
    price = IntegerField('Price:')
    item_description = TextAreaField('Item description:')
    submit = SubmitField('Add')
