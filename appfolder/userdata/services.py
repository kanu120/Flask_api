from flask import redirect
import appfolder.userdata.schema as schema
from appfolder import db
from appfolder.userdata.models import User
from flask import redirect, url_for
from appfolder.userdata.schema import UserSchema
#from appfolder.userdata.interface import UserdataInterface

def insert(username,password,email):
        data: User = User(username=username, emailid=email, password=password)
        db.session.add(data)
        db.session.commit()
        #return redirect(url_for('login'))
        return User


def delete_by_id(user_id: int):
        data = User.query.filter(User.id == user_id).first()
        if not data:
            return []
        db.session.delete(data)
        db.session.commit()
        return [user_id]


def get_by_id(user_id: int) -> User:
    return User.query.get(user_id)

def update(user_id,uname,pwd,mail) :
       data=User.query.get(user_id)
       data.username=uname
       data.password=pwd
       data.emailid=mail
       db.session.commit()
       return  User.query.get(user_id)

#def update(widget: User, Widget_change_updates: UserdataInterface) -> User:
#        widget.update(Widget_change_updates)
#        db.session.commit()
#       return widget


def insertintofile (username, password,email):
    if(schema.check(username)== True):
        outfile=open('data.txt','a')
        outfile.write("username:" + username + "\n")
        outfile.write("password:"+ password + "\n")
        outfile.write("Email id:"+ email+ "\n")
        outfile.close()
        return 1
    else:
        return 0




