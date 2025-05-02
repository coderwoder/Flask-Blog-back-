from flaskblog import db
from datetime import datetime,timezone
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(150),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    post=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User({self.username},{self.email},{self.image_file})"

class Post(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.now(timezone.utc)) # Not the () since we don't want the (executed) time right now
    content=db.Column(db.Text,nullable=False)
    # The 'User' model will have atomatically set the table name as 'user' same for 'Post'->'post, tb_name can be changed. 
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)  

    def __repr__(self):
        return f"Post({self.title},{self.date_posted})"
