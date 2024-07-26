from asyncio.windows_events import NULL
import random


class DatabaseOperations:

    def registerUser(self,conn, email, userName, password):
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
    
    def loginUser(self,conn, email, password):
        cur = conn.cursor()
        cur.execute('select email FROM users WHERE email = %s', (email,))
        emailRecord=cur.fetchone()
        cur.execute('select password FROM users WHERE password = %s', (password,))
        conn.commit()
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
            return "Login completed"
    
    def createPost(self,conn,postId, title, description, userId, createdTime, imageUrl):
        print("inside creation")
        cur = conn.cursor()
        cur.execute('INSERT INTO posts values(%s,%s,%s,%s,%s,%s)', (postId, userId, title, description, createdTime, imageUrl))
        conn.commit()
        return "Post added"
    
    def deletePost(self, conn, postId):
        print("inside delete")
        cur = conn.cursor()
        cur.execute('DELETE FROM posts WHERE postId = %s', (postId,))
        conn.commit()
        return "Post deleted"
        
        

            

