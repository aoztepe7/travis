import mysql.connector
import database.db_connection

def user_login(username,password):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        cursor.execute("Select * from user where username ='"+username+"' and password = '"+password+"' and status = true")
        result = cursor.fetchall()
        if(result):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()


def getDB():
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        return my_db
    except Exception as e:
        print(e)
        return False


