from flask import jsonify
import jwt


def isAuthorized(self, conn, secretKey, accessToken):
    
    try :
        jwtDecoded=jwt.decode(accessToken, secretKey, algorithms="HS256")
        print(jwtDecoded)
        userName = jwtDecoded['username']
        print(userName)
        cur=conn.cursor()
        cur.execute("SELECT * FROM users WHERE userName = %s", (userName,))
        userRecord = cur.fetchone()
        if userRecord:
            return {"message":"user is present", "status":200}
        else:
            return {"message":"unauthorized user", "status":401}
        
    except jwt.ExpiredSignatureError:
        return {"message":"Expired token", "status":401}

    except jwt.InvalidTokenError:
        return {"message":"invalid token", "status":401}