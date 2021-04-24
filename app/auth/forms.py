from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email=StringField('Your Email Address', validators=[Required(), Email()])
    username=StringField('Enter your preferred username', validators=[Required()])
    password=PasswordField('Password', validators=[Required(),EqualTo('password_confirm', message='Passwords do not match')])
    password_confirm=PasswordField('Confirm Passwords',validators=[Required()])
    submit=SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('An account already exists with that email address')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email=StringField('Enter your email address', validators=[Required(),Email()])
    password=PasswordField('Enter your password', validators=[Required()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Sign In')