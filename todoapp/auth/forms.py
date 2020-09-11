from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import PasswordInput
from todoapp.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', widget=PasswordInput() ,validators=[DataRequired(), Length(min=3)])
    confirm_password = StringField(
        'Confirm Password',
        widget=PasswordInput(),
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')


    def validade_username(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError('That username is taken. Plase choose a different one.')

    def validade_email(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValidationError('That email is taken. Plase choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
