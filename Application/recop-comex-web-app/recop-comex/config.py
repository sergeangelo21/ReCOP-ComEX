import pymysql

class Config(object):
	SECRET_KEY = 'random_string'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/flask_sample'
	SQLALCHEMY_TRACK_MODIFICATIONS = True