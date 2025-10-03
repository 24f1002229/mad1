from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    description = db.Column(db.String)
    chapters = db.relationship("Chapter", backref="course", cascade="all,delete",lazy=True)

class Chapter(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    no_of_question = db.Column(db.Integer, default=0)
    description = db.Column(db.String)
    course_id = db.Column(db.Integer,db.ForeignKey("course.id"), nullable=False)
    quizzes = db.relationship("Quiz", backref="chapter", cascade="all,delete",lazy=True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String,nullable=False)
    remarks = db.Column(db.String)
    Chapter_id = db.Column(db.Integer,db.ForeignKey("chapter.id"), nullable=False)

