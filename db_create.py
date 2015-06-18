#!flask/bin/python
from migrate.versioning import api
#note pulling from config.py file and the objects are being imported
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()

#uses os to create the db_repository folder
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
	#versioning created
	api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
	#version controlling
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))