# module to store the application's configuration base class

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-simple-yet-powerful-secret-key'