import random
from flask import Flask, request, session
import requests
import psycopg2
from database_operations import DatabaseOperations

print("Connecting to database........")
USERNAME = "trail_owner"
PASSWORD = "KC3FnYcO5xBp"

try:
# Establish the connection
    conn = psycopg2.connect(
    dbname="sample",
    user=USERNAME,
    password=PASSWORD,
    host="ep-blue-scene-a5e7rn2t.us-east-2.aws.neon.tech",
    port="5432",
    sslmode="require"
    )
    print("Connection succeeded")

except Exception as error:
    print(f"Error connecting to the database: {error}")

app = Flask(__name__)
ob=DatabaseOperations()

# Registration API
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    userName = data['username']
    password = data['password']
    return ob.registerUser(conn, email, userName, password)

# Login API
@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    return ob.loginUser(conn, email, password)

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
@app.route('/delete', methods=['POST'])
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

