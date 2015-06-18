wtf_csrf_enabled = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url':'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyopenID', 'url': 'https://www.myopenid.com'}
]

import os
#gets the full pathname of the file . Note:__file__ pathname of the file calling os
basedir = os.path.abspath(os.path.dirname(__file__))

#creates the database in the current directory of config file make sure triple ///
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#creates a new folder
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')