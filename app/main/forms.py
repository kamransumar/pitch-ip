from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
# from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField


class UpdateProfile(FlaskForm):
    username = TextAreaField('enter username')
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch title')
    category = SelectField('Pitch Category', choices=[('product', 'product'),
                                                      ('service', 'service'),         ('promotion', 'promotion'),     ('interview', 'interview')])
    content = TextAreaField('pitch your pitch')

    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    content = TextAreaField('comment')
    submit = SubmitField('Submit')
