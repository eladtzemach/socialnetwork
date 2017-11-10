from flask_wtf import FlaskForm
from wtforms import validators, StringField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed

class FeedPostForm(FlaskForm):
    images=FileField(
        'Select Images',
        render_kw={'multiple': True},
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'], 'Only JPEG and PNG are allowed.')]
        )
    post = StringField('Post',
    widget=TextArea(),
    validators=[validators.Length(max=1024)]
    )