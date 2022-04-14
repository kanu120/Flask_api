from flask_restx import Namespace, Resource
from flask import Flask, render_template, request, jsonify
from marshmallow import Schema

from flask_sqlalchemy import SQLAlchemy
from appfolder.userdata.schema  import UserSchema
from flask_accepts import accepts, responds
import appfolder.userdata.services as services

from flask.wrappers import Response
from appfolder.userdata.models import User
#from appfolder.userdata.interface import UserdataInterface

api =Namespace('firstapi',description='api for login')


api.debug=True
@api.route("/")
class Userclass(Resource):

    # def start(self):
    #     return render_template("login.html")
    def get(self):
        return render_template("login.html")

    # @api.route("/login", methods=['POST','GET'])
    #@api.doc(params={})
    @accepts(schema=UserSchema,api=api)
    @responds(schema=UserSchema)
    def post(self):
        try:
            name1=request.json['username']
            pwd=request.json['password']
            email=request.json['email']
            value=services.insert(name1,pwd,email)
            return jsonify({"msg":"data saved"})
           # return appfolder.__init__.db.jsonify()
        except Exception as e:
            return jsonify({"error":"invalid request"})
        #return value
       # else:
        #return render_template('login.html',info='invalid data format')
    #return render_template('home.html',name=name1)
    
@api.route('/<int:user_id>')
@api.param('user_id', 'User database ID')

class UserId(Resource):

    @responds(schema=UserSchema)
    def get(self, user_id: int) -> User:
        '''Get Single Widget'''
        return services.get_by_id(user_id)

    def delete(self, user_id: int) -> Response:
        '''Delete Single Widget'''
        id = services.delete_by_id(user_id)
        return jsonify(dict(status='Success', id=id))
    
    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def put(self, user_id):
        '''Update Single Widget'''
        uname=request.json['username']
        pwd=request.json['password']
        mail=request.json['email']
        newvalues= services.update(user_id,uname,pwd,mail)

        return newvalues

   # @accepts(schema=UserSchema, api=api)
    #@responds(schema=UserSchema)
    #def put(self, userId: int) -> User:
       # '''Update only Single Widget'''

       # changes: UserdataInterface = request.parsed_obj
       # User = services.get_by_id(userId)
       # return services.update(User, changes)


        


   




