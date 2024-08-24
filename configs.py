class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://trail_owner:KC3FnYcO5xBp@ep-blue-scene-a5e7rn2t.us-east-2.aws.neon.tech/sample?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,  # Enable keep-alive
        'pool_size': 10,        # Optional: Configure pool size
        'max_overflow': 5,      # Optional: Number of connections to create if the pool is full
    }
    # JWT_SECRET_KEY = 'your_jwt_secret_key'