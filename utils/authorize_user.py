import jwt

from models.users import Users


def isAuthorized(app,accessToken):
    
    try :
        print("inside try")
        jwtDecoded=jwt.decode(accessToken, app.config['SECRET_KEY'], algorithms="HS256")
        print(jwtDecoded)
        userName = jwtDecoded['username']
        print(userName)
        return {"message":"Authorized User",}, 200
        
    except jwt.ExpiredSignatureError:
        return {"message":"Expired token"}, 401

    except jwt.InvalidTokenError:
        return {"message":"invalid token"}, 401