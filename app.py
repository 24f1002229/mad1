from flask import Flask
from Backend.model import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database"
db.init_app(app)


@app.route('/')
def home():
    return "Hello World"


if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
