'''

Author: Rigoberto Gort
Author Email: warriorbambino23@gmail.com

'''
# Imports
from flask import Flask, render_template, redirect, url_for, request, jsonify, session, flash, make_response, abort
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from functools import wraps
from flask import session as login_session
import random, string

#from models import Base, User, Posts

# Creates the application object
app = Flask(__name__, template_folder='templates')

# Connect to DB and create DB session
#engine = create_engine('sqlite:///website.db')
#Base.metadata.bind = engine

# Sets up db connection & session
#DBSession = sessionmaker(bind=engine)
#session = DBSession()

posts = [
    {
        'author': 'Rigo Gort',
        'title': 'Blog Post #1',
        'content': 'The first blog post for testing',
        'date_posted': 'January 4, 2019',
    }
]

# Check for user login status
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in login_session:
            return f(*args, **kwargs)
        else:
            flash('You must be logged in to access this content!')
            return redirect(url_for('login', next=request.url))
    return decorated_function

# Home Page for Application
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    #posts = session.query(Posts)
    if 'username' not in login_session:
        return render_template('index.html', posts=posts)
    else:
        return render_template('about.html', posts=posts)

# About Page for users with exclusive content access and updates
@app.route('/about')
def welcome():
    return render_template('about.html', title='About') # Renders the about.html template

# Allows the users to become a registered user on the website.
@app.route('/register')
def register():
    return render_template('index.html')

# Login Page for users to log in and check out member specific content
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST': # Verifies if the users credentials are valid
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials. Please try again."
        else:
            login_session['logged_in'] = True
            flash('Welcome back!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# Logs the user out of the application
@app.route('/logout')
@login_required
def logout():
    login_session.pop('logged_in', None)
    flash("You've successfully logged out!")
    return redirect(url_for('/')) # Redirects the logged out user to the home page

if __name__ == "__main__":
    app.secret_key = 'G0dz1lla315'
    app.run(debug=True)
    app.run(host = '0.0.0.0', port = 5000) # 0.0.0.0 tells code to listen to all public ip addresses.
