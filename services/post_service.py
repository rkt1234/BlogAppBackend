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
            response=isAuthorized(app,accessToken)
            db.create_all()
            if response[1]==200:
                  try:
                        print("blog ban rha h")
                        blog = Post(title=title, description=description, userid=userId, createdtime=createdTime, imageurl=imageUrl)
                        db.session.add(blog)
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
          try:
            blogs = Post.query.all()
            print(type(blogs))
            print(len(blogs))
            for blog in blogs:
                  print(blog.title)
            return make_response(jsonify({'message':'All posts' }), 401)
          except:
                return make_response(jsonify({'message': 'Could not fetch'}), 500)  

                
            
         
