from datetime import datetime
from flask import current_app, render_template
import mysql.connector
from flask_mysqldb import MySQL
#from forms import RegistrationForm, LoginForm

#current_app for, database is stored in the application’s configuration we need a way of accessing the application object from the view

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  database="lang_exc"
)
cursor = mydb.cursor(dictionary=True)

def home_page():
    bugun = datetime.today()
    this_day = bugun.strftime("%A")
    
    sql = "SELECT * FROM user ORDER BY user_id DESC"
    cursor.execute(sql)
    users = cursor.fetchall()
    
    sql2 = "SELECT * FROM list ORDER BY list_id DESC"
    cursor.execute(sql2)
    lists = cursor.fetchall()

    sql3 = "SELECT * FROM language_in_lists"
    cursor.execute(sql3)
    lang_in_lists = cursor.fetchall()
    return render_template("home_page.html", day = this_day, kullanici=users, native_lang=lists, lang_in_lists=lang_in_lists)

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

 