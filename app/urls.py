from services.users import UserServices

ob=UserServices()

def loginUrl(conn):
    return ob.loginUser(conn)

def registerUrl(conn):
    return ob.registerUser(conn)