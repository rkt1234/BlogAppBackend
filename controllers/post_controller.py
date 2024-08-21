from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required

from models.posts import Post
from models.dbinit import db

post_bp = Blueprint('post', __name__)



@post_bp.route('/create', methods=['POST'])
@jwt_required()
def createBlog():
      data = request.get_json()
      title = data['title']
      description = data['description']
      userId = data['userId']
      createdTime = data['createdTime']
      imageUrl = data['imageUrl']
      authorName = data['authorName']
      authorImageUrl = data['authorImageUrl']
      
      try:
            blog = Post(title=title, description=description, userid=userId, createdtime=createdTime, imageurl=imageUrl, authorname=authorName, authorimageurl= authorImageUrl)
            db.session.add(blog)
            db.session.commit()
            return make_response(jsonify({'message': 'Blog created successfully'}), 200)
      except:
            return make_response(jsonify({'message': 'Could not create'}), 500)  

@post_bp.route('/delete', methods=['DELETE'])
@jwt_required()
def deleteBlog():
      accessToken = request.headers.get('Authorization')
      data = request.get_json()
      postId=data['postId']
      try :
            db.session.query(Post).filter(Post.postid == postId).delete()
            db.session.commit()
            return make_response(jsonify({'message': 'Blog deleted successfully'}), 200)
      except :
            return make_response(jsonify({'message': 'Could not delete'}), 500)  
      

@post_bp.route('/update', methods=['POST'])
@jwt_required()
def updateBlog():
      data = request.get_json()
      postId=data['postId']
      title = data['title']
      description = data['description']
      createdTime = data['createdTime']
      imageUrl = data['imageUrl']
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
      

@post_bp.route('/fetch', methods=["GET"])
def fetchBlogs():
      uId = request.headers.get('uid')
      posts=[]
      try:
            blogs = Post.query.filter(Post.userid != uId).all()
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

@post_bp.route('/fetch/userpost', methods=["GET"])
def fetchUserBlogs():
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
            return make_response(jsonify({'message': posts }), 200)

      except:
            return make_response(jsonify({'message': 'Could not fetch'}), 500)
                
            
         
