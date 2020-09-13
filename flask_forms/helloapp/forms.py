from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired,Length, Email, ValidationError

# Define QuoteForm below
class QuoteForm(FlaskForm):
    qstring = StringField("Quote",
            validators=[DataRequired(message='This field is required.'),
            Length(min=3, max=100, message='Field must be between 3 and 200 characters long.')])
    qauthor = StringField("Quote Author",
            validators=[DataRequired(message="This field is required."),
            Length(min=3, max=100, message='Field must be between 3 and 100 characters long.')])
    submit = SubmitField("Add Quote")