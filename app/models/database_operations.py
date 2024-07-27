from asyncio.windows_events import NULL
import random
from flask import jsonify
import jwt


class DatabaseOperations:
    
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
    
    def updatePost(self, conn, postId, description, title, imageUrl):
        print("inside update")
        cur = conn.cursor()
        cur.execute('UPDATE posts SET description = %s, title = %s, imageUrl = %s', (description, title, imageUrl))
        conn.commit()
        return "Post updated"
    
    def fetchBlogs(self,conn):
        print("inside fetch")
        cur = conn.cursor()
        cur.execute('SELECT * FROM posts')
        record=cur.fetchall()
        print(len(record))
        conn.commit()
        return (str(len(record)))
    

        

            

