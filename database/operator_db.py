import mysql.connector

def getOperatorList():
    my_db = None
    try:
        my_db = mysql.connector.connect(host="localhost", user="root", password="Revival2019", database="shop_takip")
        cursor = my_db.cursor()
        query = """SELECT id,name,chief_commission_amount from operator where status = true"""
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

def deleteOperator(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host="localhost", user="root", password="Revival2019", database="shop_takip")
        cursor = my_db.cursor()
        query = """UPDATE operator set status = null where id = %s"""
        query_tuple = (id,)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def addOperator(Operator):
    my_db = None
    try:
        my_db = mysql.connector.connect(host="localhost", user="root", password="Revival2019", database="shop_takip")
        cursor = my_db.cursor()
        query = """INSERT INTO operator (name,chief_commission_amount,status) VALUES (%s,%s,%s)"""
        query_tuple= (Operator.name,Operator.chiefCommissionAmount,int(Operator.status))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def updateOperator(Operator):
    my_db = None
    try:
        my_db = mysql.connector.connect(host="localhost", user="root", password="Revival2019", database="shop_takip")
        cursor = my_db.cursor()
        query = """UPDATE operator set name = %s,chief_commission_amount = %s WHERE id=%s"""
        query_tuple= (Operator.name,Operator.chiefCommissionAmount,int(Operator.id))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()