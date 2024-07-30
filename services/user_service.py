import datetime
import hashlib
from flask import jsonify, request
import jwt
from models.users import Users

def userService(app, db):

    @app.route('/user/register', methods=['POST'])
    def signup():
        with app.app_context():
            data = request.get_json()
            email = data['email']
            password = data['password']
            password = hashlib.sha256(password.encode()).hexdigest()
            userName = data['userName']
            db.create_all()
            existing_user_email = Users.query.filter_by(email=email).first()
            existing_user_username = Users.query.filter_by(username=userName).first()

            if existing_user_email:
                return jsonify({'message': 'Email already exists'}), 400
        
            if existing_user_username:
                return jsonify({'message': 'Username already exists'}), 400
        
            new_user = Users(email=email, password=password, username=userName)
            db.session.add(new_user)
            db.session.commit()
            db.session.close()

            return jsonify({'message': 'User registered successfully'}), 200
    
    @app.route('/user/login', methods=['POST'])
    def login():
        with app.app_context():
            data = request.get_json()
            email = data['email']
            password = data['password']
            password = hashlib.sha256(password.encode()).hexdigest()
            user = Users.query.filter_by(email=email).first()
            expiry_minutes = 60
            expiry_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiry_minutes)
            if user and user.password:
                payload = {
                'email': user.email,
                'username': user.username,
                'exp': expiry_time
                }
                print(payload)
                accessToken=jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
                return jsonify({'message': accessToken}), 200
        
            else:
                return jsonify({'message': 'Invalid email or password'}), 401
            


    
