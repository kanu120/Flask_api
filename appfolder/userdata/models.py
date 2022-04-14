from appfolder import db

#creating schema for the database
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True)
    emailid=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))

    def __init__(self,username,emailid,password):
        self.username=username
        self.emailid=emailid
        self.password=password

    def __repr__(self):
        return '<User %r>' % self.username