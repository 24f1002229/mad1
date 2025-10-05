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

class Questions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    question_statement = db.Column(db.String)
    option1 = db.Column(db.String, nullable=False)
    option2 = db.Column(db.String, nullable=False)
    option3 = db.Column(db.String, nullable=False)
    option4 = db.Column(db.String, nullable=False)
    correct_option = db.Column(db.String, nullable=False)
    quiz_id = db.Column(db.Integer,db.ForeignKey("quiz.id"),nullable=False)



class Scores(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    time_stamp_of_attempt = db.Column(db.Time)
    total_scored = db.Column(db.Integer,default=00)
    quiz_id = db.Column(db.Integer,db.ForeignKey("quiz.id"),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    role = db.Column(db.Integer,default=1)
    full_name = db.Column(db.String,nullable=False)
    Qualification = db.Column(db.String,nullable=False)
    dob = db.Column(db.String,nullable=False)
    scores = db.relationship("Scores",cascade="all,delete",backref="user",lazy=True)

# 0 --> admin, 1 --> user
# 0 --> admin, 1 --> doctor, 2 --> patients