from datetime import datetime
from flask import current_app, render_template, redirect, session, request, url_for
import mysql.connector
from flask_mysqldb import MySQL
import hashlib

#from forms import RegistrationForm, LoginForm

#current_app for, database is stored in the application’s configuration we need a way of accessing the application object from the view

#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  database="lang_exc"
)
cursor = mydb.cursor(dictionary=True)

def welcome_page():
    return render_template("welcome.html")

def home_page():
    bugun = datetime.today()
    this_day = bugun.strftime("%A")
    
    sql = "SELECT * FROM user ORDER BY user_id DESC"
    cursor.execute(sql)
    users = cursor.fetchall()
    
    sql2 = "SELECT * FROM list ORDER BY list_id DESC"
    cursor.execute(sql2)
    lists = cursor.fetchall()

    sql3 = "SELECT * FROM language_in_lists ORDER BY id DESC"
    cursor.execute(sql3)
    lang_in_lists = cursor.fetchall()

    sql4 = "SELECT * FROM language_names ORDER BY language_id DESC"
    cursor.execute(sql4)
    lang_names = cursor.fetchall()
    return render_template("home_page.html", day = this_day, kullanici=users, lists=lists, lang_in_lists=lang_in_lists, lang_names=lang_names)

def profile_page():
    return render_template("movie.html")#, movies=sorted(movies)

def register_page():
    return render_template("register.html")

def logout_page():
    session.clear()
    return redirect(url_for('welcome_page'))

def login_page():
    if 'user_id' in session:
        return redirect(url_for('home'))
    error = ''
    if request.method == 'POST':
        if request.form['email'] == '':
            error = 'Please enter e-mail'
        elif request.form['password'] == '':
            error = 'Please enter password'
        else:
            sql = "SELECT * FROM user WHERE mail = %s && password = %s"
            cursor.execute(sql, (request.form['email'], request.form['password']))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user['user_id']
                return redirect(url_for('home_page'))
            else:
                error = 'Girdiğiniz bilgilere ait kullanıcı bulunamadı.'




    return render_template("login.html", error=error)

 