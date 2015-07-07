from app import db

#noticei how db is called from the __init__.py file. This is how sqlalchemy is called
class User(db.Model):
	#creates fields
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	
        def __repr__(self):
		return '<User %r>' % (self.nickname)
class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        body = db.Column(db.String(140))
        timestamp=db.Column(db.DateTime)
        #foreign key brings the link to user.id
        user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
        
	
	#tells python how to print objects of this class
	def __repr__(self):
		return '<Post %r>' % (self.body)