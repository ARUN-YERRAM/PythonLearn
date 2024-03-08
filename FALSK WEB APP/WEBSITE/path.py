from flask import Blueprint

path = Blueprint('path',__name__)

@path.route('/login')
def login():
    return "<p>Login</p>"

@path.route('/logout')
def logout():
    return "<p>logout</p>"

@path.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

