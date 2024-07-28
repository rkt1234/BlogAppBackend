import random
from flask import jsonify, request
import jwt

class UserServices:

    def loginUser(self,conn, secretKey):
        data = request.get_json()
        email = data['email']
        password = data['password']
        cur = conn.cursor()
        cur.execute('select email FROM users WHERE email = %s', (email,))
        emailRecord=cur.fetchone()
        cur.execute('select password FROM users WHERE password = %s', (password,))
        passwordRecord=cur.fetchone()
        print(type(emailRecord))
        print(type(passwordRecord))

        if emailRecord==None and passwordRecord==None:
            return "Invalid login credentials"
        
        elif emailRecord!=None and passwordRecord==None:
            return "Invalid password"
        
        elif emailRecord==None and password!=None:
            return "Invalid email"
        else:
            cur.execute('select userName FROM users WHERE email = %s', (email,))
            userName=cur.fetchone()
            type(userName[0])
            payload = {
                'email': emailRecord[0],
                'password': passwordRecord[0],
                'username': userName[0],
                'expAt': 30
                }
            print(payload)
            accessToken=jwt.encode(payload, secretKey, algorithm="HS256")
            conn.commit()

            return accessToken
        
    def registerUser(self,conn, secretKey):
            data = request.get_json()
            email = data['email']
            userName = data['username']
            password = data['password']
            cur = conn.cursor()
            cur.execute('select email FROM users WHERE email = %s', (email,))
            emailRecord=cur.fetchone()
            cur.execute('select username FROM users WHERE username = %s', (userName,))
            userNameRecord=cur.fetchone()
            if emailRecord==None and userNameRecord==None:
                uid = random.randint(10000, 99999)
                cur.execute('INSERT INTO users VALUES (%s,%s,%s,%s)', (userName, uid, email, password))
                conn.commit()
                return "Registration completed"
        
            elif emailRecord!=None:
                return "Email already in use"
        
            else:
                return "Username already in use"

