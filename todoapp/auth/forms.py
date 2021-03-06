from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import PasswordInput
from todoapp.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', widget=PasswordInput(), validators=[DataRequired(), Length(min=3)])
    confirm_password = StringField(
        'Confirm Password',
        widget=PasswordInput(),
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    # Custom validation
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', widget=PasswordInput(), validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
