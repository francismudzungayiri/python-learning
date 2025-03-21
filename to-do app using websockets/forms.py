from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ToDoForm(FlaskForm):
    
    todo = StringField('What are you working on today', validators=[InputRequired()])
    submit = SubmitField('Submit') 