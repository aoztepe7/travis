import mysql.connector
import database

def getProductList():
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """SELECT id,name from product where status = true"""
        cursor.execute(query)
        result = cursor.fetchall()
        if(result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        my_db.close()

def deleteProduct(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """UPDATE product set status = null where id = %s"""
        query_tuple = (id,)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def addProduct(Product):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """INSERT INTO product (name,status) VALUES (%s,%s)"""
        query_tuple= (Product.name,int(Product.status))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def updateProduct(Product):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """UPDATE product set name = %s WHERE id=%s"""
        query_tuple= (Product.name,int(Product.id))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()