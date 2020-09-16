from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import Length, DataRequired

class TodoForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=50)])
    description = TextField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')
