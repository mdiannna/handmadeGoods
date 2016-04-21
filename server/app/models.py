from app import db


class Items(db.Model):
	__tablename__ ='items'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	photo = db.Column(db.String(255), nullable=False)
	price = db.Column(db.Integer, nullable=False)
	item_description = db.Column(db.Text, nullable=False)


class Users(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	center_name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), nullable=False)
	password = db.Column(db.String(255), nullable=False)
	tel_nr = db.Column(db.Integer, nullable=False)
	address = db.Column(db.String(255), nullable=False)
	center_description = db.Column(db.Text, nullable=False)

	item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
	items = db.relationship('Items',
		backref=db.backref('users', lazy='dynamic', order_by= id))
