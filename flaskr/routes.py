# module to store the routes to the view functions for the global instance of Flask app
from flask import render_template, redirect, request, url_for

from flaskr import app, db
from flaskr.forms import SigninForm, SignupForm, AddContact
from flaskr.models import User, UserData, UserContacts

from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # we also need to print all the users of the application for testing
        users = UserData.query.all()

        return render_template('index.html', users=users)
    elif request.method == 'POST':
        return '<p>recieved a POST request!</p>'

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm() # instantiating the form class defined in the forms module

    if request.method == 'GET':
        return render_template('signin.html', title='SIGN IN', form=form)
    elif request.method == 'POST':
        # when we get a post request on the sign in page, we need to authorize the user
        users = User.query.all()

        user_names = [u.username for u in users]
        password_hashes = [u.password_hash for u in users]

        user_index = -1

        for i in range(0, len(user_names)):
            if user_names[i] == form.username.data:
                # user exists
                user_index = i

        if user_index >= 0:
            # user exists
            # check the entered password with the one stored in the data base
            if check_password_hash(password_hashes[user_index], form.password.data):
                print("__LOG__ CORRECT CREDENTIALS")
                return redirect(url_for('user_page', username=form.username.data))
            else:
                # user exists but wrong password entered
                print("__LOG__ WRONG PASSWORD FOR THE GIVEN USERNAME")
                return render_template('signin.html', title='SIGN IN', form=form)
        else:
            # user does not exist
            print("__LOG__ USER DOES NOT EXIST")
            return render_template('signin.html', title='SIGN IN', form=form)
             
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm() # instantiating the form class defined in the forms module

    if request.method == 'GET':
        return render_template('signup.html', title='SIGN UP', form=form)
    elif request.method == 'POST':
        # we need to add the user to the data base of users => in UserData table
        username = form.username.data
        name = form.name.data
        email = form.email.data
        contact = form.cno.data

        password_hash = generate_password_hash(form.password.data)

        new_user = UserData(username = username, name=name, email=email, contact=contact)
        new_user_add = User(username = username, password_hash = password_hash)

        # adding the user to both User and UserData tables for signin later
        db.session.add(new_user)
        db.session.add(new_user_add)
        db.session.commit()

        print("__LOG__ ADDED A NEW USER")
        return redirect(url_for('user_page', username=form.username.data))

@app.route('/userpage/<username>', methods=['GET', 'POST'])
def user_page(username):
    form = AddContact()

    # we need to display all the contacts that the user has so let us fetch them first
    all_contacts = UserContacts.query.filter_by(username=username).all()

    if request.method == 'GET':
        return render_template('userpage.html', user=username, form=form, contacts=all_contacts)
    elif request.method == 'POST':
        # now user has added a new contact and we need to add it to the UserContacts table
        new_name = form.name.data
        new_email = form.email.data
        new_cno = form.cno.data

        new_contact = UserContacts(username=username, name=new_name, email=new_email, contact=new_cno)

        db.session.add(new_contact)
        db.session.commit()

        print(f"__LOG__ ADDED CONTACT FOR {username}")
        
        return redirect(url_for('user_page', username=username))


    
