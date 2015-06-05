from flask import  render_template, flash, redirect
from app import app
from .forms import LoginForm

#below decides the urls for this particular view
#every url requires an @app and a function

#index
@app.route('/')
@app.route('/index')

def index():
	#define variables for template
	user={'nickname': 'Miguel'} #fake user
	
	posts=[#fake array of posts
	{
		'author':{'nickname':'John'},
		'body': 'Beautiful day in Portland!'
		
	},
	{
		'author':{'nickname':'Susan'},
		'body':'The Avengers movie was so cool!'
	}
	]
	
	#assign variables and parameters for html template
	return render_template('index.html',
							#title=,
							user=user,
							posts=posts
							)

#login
@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	#below will check if the login page validate fields are ok. will return true
	if form.validate_on_submit():
	#Flash - assigns message text. called into html by use of get_flashed_messages(). note it disappears after next page
		flash('Login requested for OpenID="%s", remember_me=%s' % 
			(form.openid.data, str(form.remember_me.data)))
		#tells browser to redirect to index instead of refreshing page	
		return redirect('/index')	
	return render_template('login.html',
							title='Sign in',
							form=form,
							providers=app.config['OPENID_PROVIDERS']
							)