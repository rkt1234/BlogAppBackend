from flask import Flask
from urls import createBlogUrl, deleteBlogUrl, fetchBlogsUrl, loginUrl, registerUrl, updateBlogUrl
from utils.connection import connectToDB

# setting the connection with database
conn=connectToDB()

#initialising flask app
app = Flask(__name__)



# Registration API
@app.route('/app/register', methods=['POST'])
def register():
    return registerUrl(conn)

# Login API
@app.route('/app/login',methods=['POST'])
def login():
    return loginUrl(conn)

# Fetch all posts(to show on users feed)
@app.route('/app/fetch', methods=['GET'])
def getBlogs():
    return fetchBlogsUrl(conn)

# Create post API
@app.route('/app/create', methods=['POST'])
def create():
    return createBlogUrl(conn)

# Delete post API
@app.route('/app/delete', methods=['DELETE'])
def delete():
    return deleteBlogUrl(conn)

# Update API
@app.route('/app/update',methods=['POST'])
def update():
    return updateBlogUrl(conn)

if __name__ == "__main__" :
    app.run(debug=True)

