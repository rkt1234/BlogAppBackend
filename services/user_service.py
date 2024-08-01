import datetime
import hashlib
from flask import jsonify, make_response, request
import jwt
from models.users import Users
from utils.authorize_user import isAuthorized

def userService(app, db):

    @app.route('/', methods=['GET'])
    def home():
        return "Hello"

    @app.route('/user/register', methods=['POST'])
    def signup():
        with app.app_context():
            try:
                data = request.get_json()
                email = data['email']
                password = data['password']
                password = hashlib.sha256(password.encode()).hexdigest()
                userName = data['userName']
                db.create_all()
                existing_user_email = Users.query.filter_by(email=email).first()
                existing_user_username = Users.query.filter_by(username=userName).first()

                if existing_user_email:
                    return make_response(jsonify({'message': 'Email already exists'}), 400)

            
                if existing_user_username:
                    return make_response(jsonify({'message': 'Username already exists'}), 400)

            
                new_user = Users(email=email, password=password, username=userName)
                db.session.add(new_user)
                db.session.commit()
                db.session.close()
                return make_response(jsonify({'message': 'User registered successfully'}), 200)
            except:
                return make_response(jsonify({'message': 'Could not register'}), 500)

    
    @app.route('/user/login', methods=['POST'])
    def login():
        with app.app_context():
            try:
                data = request.get_json()
                email = data['email']
                password = data['password']
                print(email)
                print(password)
                password = hashlib.sha256(password.encode()).hexdigest()
                user = Users.query.filter_by(email=email).first()
                if user and user.password:
                    payload = {
                    'uid': user.userid,
                    'username': user.username,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                    'iat': datetime.datetime.utcnow()
                    }
                    print(payload)
                    accessToken=jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
                    return jsonify({'message': accessToken}), 200
            
                else:
                    return jsonify({'message': 'Invalid email or password'}), 401
            except  Exception as e :
                print(f"An error occurred: {e}")
                return make_response(jsonify({'message': e}), 500)
                
    @app.route('/user/update', methods=['POST'])
    def update():
        with app.app_context():
            try:
                data = request.get_json()
                accessToken = request.headers.get('Authorization')
                userId = data['userId']
                email = data['email']
                imageUrl = data['imageUrl']
                userName = data['userName']            
                response=isAuthorized(app,accessToken)
                if response[1]==200:
                    existing_user_email = Users.query.filter_by(email=email).first()
                    existing_user_username = Users.query.filter_by(username=userName).first()
                    
                    if existing_user_email and existing_user_email.userid != userId:
                        return make_response(jsonify({'message': 'Email already exists'}), 400)
                    
                    if existing_user_username and existing_user_username.userid != userId:
                        return make_response(jsonify({'message': 'Username already exists'}), 400)
                    
                    # Update user details
                    user = Users.query.filter_by(userid=userId).first()
                    if not user:
                        return make_response(jsonify({'message': 'User not found'}), 404)
                    
                    user.email = email
                    user.username = userName
                    user.imageUrl = imageUrl
                    db.session.commit()
                    
                    return make_response(jsonify({'message': 'User updated successfully'}), 200)
                return make_response(jsonify({'message':response[0]['message'] }), 401)
            except:
                return make_response(jsonify({'message': 'Could not update'}), 500)
                    


    
