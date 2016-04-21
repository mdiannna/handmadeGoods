from app import db


class Items(db.Model):
	__tablename__ ='items'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	photo = db.Column(db.String(255))
	price = db.Column(db.Integer)
	item_description = db.Column(db.Text)


class Users(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	center_name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	password = db.Column(db.String(255))
	tel_nr = db.Column(db.Integer)
	address = db.Column(db.String(255))
	center_description = db.Column(db.Text)

	item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
	items = db.relationship('Items',
		backref=db.backref('users', lazy='dynamic', order_by= id))
