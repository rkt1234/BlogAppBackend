import random
from flask import Flask, request
from urls import loginUrl, registerUrl
from models.database_operations import DatabaseOperations
from utils.connection import connectToDB

# setting the connection with database
conn=connectToDB()

app = Flask(__name__)
ob=DatabaseOperations()

# Registration API
@app.route('/app/register', methods=['POST'])
def register():
    return registerUrl(conn)

# Login API
@app.route('/app/login',methods=['POST'])
def login():
    return loginUrl(conn)

# Fetch all posts(to show on users feed)
@app.route('/fetch', methods=['GET'])
def getBlogs():
    return ob.fetchBlogs(conn)

# Create post API
@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    postId = postId=random.randint(10000, 99999)
    title = data['title']
    description = data['description']
    userId = data['userId']
    createdTime = data['createdTime']
    imageUrl = data['imageUrl']
    return ob.createPost(conn, postId, title, description, userId, createdTime, imageUrl)

# Delete post API
@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    postId = data['postId']
    return ob.deletePost(conn, postId)

# Update API
@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()
    postId = data['postId']
    title = data['title']
    description = data['description']
    imageUrl = data['imageUrl']
    return ob.updatePost(conn, postId, description, title, imageUrl)

if __name__ == "__main__" :
    app.run(debug=True)

