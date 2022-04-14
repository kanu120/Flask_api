# from flask import Flask, render_template, request
# import userdata.services as services
# app=Flask(__name__)

# @app.route("/")

# def start():
#     return render_template("login.html")

# @app.route("/login", methods=['POST','GET'])
# def login():
#     name1=request.form['un']
#     pwd=request.form['pw']
#     value=services.insert(name1,pwd)
#     if(value==1):
#         return render_template('home.html',name=name1)
#     else:
#         return render_template('login.html',info='invalid data format')
#     #return render_template('home.html',name=name1)

# if __name__=="__main__":
#     app.run()




