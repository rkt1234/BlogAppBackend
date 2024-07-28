from services.posts import PostsServices
from services.users import UserServices

userServices=UserServices()
postsServices=PostsServices()

def loginUrl(conn,secretKey):
    return userServices.loginUser(conn,secretKey)

def registerUrl(conn,secretKey):
    return userServices.registerUser(conn,secretKey)

def fetchBlogsUrl(conn,secretKey):
    return postsServices.fetchBlogs(conn,secretKey)

def createBlogUrl(conn,secretKey):
    return postsServices.createBlog(conn,secretKey)

def updateBlogUrl(conn,secretKey):
    return postsServices.updateBlog(conn,secretKey)

def deleteBlogUrl(conn,secretKey):
    return postsServices.deleteBlog(conn,secretKey)