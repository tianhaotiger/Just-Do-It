from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField, HiddenField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import HiddenInput


class TaskForm(FlaskForm):
    id = DecimalField('id',
                      # widget=HiddenInput()
                      )
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d' , validators=[DataRequired()])
    status = HiddenField('status')
    submit = SubmitField('Save Changes')