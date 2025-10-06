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

        print(email)
        print(pwd)
        if user and user.role == 0:
            return redirect(url_for("admin"))
        elif user and user.role ==1:
            return redirect(url_for("user"))
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
        user = User.query.filter_by(email=email, password=password).first()
        print("Form Data:", request.form)
        if user:
            return render_template("Register.html", msg="User is already there you can simply login")
        newuser = User(email=email, password=password, role=role)
        db.session.add(newuser)
        db.session.commit()
        return render_template("login.html", msg="you have successfully registered and do login")
    return render_template("Register.html")

@app.route("/admin/<email>")
def admin(email):
    return render_template("admin.html", email=email)


@app.route("/user")
def user():
    return render_template("user.html")