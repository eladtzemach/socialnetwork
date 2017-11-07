from flask import Flask
from flask_mongoengine import MongoEngine 

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    db.init_app(app) # initialize db
    
    from user.views import user_app
    app.register_blueprint(user_app)
    from relationship.views import relationship_app
    app.register_blueprint(relationship_app)
    
    return app