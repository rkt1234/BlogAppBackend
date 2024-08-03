from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://trail_owner:KC3FnYcO5xBp@ep-blue-scene-a5e7rn2t.us-east-2.aws.neon.tech/sample?sslmode=require'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hytjo89@34'
    db.init_app(app)

    from services.user_service import userService
    userService(app, db)

    from services.post_service import postService
    postService(app,db)

    return app