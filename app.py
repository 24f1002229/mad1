from flask import Flask
from Backend.model import db

app = Flask(__name__)

def setup():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) #connection between db and app 
    app.app_context().push() #direct access to modeules
    print("App is started!!!") #you can skip it 
    return app 

app = setup()

from Backend.controller import *

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
