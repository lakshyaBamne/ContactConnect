# module to store the application's configuration base class

import os

# provides the absolute path of the directory containing the current script's file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # secret key used by Flask internally and by some extensions
    # one common use of this is to protect web-forms from (seasurf attacks) 
    # or CSRF(Common-Site Resource Forgery) attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-simple-yet-powerful-secret-key'

    # configuration variables for Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
