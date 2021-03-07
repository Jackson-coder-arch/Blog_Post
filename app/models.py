from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import current_user,UserMixin
from . import login_manager


class User (UserMixin, db.Model):
    __table__ = 'users'
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(255), unique =True, nullable = False)
    email = db.Column(String(255),unique = True, nullable = False)
    bio = db.Column(db.Column(255),default ='My default Bio')
    profile_pic_path = db.Column(db.String(150),default = 'default.png')
    hashed_password = db.Column(db.String(255),nullable = False)
    blog = db.relationship('Blog', backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username} '


class Blog(db.Model):
    __table__ = 'blogs'
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(255),nullable = False)
    content = db.Column(db.Text(),nullable = False)
    posted = db.Column(db.Datetime, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    comment = db.relationship('comment',backref='blog',lazy='dynamic')

    def save_b(self)
    db.session.add(self)
    db.session.commit()


class Comment(db.Model):
      __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_c(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.remove(self)
        db.session.commit()


     def get_comment(id):
        comment = Comment.query.all(id=id)
        return comment
    
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



class Subsciber(db.Model):
    
      __tablename__='subscribers'
    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'




