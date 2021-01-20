from flask import Flask
#from forms import RegistrationForm, LoginForm



import views
from database import Database
from native_lang import Native_lang




def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '5ab6aee66997a5901a7a7d386d8591ce' #secret key

    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.welcome_page)

    app.add_url_rule("/home", view_func=views.home_page)

    app.add_url_rule("/profile", view_func=views.profile_page)

    app.add_url_rule("/addlanguage", view_func=views.add_language, methods=["GET","POST"])

    app.add_url_rule("/deletelanguage", view_func=views.delete_language, methods=["GET","POST"])

    app.add_url_rule("/register", view_func=views.register_page, methods=["GET","POST"])

    app.add_url_rule("/login", view_func=views.login_page, methods=['POST', 'GET'])

    app.add_url_rule("/logout", view_func=views.logout_page)


    #db = Database()    
    #app.config["db"] = db #adding new data to database, we store the database object in the configuration to make it accessible to all components in the application
    
    return app




if __name__ == "__main__":#if this file runs as a script do the following
    app = create_app()
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(host="127.0.0.1", port=8080)
