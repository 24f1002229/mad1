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

def get_course(id=None):
    if id:
        return Course.query.filter_by(id=id).first()
    return Course.query.all()

@app.route("/add_course/<email>", methods=["GET","POST"])
def add_course(email):
    if request.method == "POST":
        id = request.form.get("id")
        name = request.form.get("name")
        description = request.form.get("description")
        newcourse = Course(id=id,name=name,description=description)
        db.session.add(newcourse)
        db.session.commit()
        return redirect(url_for("admin", email=email))
    return render_template("add_course.html",email=email)

@app.route("/edit_course/<id>/<email>", methods=["GET","POST"])
def edit_course(id,email):
    c= get_course(id)
    if request.method == "POST":
        id = request.form.get("id")
        name = request.form.get("name")
        description = request.form.get("description")
        c.id = id 
        c.name = name
        c.description = description
        db.session.commit()
        return redirect(url_for("admin", email=email))
    return render_template("edit_course.html", email=email, course=c)

@app.route("/delete_course/<id>/<email>", methods=["GET","POST"])
def delete_course(id,email):
    dc = get_course(id)
    db.session.delete(dc)
    db.session.commit()
    return redirect(url_for("admin", email=email))

@app.route("/search/<email>", methods=["GET","POST"])
def search_query(email):
    if request.method == "POST":
        search_query = request.form.get("search")
        by_user = search_by_user(search_query)
        by_course = search_by_course(search_query)

        result = {"users":by_user,"courses":by_course}
        return render_template("search.html", email=email, result=result)
    return redirect(url_for("admin", email=email))

def search_by_user(search):
    users = User.query.filter(User.email.ilike(f"%{search}%")).all()
    return users

def search_by_course(search):
    courses = Course.query.filter(Course.name.ilike(f"%{search}%")).all()
    return courses


@app.route("/user/<email>")
def user(email):
    courses = Course.query.all()
    return render_template("user.html", courses = courses, email=email)