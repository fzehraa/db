import mysql.connector
#from native_lang import Native_lang

class Database:
    def __init__(self):# constructor
        #self.lists = {} # dictionary
        #elf.tasks = {} # dictionary
        #self.users = {} # dictionary

        #self._last_list_key = 0
        #self.last_task_key = 0
        #self.last_user_key = 0
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password='',
            database="lang_exc"
        )