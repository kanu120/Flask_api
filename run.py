from appfolder import connection,db


if __name__=="__main__":
        app=connection('dev')
        with app.app_context():
          db.create_all()
        app.run()


        
