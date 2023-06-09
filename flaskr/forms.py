# module to store the web-form classes for the extension Flask-WTF

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class SigninForm(FlaskForm):
    """
        Web-Form which handles User SignIn
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    """
        Web-Form which handles User SignUp
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Full Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[])
    cno = StringField('Contact number', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class AddContact(FlaskForm):
    """
        Web-Form which handles Addition of New Contacts to a user's profile
    """
    name = StringField('Full Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[])
    cno = StringField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Add Contact')
