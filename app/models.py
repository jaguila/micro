from app import db

#noticei how db is called from the __init__.py file. This is how sqlalchemy is called
class User(db.Model):
	#creates fields
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	
	#tells python how to print objects of this class
	def __repr__(self):
		return '<User %r>' % (self.nickname)