from flask import jsonify, make_response, request

from models.posts import Post
from utils.authorize_user import isAuthorized

def postService(app, db) :

    @app.route('/post/create', methods=['POST'])
    def createBlog():
            data = request.get_json()
            accessToken = request.headers.get('Authorization')
            print(accessToken)
            title = data['title']
            description = data['description']
            userId = data['userId']
            createdTime = data['createdTime']
            imageUrl = data['imageUrl']
            authorName = data['authorName']
            authorImageUrl = data['authorImageUrl']
            response=isAuthorized(app,accessToken)
            db.create_all()
            if response[1]==200:
                  try:
                        print("blog ban rha h")
                        print(response[0]['message'])
                        blog = Post(title=title, description=description, userid=userId, createdtime=createdTime, imageurl=imageUrl, authorname=authorName, authorimageurl= authorImageUrl)
                        db.session.add(blog)
                        print("add ho rha h ")
                        db.session.commit()
                        return make_response(jsonify({'message': 'Blog created successfully'}), 200)
                  except:
                        return make_response(jsonify({'message': 'Could not create'}), 500)  
            return make_response(jsonify({'message':response[0]['message'] }), 401)
    
    @app.route('/post/delete', methods=['DELETE'])
    def deleteBlog():
          accessToken = request.headers.get('Authorization')
          data = request.get_json()
          postId=data['postId']
          response=isAuthorized(app,accessToken)
          if response[1]==200:
                try :
                  db.session.query(Post).filter(Post.postid == postId).delete()
                  db.session.commit()
                  return make_response(jsonify({'message': 'Blog deleted successfully'}), 200)
                except :
                      return make_response(jsonify({'message': 'Could not delete'}), 500)  
          return make_response(jsonify({'message':response[0]['message'] }), 401)
    
    @app.route('/post/update', methods=['POST'])
    def updateBlog():
          print("inside update")
          accessToken = request.headers.get('Authorization')
          data = request.get_json()
          postId=data['postId']
          title = data['title']
          description = data['description']
          createdTime = data['createdTime']
          imageUrl = data['imageUrl']
          response=isAuthorized(app,accessToken)
          if response[1]==200:
                try:
                  blog = Post.query.filter_by(postid=postId).first()
                  blog.title = title
                  blog.description = description
                  blog.createdtime = createdTime
                  blog.imageurl = imageUrl
                  db.session.commit()
                  return make_response(jsonify({'message': 'Blog updated successfully'}), 200)
                except:
                   return make_response(jsonify({'message': 'Could not update'}), 500)   
          return make_response(jsonify({'message':response[0]['message'] }), 401)
    
    @app.route('/post/fetch', methods=["GET"])
    def fetchBlogs():
          print("here")
          print("inside update")
          uId = request.headers.get('uid')
          posts=[]
          try:
            blogs = Post.query.filter(Post.userid != uId).all()

            print(type(blogs))
            print(len(blogs))
            for blog in blogs:
                  postData = {'postid': blog.postid,
                'title': blog.title,
                'description': blog.description,
                'userid': blog.userid,
                'createdtime': blog.createdtime,
                'imageurl': blog.imageurl,
                'authorname': blog.authorname,
                'authorimageurl': blog.authorimageurl
                }
                  posts.append(postData)
                  print(blog)
            print(len(posts))
            return make_response(jsonify({'message': posts }), 200)
          except:
                return make_response(jsonify({'message': 'Could not fetch'}), 500)  
      
    @app.route('/post/fetch/userpost', methods=["GET"])
    def fetchUserBlogs():
         print("inside fetch user post")
         uId = request.headers.get('uid')
         print(uId)
         posts=[]
         try:
              blogs = Post.query.filter(Post.userid == int(uId)).all()
              print(len(blogs))
              for blog in blogs:
                   postData = {'postid': blog.postid,
                'title': blog.title,
                'description': blog.description,
                'userid': blog.userid,
                'createdtime': blog.createdtime,
                'imageurl': blog.imageurl,
                'authorname': blog.authorname,
                'authorimageurl': blog.authorimageurl
                }
                   posts.append(postData)
                   print(blog)
                   print(posts)
                   print(len(posts))
              return make_response(jsonify({'message': posts }), 200)
    
         except:
            return make_response(jsonify({'message': 'Could not fetch'}), 500)
                
            
         
