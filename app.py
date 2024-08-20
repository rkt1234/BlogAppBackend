# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# def createApp():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://trail_owner:KC3FnYcO5xBp@ep-blue-scene-a5e7rn2t.us-east-2.aws.neon.tech/sample?sslmode=require'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SECRET_KEY'] = 'hytjo89@34'
#     db.init_app(app)

#     from services.user_service import userService
#     userService(app, db)

#     from services.post_service import postService
#     postService(app,db)

#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import configs
from models.dbinit import db
from models.posts import Post 
from models.users import Users 
from controllers.user_controller import user_bp
from controllers.post_controller import post_bp
# Initialize the Flask application
app = Flask(__name__)

# Load the configuration settings
app.config.from_object(configs.Config)

# Initialize the database and migration tools
db.init_app(app)
with app.app_context():
    print("Creating all tables...")
    db.create_all()
    print("Tables created.")
# migrate = Migrate(app, db)

# Initialize the JWT manager
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(post_bp, url_prefix='/post')

if __name__ == '__main__':
    app.run(debug=True)