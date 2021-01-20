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
    
    sql = "SELECT * FROM user ORDER BY user_id ASC"
    cursor.execute(sql)
    users = cursor.fetchall()
    """
    sql2 = "SELECT * FROM list ORDER BY list_id ASC"
    cursor.execute(sql2)
    lists = cursor.fetchall()
    """
    sql3 = "SELECT * FROM language_in_lists ORDER BY id ASC"
    cursor.execute(sql3)
    lang_in_lists = cursor.fetchall()

    sql4 = "SELECT * FROM language_names ORDER BY language_id ASC"
    cursor.execute(sql4)
    lang_names = cursor.fetchall()
    return render_template("home_page.html", day = this_day, kullanici=users, lang_in_lists=lang_in_lists, lang_names=lang_names)

def profile_page():
    sql = "SELECT * FROM user ORDER BY user_id ASC"
    cursor.execute(sql)
    users = cursor.fetchall()
    """
    sql2 = "SELECT * FROM list ORDER BY list_id ASC"
    cursor.execute(sql2)
    lists = cursor.fetchall()
    """
    sql3 = "SELECT * FROM language_in_lists ORDER BY id ASC"
    cursor.execute(sql3)
    lang_in_lists = cursor.fetchall()

    sql4 = "SELECT * FROM language_names ORDER BY language_id ASC"
    cursor.execute(sql4)
    lang_names = cursor.fetchall()
    return render_template("movie.html", kullanici=users, lang_in_lists=lang_in_lists, lang_names=lang_names)

def add_language():
    sql = "SELECT * FROM language_names ORDER BY language_id ASC"
    cursor.execute(sql)
    lang_names = cursor.fetchall()

    error = ''
    if request.method == 'POST':
        if request.form['label_id'] == '':
            error = 'Please choose learning or speaking'
        elif request.form['languages'] == '':
            error = 'Please choose a language'
        else:
            sql = "INSERT INTO language_in_lists SET user_id = %s, language_id = %s, label = %s"
            cursor.execute(sql, (session['user_id'], request.form['languages'], request.form['label_id'],))
            mydb.commit()
            if cursor.rowcount:
                return redirect(url_for('profile_page'))
            else:
                error = 'error'
    return render_template("add_language.html", lang_names=lang_names, error=error)#, movies=sorted(movies)

def delete_language():
    sql = "SELECT * FROM user ORDER BY user_id ASC"
    cursor.execute(sql)
    users = cursor.fetchall()
    """
    sql2 = "SELECT * FROM list ORDER BY list_id ASC"
    cursor.execute(sql2)
    lists = cursor.fetchall()
    """
    sql3 = "SELECT * FROM language_in_lists ORDER BY id ASC"
    cursor.execute(sql3)
    lang_in_lists = cursor.fetchall()

    sql4 = "SELECT * FROM language_names ORDER BY language_id ASC"
    cursor.execute(sql4)
    lang_names = cursor.fetchall()

    if request.method == 'POST':
        sql = "DELETE FROM language_in_lists WHERE user_id = %s, language_id = %s"
        cursor.execute(sql, (session['user_id'], request.form.get('language1')))
        mydb.commit()
        return redirect(url_for('profile_page'))

    return render_template("delete_language.html", kullanici=users, lang_in_lists=lang_in_lists, lang_names=lang_names)

def register_page():
    error = ''
    if request.method == 'POST':
        if request.form['user_name'] == '':
            error = 'please enter user name'
        elif request.form['email'] == '':
            error = 'please enter e-mail'
        elif request.form['password'] == '' or request.form['re_password'] == '':
            error = 'please enter password'
        elif request.form['password'] != request.form['re_password']:
            error = 'Passwords not matched'
        else: 
            sql = "INSERT INTO user SET user_name = %s, mail = %s, password = %s"
            cursor.execute(sql, (request.form['user_name'], request.form['email'], request.form['password']))
            mydb.commit()
            if cursor.rowcount:
                session['user_id'] = cursor.lastrowid
                return redirect(url_for('welcome_page'))
            else:
                error = 'account could not been created because of an error'
    return render_template("register.html", error=error)

def logout_page():
    session.clear()
    return redirect(url_for('login_page'))

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

 