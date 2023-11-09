from flask import flash
from flask_wtf import FlaskForm  # pip install Flask-WTF
from wtforms import StringField, EmailField, SubmitField, TextAreaField, SelectField  # pip install email-validator
from wtforms.validators import DataRequired, Email
from flask_babel import lazy_gettext as _l


class ContactForm(FlaskForm):
    full_name = StringField(label=_l('Full Name'), validators=[DataRequired()])
    email = EmailField(label=_l('Email'), validators=[DataRequired(), Email()])
    options = SelectField(label=_l('What are you after?'),
                          choices=[('', _l('Please choose one option:')), (_l('general'), _l('I have a general inquiry')),
                                   (_l('tutoring'), _l('I need tutoring')), (_l('english'), _l('I need English classes')),
                                   (_l('pyhton'), _l('I need Python classes')), (_l('web-dev'), _l('I need Web Dev classes')),
                                   ('excel', _l('I need MS Excel classes')), (_l('other'), _l('Other'))],
                          validators=[DataRequired()])
    message = TextAreaField(label=_l('Message'), validators=[DataRequired()])
    submit = SubmitField(label=_l('Send Message'))
