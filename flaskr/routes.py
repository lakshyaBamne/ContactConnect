# module to store the routes to the view functions for the global instance of Flask app
from flask import render_template, redirect, request, url_for

from flaskr import app
from flaskr.forms import SigninForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm() # instantiating the form class defined in the forms module

    if request.method == 'GET':
        return render_template('signin.html', title='SIGN IN', form=form)
    elif request.method == 'POST':
        return redirect(url_for('user_page', username=form.username.data))
    

@app.route('/userpage/<username>', methods=['GET', 'POST'])
def user_page(username):
    if request.method == 'GET':
        return render_template('userpage.html', user=username)