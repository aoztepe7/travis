import datetime

import mysql.connector
import database.db_connection


def getSearchQueryResultForShopReport(query):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = query
        cursor.execute(query)
        result = cursor.fetchall()
        if (result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        my_db.close()