class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://trail_owner:KC3FnYcO5xBp@ep-blue-scene-a5e7rn2t.us-east-2.aws.neon.tech/sample?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    'pool_size': 10,
    'max_overflow': 5,
    'pool_timeout': 30,  # Timeout to wait for a connection from the pool
    'pool_recycle': 1800,  # Recycle connections after 30 minutes
}

    # JWT_SECRET_KEY = 'your_jwt_secret_key'