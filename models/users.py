from models.dbinit import db

class Users(db.Model):
    __tablename__ = 'users'

    userid=db.Column(db.Integer, primary_key=True, autoincrement=True)
    email=db.Column(db.Text, nullable=False, index=True)
    password=db.Column(db.Text, nullable=False)
    username=db.Column(db.Text, nullable=False)
    imageurl=db.Column(db.Text, nullable=False)