import datetime
import hashlib
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token
import jwt
from models.users import Users

from models.dbinit import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def home():
    return "Hello"

@user_bp.route('/register', methods=['POST'])
def signup():
    
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        password = hashlib.sha256(password.encode()).hexdigest()
        userName = data['userName']
        imageUrl=data['imageUrl']
        existing_user_email = Users.query.filter_by(email=email).first()
        existing_user_username = Users.query.filter_by(username=userName).first()

        if existing_user_email:
            return make_response(jsonify({'message': 'Email already exists'}), 400)

    
        if existing_user_username:
            return make_response(jsonify({'message': 'Username already exists'}), 400)

    
        new_user = Users(email=email, password=password, username=userName, imageurl=imageUrl)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return make_response(jsonify({'message': 'User registered successfully'}), 200)
    except:
        return make_response(jsonify({'message': 'Could not register'}), 500)


@user_bp.route('/login', methods=['POST'])
def login():
   
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        print(email)
        print(password)
        password = hashlib.sha256(password.encode()).hexdigest()
        user = Users.query.filter_by(email=email).first()
        if user and user.password==password:
            payload = {
            'username': user.username,
            'imageurl': user.imageurl,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
            }
            print(payload)
            accessToken=create_access_token(identity=user.userid,  additional_claims=payload
    )
            return jsonify({'message': accessToken}), 200
    
        else:
            return jsonify({'message': 'Invalid email or password'}), 401
    except  Exception as e :
        print(f"An error occurred: {e}")
        return make_response(jsonify({'message': e}), 500)
       
                    


    
