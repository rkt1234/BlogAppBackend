from sqlalchemy import ForeignKey
from models.dbinit import db


class Post(db.Model):
    __tablename__ = 'posts'
    
    postid = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    userid = db.Column(db.Integer, ForeignKey('users.userid', ondelete='CASCADE'), nullable=False, index=True)
    createdtime = db.Column(db.Text, nullable=False)
    imageurl = db.Column(db.String(255), nullable=False)
    authorname = db.Column(db.String(255), nullable=False)
    authorimageurl = db.Column(db.String(255), nullable=False)
    
