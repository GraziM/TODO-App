from flask import Blueprint, render_template
from .forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit:
        pass
    return render_template('register.html', title='Register', form=form)

@auth.route('/register')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)