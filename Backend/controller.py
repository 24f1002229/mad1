from flask import Flask, request, render_template, url_for, redirect
from .model import *
from app import app 

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def Login():
    if request.method == "POST":
        email = request.form.get("email")
        pwd = request.form.get("password")
        rol = int(request.form.get("role"))
        user = User.query.filter_by(email=email, password=pwd, role=rol).first()
        if user and user.role == 0:
            return redirect(url_for("admin", email=email))
        elif user and user.role ==1:
            return redirect(url_for("user", email=email))
        else:
            return render_template("login.html", msg="Invalid user")
        
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def Register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")
        # full_name = request.form.get("full_name")
        # Qualification = request.form.get("Qualification")
        # dob = request.form.get("dob")
        user = User.query.filter_by(email=email, password=password, role=role).first()
        if user:
            return render_template("Register.html", msg="User is already there you can simply login")
        newuser = User(email=email, password=password, role=role)
        db.session.add(newuser)
        db.session.commit()
        return render_template("login.html", msg="you have successfully registered and do login")
    return render_template("Register.html")

@app.route("/admin/<email>")
def admin(email):
    courses = get_course()
    return render_template("admin.html", email=email, courses=courses)

def get_course():
    courses = Course.query.all()
    return courses

@app.route("/add_course/<email>", methods=["GET","POST"])
def add_course(email):
    if request.form.get("POST"):
        id = request.form.get("id")
        name = request.form.get("name")
        description = request.form.get("description")
        newcourse = Course(id=id,name=name,description=description)
        db.session.add(newcourse)
        db.session.commit()
        return redirect(url_for("admin", email=email))
    return render_template("add_course.html",email=email)

@app.route("/edit_course/<id>/<name>", methods=["GET","POST"])
def edit_course():
    course= get_course(id)
    if request.form.get("POST"):
        id = request.form.get("id")
        name = request.form.get("name")
        description = request.form.get("description")
        course.id = id 
        course.name = name
        course.description = description
        db.session.commit()
        return redirect(url_for("admin", name=name))
    return render_template("edit_course.html", name=name, course=course)

@app.route("/user/<email>")
def user(email):
    return render_template("user.html", email=email)