import mysql.connector
import database.db_connection

def getShopList():
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """SELECT shop.id,shop.area_id,shop.name,area.name,shop.commercial_name,shop.mail,shop.phone,shop.vip_commission,shop.landing_fee,
        shop.currency,shop.vip_commission_rep from shop join area on shop.area_id = area.id where shop.status = true"""
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


def getShopCommissionRates(id,):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """SELECT shop.id,shop.vip_commission,shop.landing_fee,
        shop.vip_commission_rep,shop.currency from shop where shop.status = true and shop.id = %s"""
        query_tuple = (id,)
        cursor.execute(query, query_tuple)
        result = cursor.fetchall()
        if(result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        my_db.close()

def deleteShop(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """UPDATE shop set status = null where id = %s"""
        query_tuple = (id,)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def addShop(Shop):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """INSERT INTO shop (name,area_id,commercial_name,mail,phone,vip_commission,landing_fee,currency,vip_commission_rep,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        query_tuple= (Shop.name,Shop.areaId,Shop.commercialName,Shop.mail,Shop.phone,Shop.vipCommission,Shop.landingFee,Shop.currency,Shop.vipCommissionRep,int(Shop.status))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def updateShop(Shop):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """UPDATE shop set name = %s,area_id = %s,commercial_name = %s, mail = %s, phone = %s, vip_commission = %s,landing_fee = %s, currency = %s, vip_commission_rep = %s WHERE id=%s"""
        query_tuple= (Shop.name,Shop.areaId,Shop.commercialName,Shop.mail,Shop.phone,Shop.vipCommission,Shop.landingFee,Shop.currency,Shop.vipCommissionRep,int(Shop.id))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()