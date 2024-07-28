from services.posts import PostsServices
from services.users import UserServices

userServices=UserServices()
postsServices=PostsServices()

def loginUrl(conn):
    return userServices.loginUser(conn)

def registerUrl(conn):
    return userServices.registerUser(conn)

def fetchBlogsUrl(conn):
    return postsServices.fetchBlogs(conn)

def createBlogUrl(conn):
    return postsServices.createBlog(conn)

def updateBlogUrl(conn):
    return postsServices.updateBlog(conn)

def deleteBlogUrl(conn):
    return postsServices.deleteBlog(conn)