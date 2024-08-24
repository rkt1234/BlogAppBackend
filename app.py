from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import create_engine, text
import configs
from models.dbinit import db
from models.posts import Post
from models.users import Users
from controllers.user_controller import user_bp
from controllers.post_controller import post_bp

# Initialize the Flask application
app = Flask(__name__)

# Load the configuration settings, including pool_pre_ping
app.config.from_object(configs.Config)

# Initialize the database and migration tools
db.init_app(app)
with app.app_context():
    print("starting")
    db.create_all()
    print("ending")
migrate = Migrate(app, db)

# Initialize the JWT manager
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(post_bp, url_prefix='/post')

# Function to keep the database alive
def keep_db_alive():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

# Initialize APScheduler and add job
scheduler = BackgroundScheduler()
scheduler.add_job(keep_db_alive, 'interval', minutes=5)
scheduler.start()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True)
