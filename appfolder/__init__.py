from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from appfolder.routes import connectionroutes
from flask_restx import Api

db=SQLAlchemy()


def connection(env : str):
        app=Flask(__name__)
        if(env=='dev'):
                app.config['SQLALCHEMY_DATABASE_URI']='postgresql://datamax_user:abc123@localhost:5433/new_db'
        else:
                app.config['SQLALCHEMY_DATABASE_URI']='postgresql://datamax_user:abc123@localhost:5433/testingdb' 

        #connecting to  DB
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        db.init_app(app)
        api = Api(app, version="1.0", title="My First App")
        connectionroutes(api, app)
        return app

     








