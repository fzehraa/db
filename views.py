from datetime import datetime
from flask import current_app, render_template
#from forms import RegistrationForm, LoginForm

#current_app for, database is stored in the application’s configuration we need a way of accessing the application object from the view

def home_page():
    bugun = datetime.today()
    this_day = bugun.strftime("%A")
    return render_template("home_page.html", day = this_day)

def profile_page():
    #db = current_app.config["db"] #thanks to current_app, database can be accessed through configuration
    #movies = db.get_movies()
    return render_template("movie.html")#, movies=sorted(movies)

def register_page():
    #form = RegistrationForm()
    return render_template("register.html")

def login_page():
    #form = LoginForm()
    return render_template("login.html")

 