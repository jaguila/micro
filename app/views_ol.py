from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)