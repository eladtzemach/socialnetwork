import os, sys
from application import db
from utilities.common import utc_now_ts as now
from mongoengine import signals
from flask import url_for
import os
from settings import IMAGE_URL, AWS_BUCKET, AWS_CONTENT_URL

class User(db.Document):
    username = db.StringField(db_field="u", required=True, unique=True)
    password = db.StringField(db_field="p", required=True)
    email = db.EmailField(db_field="e", require=True, unique=True)
    first_name = db.StringField(db_field="fn", max_length=50)
    last_name = db.StringField(db_field="ln", max_length=50)
    created = db.IntField(db_field="c", default=now())
    bio = db.StringField(db_field="b", max_length=50)
    email_confirmed = db.BooleanField(db_field="ecf", default=False)
    change_configuration = db.DictField(db_field="cc")
    profile_image = db.StringField(db_field="i",default=None)
    
    
    # indexes
    meta = {
        'indexes': ['username', 'email', '-created']
    }
    
    def profile_imgsrc(self, size):
        
        if self.profile_image:
            return os.path.join('https://s3.amazonaws.com', 'socialnetwork2', 'user', '%s%s.%s.png' % (self.id, self.profile_image, size))
        else:
            return url_for('static', filename=os.path.join(IMAGE_URL, 'user', 'no-profile.%s.png' % (size)))