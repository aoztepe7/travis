import datetime

import mysql.connector
import database.db_connection

def getExistingShopProduct(start_date,finish_date):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        start_date_formatted = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
        finish_date_formatted = datetime.datetime.strptime(finish_date, "%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        formatted_finish_date = finish_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """SELECT * FROM shop_takip.shop_product where shop_id = 2 and product_id = 1 and finish_date > CAST(%s as datetime) and start_date < CAST(%s as datetime) and status = true"""
        query_tuple = (formatted_start_date,formatted_finish_date)
        cursor.execute(query, query_tuple)
        result = cursor.fetchall()
        if (result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        my_db.close()

def getExistingShopProductUpdate(start_date,finish_date,id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        start_date_formatted = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
        finish_date_formatted = datetime.datetime.strptime(finish_date, "%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        formatted_finish_date = finish_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """SELECT * FROM shop_takip.shop_product where shop_id = 2 and product_id = 1 and finish_date > CAST(%s as datetime) and start_date < CAST(%s as datetime) and status = true and id not = %s"""
        query_tuple = (formatted_start_date,formatted_finish_date,id)
        cursor.execute(query, query_tuple)
        result = cursor.fetchall()
        if (result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        my_db.close()

def getShopProductList():
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """select shop_product.id,shop_product.shop_id,shop_product.product_id,shop.name,product.name,shop_product.total_commission,
shop_product.guide_commission,shop_product.driver_commission,shop_product.company_commission_with_guide,shop_product.operator_commission,shop_product.hotel_rep_commission,shop_product.company_commission_with_hotel,DATE_FORMAT(start_date,'%d-%m-%Y'),DATE_FORMAT(finish_date,'%d-%m-%Y') from shop_takip.shop_product
inner join shop_takip.shop on shop_product.shop_id = shop.id
inner join shop_takip.product on shop_product.product_id = product.id where shop_product.status = true"""
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

def getById(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """select id,total_commission,guide_commission,driver_commission,company_commission_with_guide,operator_commission,hotel_rep_commission,company_commission_with_hotel from shop_product where shop_product.status = true and id =%s"""
        query_tuple = (int(id),)
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

def deleteShopProduct(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """UPDATE shop_product set status = null where id = %s"""
        query_tuple = (id,)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def addShopProduct(ShopProduct):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        start_date_formatted = datetime.datetime.strptime(ShopProduct.startDate,"%d-%m-%Y %H:%M:%S")
        finish_date_formatted = datetime.datetime.strptime(ShopProduct.finishDate,"%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        formatted_finish_date = finish_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """INSERT INTO shop_product(shop_id,product_id,total_commission,guide_commission,driver_commission,company_commission_with_guide,operator_commission,status,hotel_rep_commission,company_commission_with_hotel,start_date,finish_date)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        query_tuple= (ShopProduct.shopId,ShopProduct.productId,ShopProduct.totalCommission,ShopProduct.guideCommission,ShopProduct.driverCommission,ShopProduct.companyCommissionWithGuide,ShopProduct.operatorCommission,int(ShopProduct.status),ShopProduct.hotelRepCommission,ShopProduct.companyCommissionWithHotel,formatted_start_date,formatted_finish_date)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def updateShopProduct(ShopProduct):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        start_date_formatted = datetime.datetime.strptime(ShopProduct.startDate, "%d-%m-%Y %H:%M:%S")
        finish_date_formatted = datetime.datetime.strptime(ShopProduct.finishDate, "%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        formatted_finish_date = finish_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """UPDATE shop_product set shop_id = %s,product_id = %s,total_commission = %s, guide_commission = %s , driver_commission = %s , company_commission_with_guide = %s , operator_commission = %s , hotel_rep_commission = %s , company_commission_with_hotel = %s , start_date = %s , finish_date = %s WHERE id=%s"""
        query_tuple= (ShopProduct.shopId,ShopProduct.productId,ShopProduct.totalCommission,ShopProduct.guideCommission,ShopProduct.driverCommission,ShopProduct.companyCommissionWithGuide,ShopProduct.operatorCommission,ShopProduct.hotelRepCommission,ShopProduct.companyCommissionWithHotel,formatted_start_date,formatted_finish_date,int(ShopProduct.id))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def getShopProductsByShopIdAndDate(id,date):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        cursor = my_db.cursor(buffered=True)
        date = date + " 01:00:00"
        start_date_formatted = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """select shop_product.id,shop_product.product_id,product.name,shop_product.total_commission,
        shop_product.guide_commission,shop_product.driver_commission,shop_product.company_commission_with_guide,shop_product.operator_commission,shop_product.hotel_rep_commission,shop_product.company_commission_with_hotel from shop_takip.shop_product
        inner join shop_takip.shop on shop_product.shop_id = shop.id
        inner join shop_takip.product on shop_product.product_id = product.id where shop_product.status = true and start_date <= CAST(%s as datetime) and finish_date >= CAST(%s as datetime) and shop_product.shop_id = %s"""
        query_tuple = (formatted_start_date,formatted_start_date,id)
        cursor.execute(query, query_tuple)
        result = cursor.fetchall()
        if (result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        my_db.close()