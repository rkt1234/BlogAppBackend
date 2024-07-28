from flask import Flask
from urls import createBlogUrl, deleteBlogUrl, fetchBlogsUrl, loginUrl, registerUrl, updateBlogUrl
from utils.connection import connectToDB

# setting the connection with database
conn=connectToDB()

#initialising flask app
app = Flask(__name__)
secretKey=app.config['SECRET_KEY'] = 'xJ3jc9O'

# Registration API
@app.route('/app/register', methods=['POST'])
def register():
    return registerUrl(conn, secretKey)

# Login API
@app.route('/app/login',methods=['POST'])
def login():
    return loginUrl(conn,secretKey)

# Fetch all posts(to show on users feed)
@app.route('/app/fetch', methods=['GET'])
def getBlogs():
    return fetchBlogsUrl(conn,secretKey)

# Create post API
@app.route('/app/create', methods=['POST'])
def create():
    return createBlogUrl(conn,secretKey)

# Delete post API
@app.route('/app/delete', methods=['DELETE'])
def delete():
    return deleteBlogUrl(conn,secretKey)

# Update API
@app.route('/app/update',methods=['POST'])
def update():
    return updateBlogUrl(conn,secretKey)

if __name__ == "__main__" :
    app.run(debug=True)

