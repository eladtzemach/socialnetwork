from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from user.models import User
import re
from wtforms.widgets import TextArea

class BaseForm(FlaskForm):
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    username = StringField('Username', [validators.Required(), validators.length(min=4, max=25)])
    bio = StringField('Bio', widget=TextArea())
    
class PasswordBaseForm(FlaskForm):
    password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirm',message='Passwords need to match!')])
    confirm = PasswordField('Confirm Password')
    
class RegisterForm(BaseForm, PasswordBaseForm):
    
    def validate_username(form, field):
        if User.objects.filter(username=field.data).first():
            raise ValidationError("Username already exists!")
        # if the string does not contain any of the following of length 4-25, reject it
        if not re.match("^[a-zA-Z0-9_-]{4,25}$", field.data):
            raise ValidationError("Invalid username.")
            
    def validate_email(form, field):
        if User.objects.filter(email=field.data).first():
            raise ValidationError("Email already exists!")
            
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
    

class EditForm(BaseForm):
    image = FileField('Profile Image', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'],
        'Only JPEG, PNG or GIF is allowed')])

class ForgotForm(FlaskForm):
    email = EmailField('Email Address',
    [validators.DataRequired(), validators.Email()])
    
class PasswordResetForm(PasswordBaseForm):
    current_password = PasswordField('Current Password',
    [validators.DataRequired()])