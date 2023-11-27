import os

# grap folder where the script lives

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

# define full path of the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
