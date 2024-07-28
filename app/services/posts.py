import random
from flask import request


class PostsServices :

        def fetchBlogs(self,conn):
            print("inside fetch")
            cur = conn.cursor()
            cur.execute('select * FROM posts')
            record=cur.fetchall()
            print(len(record))
            conn.commit()
            return (str(len(record)))
        
        def createBlog(self,conn):
            data = request.get_json()
            postId = postId=random.randint(10000, 99999)
            title = data['title']
            description = data['description']
            userId = data['userId']
            createdTime = data['createdTime']
            imageUrl = data['imageUrl']
            print("inside creation")
            cur = conn.cursor()
            cur.execute('insert into posts values(%s,%s,%s,%s,%s,%s)', (postId, userId, title, description, createdTime, imageUrl))
            conn.commit()
            return "Post added"
        
        def updateBlog(self, conn):
            data = request.get_json()
            postId = data['postId']
            title = data['title']
            description = data['description']
            imageUrl = data['imageUrl']
            print("inside update")
            cur = conn.cursor()
            cur.execute('update posts set description = %s, title = %s, imageUrl = %s, where postId=%s', (description, title, imageUrl, postId))
            conn.commit()
            return "Post updated"
        
        def deleteBlog(self, conn):
            data=request.get_json()
            postId=data['postId']
            print("inside delete")
            cur = conn.cursor()
            cur.execute('delete from posts where postId = %s', (postId,))
            conn.commit()
            return "Post deleted"