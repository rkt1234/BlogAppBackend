import random
from flask import request
from utils.authorization import isAuthorized


class PostsServices :

        def fetchBlogs(self,conn, secretKey):
            data = request.get_json()
            accessToken = data['accessToken']
            response=isAuthorized(self,conn,secretKey,accessToken)
            print(response)
            print()
            if response['status']== 200:
                print("inside fetch")
                cur = conn.cursor()
                cur.execute('select * FROM posts')
                record=cur.fetchall()
                print(len(record))
                conn.commit()
                return (str(len(record)))
            else:
                 return response['message']
        
        def createBlog(self,conn, secretKey):
            data = request.get_json()
            accessToken = data['accessToken']
            postId = postId=random.randint(10000, 99999)
            title = data['title']
            description = data['description']
            userId = data['userId']
            createdTime = data['createdTime']
            imageUrl = data['imageUrl']
            response=isAuthorized(self,conn,secretKey,accessToken)
            if response['status']==200:
                print("inside creation")
                cur = conn.cursor()
                cur.execute('insert into posts values(%s,%s,%s,%s,%s,%s)', (postId, userId, title, description, createdTime, imageUrl))
                conn.commit()
                return "Post added"
            else :
                 return "could not add post"
        
        def updateBlog(self,conn, secretKey):
            data = request.get_json()
            accessToken = data['accessToken']
            postId = data['postId']
            title = data['title']
            description = data['description']
            imageUrl = data['imageUrl']
            response=isAuthorized(self,conn,secretKey,accessToken)
            if response['status']==200:
                print("inside update")
                cur = conn.cursor()
                cur.execute('update posts set description = %s, title = %s, imageUrl = %s, where postId=%s', (description, title, imageUrl, postId))
                conn.commit()
                return "Post updated"
            else :
                 return "could not update post"
        
        def deleteBlog(self,conn, secretKey):
            data=request.get_json()
            accessToken=data['accessToken']
            postId=data['postId']
            response=isAuthorized(self,conn,secretKey,accessToken)
            if response['status']==200:
                print("inside delete")
                cur = conn.cursor()
                cur.execute('delete from posts where postId = %s', (postId,))
                conn.commit()
                return "Post deleted"
            else :
                 return "could not delete post"