from flask import Flask

# we are initializing the application instance as a Global Variable
# this is not ideal for large applications and will be changed later
# in the application factory pattern
app = Flask(__name__)

# the routes module does not exist yet in our application
# this import is not made at the top of the script to avoid
# circular imports (which is a frequent problem in flask) 
from flaskr import routes      