import datetime

import mysql.connector
import database.db_connection


def getSearchQueryResult(query):
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

def fillBoxesWithValues(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """select shop_sale.id,shop_sale.guide_id,shop_sale.tour_name,shop_sale.tour_type,shop_sale.hotel,
        shop_sale.note, shop_sale.operator_id, shop_sale.shop_id, shop_sale.shop_product_id,
        shop_sale.total_pax, shop_sale.total_sale,shop_sale.money_on_guide, shop_sale.money_received, shop_sale.is_forwarded_sale, DATE_FORMAT(shop_sale.sale_date,'%d-%m-%Y'),
        DATE_FORMAT(shop_sale.forward_date,'%d-%m-%Y'), shop_sale.shop_currency, shop_sale.rate,
        shop_sale.add_vip,shop_sale.add_landing,shop_sale.add_chief ,shop_sale.product_name , shop_sale.guide_selection ,
        guide.full_name,operator.name ,shop.name , shop_sale.guide_comm_rate , shop_sale.driver_comm_rate , shop_sale.operator_comm_rate,
        shop_sale.hotel_rep_comm_rate,shop_sale.total_comm_rate,shop_sale.comp_rate_guide,shop_sale.comp_rate_hotel
        from shop_takip.shop_sale inner join shop_takip.shop on shop_sale.shop_id = shop.id
        inner join shop_takip.operator on shop_sale.operator_id = operator.id
        inner join shop_takip.guide on shop_sale.guide_id = guide.id where shop_sale.status = true and shop_sale.id = %s"""
        query_tuple = (int(id),)
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

def getById(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),
                                        username=database.db_connection.getUser(),
                                        password=database.db_connection.getPassword(),
                                        database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """select shop_sale.id,shop_sale.guide_id,shop_sale.tour_name,shop_sale.tour_type,shop_sale.hotel,
        shop_sale.note, shop_sale.operator_id, shop_sale.shop_id, shop_sale.shop_product_id,
        shop_sale.total_pax, shop_sale.total_sale, shop_sale.total_commission_amount,
        shop_sale.guide_commission_amount, shop_sale.operator_commission_amount, shop_sale.driver_commission_amount,
        shop_sale.chief_commission_amount, shop_sale.total_landing_fee_amount,
        shop_sale.total_vip_commission_amount,shop_sale.money_on_guide, shop_sale.money_received, shop_sale.is_forwarded_sale, DATE_FORMAT(shop_sale.sale_date,'%d-%m-%Y'),
        DATE_FORMAT(shop_sale.forward_date,'%d-%m-%Y'), shop_sale.shop_currency, shop_sale.convert_currency, shop_sale.rate,
        shop_sale.converted_total_sale, shop_sale.converted_total_commission_amount, shop_sale.converted_guide_commission_amount,
        shop_sale.converted_operator_commission_amount, shop_sale.converted_driver_commission_amount, shop_sale.converted_chief_commission_amount,
        shop_sale.converted_total_landing_fee_amount, shop_sale.converted_total_vip_commission_amount,
        shop_sale.total_company_income, shop_sale.converted_company_income,shop_sale.add_vip,shop_sale.add_landing,shop_sale.add_chief ,shop_sale.product_name , shop_sale.guide_selection ,
        shop_sale.vip_commission_amount_rep , shop_sale.converted_vip_commission_amount_rep , guide.full_name,operator.name ,shop.name , total_comp_receive, converted_total_comp_receive
        from shop_takip.shop_sale inner join shop_takip.shop on shop_sale.shop_id = shop.id
        inner join shop_takip.operator on shop_sale.operator_id = operator.id
        inner join shop_takip.guide on shop_sale.guide_id = guide.id where shop_sale.status = true and shop_sale.id = %s"""
        query_tuple = (int(id),)
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

def getShopSaleList():
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()

        query = """SELECT shop_sale.id,DATE_FORMAT(shop_sale.sale_date,'%d-%m-%Y'),shop_sale.guide_id,guide.full_name,shop_sale.tour_type,shop_sale.shop_id,shop.name,shop_sale.shop_product_id,shop_product.product_id,product.name,shop_sale.total_sale,shop_sale.shop_currency 
        from shop_sale inner join guide on shop_sale.guide_id = guide.id 
        inner join shop on shop_sale.shop_id = shop.id
        inner join shop_product on shop_sale.shop_product_id = shop_product.id
        inner join product on shop_product.product_id = product.id where shop_sale.status = true"""
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


def getShortList():
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()

        query = """SELECT shop_sale.id,DATE_FORMAT(shop_sale.sale_date,'%d-%m-%Y'),guide.full_name,shop.name
        from shop_sale inner join guide on shop_sale.guide_id = guide.id 
        inner join shop on shop_sale.shop_id = shop.id where shop_sale.status = true"""
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

def deleteShopSale(id):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        query = """UPDATE shop_sale set status = null where id = %s"""
        query_tuple = (id,)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def addShopSale(ShopSale):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        sale_date_formatted = datetime.datetime.strptime(ShopSale.saleDate, "%d-%m-%Y %H:%M:%S")
        forward_date_formatted = datetime.datetime.strptime(ShopSale.forwardDate, "%d-%m-%Y %H:%M:%S")
        ShopSale.saleDate = sale_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        ShopSale.forwardDate = forward_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """INSERT INTO shop_sale (guide_id,tour_name,tour_type,hotel,note,operator_id,shop_id,shop_product_id,total_pax,total_sale,total_commission_amount,guide_commission_amount,
        operator_commission_amount,driver_commission_amount,chief_commission_amount,total_landing_fee_amount,total_vip_commission_amount,money_on_guide,money_received,is_forwarded_sale,
        sale_date,forward_date,shop_currency,convert_currency,rate,converted_total_sale,converted_total_commission_amount,converted_guide_commission_amount,converted_operator_commission_amount,
        converted_driver_commission_amount,converted_chief_commission_amount,converted_total_landing_fee_amount,converted_total_vip_commission_amount,
        total_company_income,converted_company_income,status,add_vip,add_landing,add_chief,product_name,guide_selection,vip_commission_amount_rep,
        converted_vip_commission_amount_rep,total_comp_receive,converted_total_comp_receive) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        query_tuple= (ShopSale.guideId,ShopSale.tourName,ShopSale.tourType,ShopSale.hotel,ShopSale.note,ShopSale.operatorId,ShopSale.shopId,ShopSale.shopProductId,ShopSale.totalPax,
                      ShopSale.totalSale,ShopSale.totalCommissionAmount,ShopSale.guideCommissionAmount,ShopSale.operatorCommissionAmount,ShopSale.driverCommissionAmount,ShopSale.chiefCommissionAmount,
                      ShopSale.totalLandingFeeAmount,ShopSale.totalVipCommissionAmount,ShopSale.moneyOnGuide,ShopSale.moneyReceived,ShopSale.isForwardedSale,ShopSale.saleDate,ShopSale.forwardDate,
                      ShopSale.shopCurrency,ShopSale.convertCurrency,ShopSale.rate,ShopSale.convertedTotalSale,ShopSale.convertedTotalCommissionAmount,ShopSale.convertedGuideCommissionAmount,
                      ShopSale.convertedOperatorCommissionAmount,ShopSale.convertedDriverCommissionAmount,ShopSale.convertedChiefCommissionAmount,ShopSale.convertedTotalLandingFeeAmount,
                      ShopSale.convertedTotalVipCommissionAmount,ShopSale.totalCompanyIncome,ShopSale.convertedCompanyIncome,int(ShopSale.status),ShopSale.addVip,ShopSale.addLanding,ShopSale.addChief,
                      ShopSale.productName,ShopSale.guideSelection,ShopSale.vipCommissionAmountRep,ShopSale.convertedVipCommissionAmountRep,ShopSale.totalCompReceive,ShopSale.convertedTotalCompReceive)
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()

def updateShopSale(ShopSale):
    my_db = None
    try:
        my_db = mysql.connector.connect(host=database.db_connection.getHost(),username = database.db_connection.getUser(),password = database.db_connection.getPassword(),database=database.db_connection.getDatabase())
        cursor = my_db.cursor()
        sale_date_formatted = datetime.datetime.strptime(ShopSale.saleDate, "%d-%m-%Y %H:%M:%S")
        forward_date_formatted = datetime.datetime.strptime(ShopSale.forwardDate, "%d-%m-%Y %H:%M:%S")
        ShopSale.saleDate = sale_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        ShopSale.forwardDate = forward_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        query = """UPDATE shop_sale set guide_id = %s,tour_name= %s,tour_type= %s,hotel= %s,note= %s,operator_id= %s,shop_id= %s,shop_product_id= %s,total_pax= %s,total_sale= %s,total_commission_amount= %s,guide_commission_amount= %s,
        operator_commission_amount= %s,driver_commission_amount= %s,chief_commission_amount= %s,total_landing_fee_amount= %s,total_vip_commission_amount= %s,money_on_guide= %s,money_received= %s,is_forwarded_sale= %s,
        sale_date= %s,forward_date= %s,shop_currency= %s,convert_currency = %s,rate= %s,converted_total_sale= %s,converted_total_commission_amount= %s,converted_guide_commission_amount= %s,converted_operator_commission_amount= %s,
        converted_driver_commission_amount= %s,converted_chief_commission_amount= %s,converted_total_landing_fee_amount= %s,converted_total_vip_commission_amount= %s,
        total_company_income= %s,converted_company_income= %s,add_vip= %s,add_landing= %s,add_chief= %s,product_name= %s,guide_selection= %s,vip_commission_amount_rep= %s,
        converted_vip_commission_amount_rep= %s ,total_comp_receive = %s, converted_total_comp_receive = %s WHERE id=%s"""
        query_tuple= (ShopSale.guideId,ShopSale.tourName,ShopSale.tourType,ShopSale.hotel,ShopSale.note,ShopSale.operatorId,ShopSale.shopId,ShopSale.shopProductId,ShopSale.totalPax,
                      ShopSale.totalSale,ShopSale.totalCommissionAmount,ShopSale.guideCommissionAmount,ShopSale.operatorCommissionAmount,ShopSale.driverCommissionAmount,ShopSale.chiefCommissionAmount,
                      ShopSale.totalLandingFeeAmount,ShopSale.totalVipCommissionAmount,ShopSale.moneyOnGuide,ShopSale.moneyReceived,ShopSale.isForwardedSale,ShopSale.saleDate,ShopSale.forwardDate,
                      ShopSale.shopCurrency,ShopSale.convertCurrency,ShopSale.rate,ShopSale.convertedTotalSale,ShopSale.convertedTotalCommissionAmount,ShopSale.convertedGuideCommissionAmount,
                      ShopSale.convertedOperatorCommissionAmount,ShopSale.convertedDriverCommissionAmount,ShopSale.convertedChiefCommissionAmount,ShopSale.convertedTotalLandingFeeAmount,
                      ShopSale.convertedTotalVipCommissionAmount,ShopSale.totalCompanyIncome,ShopSale.convertedCompanyIncome,ShopSale.addVip,ShopSale.addLanding,ShopSale.addChief,
                      ShopSale.productName,ShopSale.guideSelection,ShopSale.vipCommissionAmountRep,ShopSale.convertedVipCommissionAmountRep,ShopSale.totalCompReceive,ShopSale.convertedTotalCompReceive,int(ShopSale.id))
        cursor.execute(query,query_tuple)
        my_db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        my_db.close()