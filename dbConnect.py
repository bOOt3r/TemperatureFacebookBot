import mysql.connector
import response as r
import credentials as c


mydb = mysql.connector.connect(
    host=c.host,
    user=c.user,
    password=c.password,
    database=c.database
)


def save_user_to_db(user_id, user_first_name, user_last_name):
    try:
        cursor = mydb.cursor()
        cursor.callproc("insert_user_data", [user_id, user_first_name, user_last_name])
        mydb.commit()
        cursor.close()
        r.greet_new_user(user_id, user_first_name)
    except mysql.connector.Error as err:
        r.greet_known_user(user_id, user_first_name)


def save_temperature_to_db(temp):
    cursor = mydb.cursor()
    cursor.callproc("save_skrea_temperature", [temp])
    mydb.commit()
    cursor.close()
