

DEBUG = True
TEMPLATES_AUTO_RELOAD = True

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'xfz'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'abcdefghijklnmopqrstuvwx'
CMS_USER_ID = 'CMS_USER'
FRONT_USER_ID = 'FRONT_USER'