import sqlite3
import json

conn = sqlite3.connect("settings.db")
cursor = conn.cursor()

Alerts = {}

from enum import Enum
class Character(Enum):
    OwnCurrency = "OwnCurrency"
    CountOfAlerts = "CountOfAlerts"
    Status = "Status"
    all = "*"

class Status(Enum):
    NotRegistered = "NotRegistered"
    Default = "Default"
    VIP = "VIP"

def post_sql_query(sql_query):
    with sqlite3.connect('settings.db') as connection:
        cursor = connection.cursor()
        #try:
        cursor.execute(sql_query)
        #except:
        #    print('except')
        #    pass
        result = cursor.fetchall()
        return result

# Создание таблицы
def createBase():
    base_query = """CREATE TABLE IF NOT EXISTS settings (
                   user_id INTEGER PRIMARY KEY NOT NULL, 
                   OwnCurrency TEXT,
                   CountOfAlerts INTEGER,
                   Status TEXT);
                   """
    post_sql_query(base_query)

createBase()

def Register(user_id, OwnCurrency, CountOfAlert, Status):
    user_query = f'Select * FROM settings WHERE user_id = {user_id}'
    user_data = post_sql_query(user_query)
    if not user_data:
        insert_data = f"INSERT INTO settings VALUES({user_id}, '{OwnCurrency}', {CountOfAlert}, '{Status}');"
        post_sql_query(insert_data)

def Update(user_id, Character, Value):
    insert_query = f"UPDATE settings SET {Character} = '{Value}' WHERE user_id = {user_id}"
    post_sql_query(insert_query)


def Delete(user_id):
    delete_query = "DELETE FROM settings WHERE user_id = ?", (user_id,)
    post_sql_query(delete_query)


def GetFromBase(user_id, Character):
    sql_select_query = f"select {Character} from settings where user_id = {user_id}"
    records = post_sql_query(sql_select_query)
    return records[0][0]

def saveArray(filename, dict):
    with open(filename, 'w') as f:
        json.dump(dict, f)

def loadArray(filename):
    with open(filename, 'r') as f:
        return json.load(f)


