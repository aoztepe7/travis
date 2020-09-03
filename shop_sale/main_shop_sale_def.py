import sys
# GUI FILE
from PyQt5 import QtCore, QtSql, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import shop_sale.ui_shop_sale_entry
import shop_sale.main_shop_sale
import database.shop_sale_db
import database.shop_db
import database.shop_product_db
import database.operator_db
import database.guide_db
import database.product_db
import pyautogui
import shop_sale.obj_shop_sale
import shop_product.obj_shop_product
import utils.helper
import datetime
import easygui

GLOBAL_STATE = 0
GLOBAL_UPDATE = 0
GLOBAL_SELECTED_SHOP_PRODUCT = shop_product.obj_shop_product.ShopProductView(None,None,None,None,None,None,None,None,None,None)
GLOBAL_CHIEF_COMMISSION = 0

GLOBAL_VIP_COMPANY = 0
GLOBAL_VIP_REP = 0
GLOBAL_LANDING_FEE = 0
GLOBAL_SHOP_CURRENCY = None
GLOBAL_SELECTED_GUIDE = 0
GLOBAL_INTERNAL_RATE = None
GLOBAL_IS_CALCULATED = False

GLOBAL_SELECTED_SHOP_PAYMENT_TYPE = 0

class ShopSaleDefWindow(QMainWindow):
    def changeGuideEvent(self):
        if(self.ui.cmb_guide.currentIndex() != -1):
            self.ui.cmb_shop.setEnabled(True)
            self.ui.dtp_sale.setEnabled(True)

    def fillShopProducts(self,date):
        self.ui.cmb_product.clear()
        global GLOBAL_SELECTED_SHOP_PAYMENT_TYPE
        GLOBAL_SELECTED_SHOP_PAYMENT_TYPE = self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 2))
        if(self.ui.cmb_shop.currentIndex() != -1):
            product_list = database.shop_product_db.getShopProductsByShopIdAndDate(self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0)),self.ui.dtp_sale.date().toString("dd-MM-yyyy"))
            if (product_list):
                for i in product_list:
                    global GLOBAL_SELECTED_SHOP_PRODUCT
                    GLOBAL_SELECTED_SHOP_PRODUCT = shop_product.obj_shop_product.ShopProductView(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])

                    it5 = QtGui.QStandardItem(str(i[0]))
                    it6 = QtGui.QStandardItem(str(i[2]))
                    self.product_model.appendRow((it5, it6))

            self.ui.cmb_product.setModel(self.product_model)
            self.ui.cmb_product.setModelColumn(1)
            self.ui.cmb_product.setCurrentIndex(0)

            self.ui.cmb_product.setEnabled(True)



    def fillSelectedShopProductCommissions(self):
        if(self.ui.cmb_product.currentIndex() != -1):
            result = database.shop_product_db.getById(self.product_model.data(self.product_model.index(self.ui.cmb_product.currentIndex(), 0)))
            if(result and len(result)>0):
                for i in result:
                    self.ui.txt_def_guide_rate.setText(str(i[2]))
                    self.ui.txt_def_driver_rate.setText(str(i[3]))
                    self.ui.txt_def_opr_rate.setText(str(i[5]))
                    self.ui.txt_def_reo_rate.setText(str(i[6]))
                    self.ui.txt_def_guide_rate_2.setText(str(i[1]))
                    self.ui.txt_def_guide_rate_3.setText(str(i[4]))
                    self.ui.txt_def_guide_rate_4.setText(str(i[7]))
        else:
            self.ui.txt_def_guide_rate.clear()
            self.ui.txt_def_driver_rate.clear()
            self.ui.txt_def_opr_rate.clear()
            self.ui.txt_def_reo_rate.clear()
            self.ui.txt_def_guide_rate_2.clear()
            self.ui.txt_def_guide_rate_3.clear()
            self.ui.txt_def_guide_rate_4.clear()

    def setGuideType(self):
        if(self.ui.cmb_guide.currentIndex() != -1):
            global GLOBAL_SELECTED_GUIDE
            if (self.guide_model.data(self.guide_model.index(self.ui.cmb_guide.currentIndex(), 2)) == "OTEL REHBERİ"):
                GLOBAL_SELECTED_GUIDE = 1
            else:
                GLOBAL_SELECTED_GUIDE = 0



    def calculate(self):
        if(self.checkNessessarySelections() == False):
            pyautogui.alert("Rehber-Mağaza ve Ürün Seçimi Boş Olamaz!")
            return

        self.getShopCommissionRates(self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0)))
        self.setChiefCommission(self.operator_model.data(self.operator_model.index(self.ui.cmb_operator.currentIndex(), 0)))

        #Guide Calculations
        guideDict = self.calculateGuideCommissionAmounts()
        self.ui.txt_calc_org_guide.setText(str(guideDict["originalGuideComm"]))
        self.ui.txt_calc_eur_guide.setText(str(guideDict["convertedGuideComm"]))

        # Driver Calculations
        driverDict = self.calculateDriverCommissionAmounts()
        self.ui.txt_calc_org_driver.setText(str(driverDict["originalDriverComm"]))
        self.ui.txt_calc_eur_driver.setText(str(driverDict["convertedDriverComm"]))

        # Operator Calculations
        operatorDict = self.calculateOperatorCommissionAmounts()
        self.ui.txt_calc_org_operator.setText(str(operatorDict["originalOperatorComm"]))
        self.ui.txt_calc_eur_operator.setText(str(operatorDict["convertedOperatorComm"]))

        # Chief Calculations
        chiefDict = self.calculateChiefRepCommissionAmounts()
        chiefCommAmount = chiefDict["originalChiefComm"]
        self.ui.txt_calc_org_chief.setText(str(chiefDict["originalChiefComm"]))
        self.ui.txt_calc_eur_chief.setText(str(chiefDict["convertedChiefComm"]))

        # Landing Fee Calculations
        landingDict = self.calculateLandingFeeAmounts()
        self.ui.txt_calc_org_landing.setText(str(landingDict["originalLandingFeeAmount"]))
        self.ui.txt_calc_eur_landing.setText(str(landingDict["convertedLandingFeeAmount"]))

        # Vip Rep Calculations
        vipDict = self.calculateVipCommissionAmounts()
        self.ui.txt_calc_org_vip_rep.setText(str(vipDict["originalVipRep"]))
        self.ui.txt_calc_eur_vip_rep.setText(str(vipDict["convertedVipRep"]))

        # Vip Company Calculations
        self.ui.txt_calc_org_vip_comp.setText(str(vipDict["originalVipCompany"]))
        self.ui.txt_calc_eur_vip_comp.setText(str(vipDict["convertedVipCompany"]))

        # Total Commission Calculations
        totalComDict = self.calculateTotalCommissionAmount()
        self.ui.txt_calc_org_comp.setText(str(totalComDict["originalTotalCommission"]))
        self.ui.txt_calc_eur_comp.setText(str(totalComDict["convertedTotalCommission"]))

        # Company Income Calculations
        companyIncomeDict = self.calculateCompanyIncome(chiefCommAmount,GLOBAL_SELECTED_GUIDE)
        self.ui.txt_calc_org_total.setText(str(companyIncomeDict["originalCompanyIncome"]))
        self.ui.txt_calc_eur_total.setText(str(companyIncomeDict["convertedCompanyIncome"]))

        # Company Receive Calculations
        companyReceiveDict = self.calculateMustReceive(GLOBAL_SELECTED_GUIDE)
        self.ui.txt_calc_org_comp_receive.setText(str(companyReceiveDict["totalOrginalReceive"]))
        self.ui.txt_calc_eur_comp_receive.setText(str(companyReceiveDict["totalConvertedReceive"]))

        global GLOBAL_IS_CALCULATED
        GLOBAL_IS_CALCULATED = True

        pyautogui.alert("Hesaplama Tamamlandı!")

    def calculateMustReceive(self,guideSelection):
        totalOrginalReceive = 0
        totalConvertedReceive = 0
        rate = float(self.ui.txt_rate.text())
        if(GLOBAL_SELECTED_SHOP_PAYMENT_TYPE == 0):
            totalOrginalReceive = (float(self.ui.txt_calc_org_guide.text()) + float(self.ui.txt_calc_org_driver.text())+ float(self.ui.txt_calc_org_operator.text()) + float(self.ui.txt_calc_org_chief.text()) + float(self.ui.txt_calc_org_landing.text())+ float(self.ui.txt_calc_org_vip_rep.text()) + float(self.ui.txt_calc_org_vip_comp.text()) + float(self.ui.txt_calc_org_total.text()))
            totalConvertedReceive = totalOrginalReceive * rate
        else:
            totalOrginalReceive = (float(self.ui.txt_calc_org_driver.text())+ float(self.ui.txt_calc_org_operator.text()) + float(self.ui.txt_calc_org_chief.text()) + float(self.ui.txt_calc_org_landing.text())+ float(self.ui.txt_calc_org_vip_rep.text()) + float(self.ui.txt_calc_org_vip_comp.text())+float(self.ui.txt_calc_org_total.text()))
            totalConvertedReceive = totalOrginalReceive * rate

        totalCompanyReceiveDict = {"totalOrginalReceive": "{:.2f}".format(float(totalOrginalReceive)),
                                      "totalConvertedReceive": "{:.2f}".format(
                                          float(totalConvertedReceive))}
        return totalCompanyReceiveDict


    def calculateCompanyIncome(self,chiefCommissionAmount,guideSelection):
        companyCommissionRate = float(0)
        rate = float(self.ui.txt_rate.text())
        if(guideSelection == 0):
            companyCommissionRate = float(self.ui.txt_def_guide_rate_3.text())
        else:
            companyCommissionRate = float(self.ui.txt_def_guide_rate_4.text())

        totalSale = float(self.ui.txt_total_sale.text())

        companyCommissionAmount = (((totalSale * companyCommissionRate) / 100 ) - float(chiefCommissionAmount)) + float(self.ui.txt_calc_org_vip_comp.text()) + float(self.ui.txt_calc_org_landing.text())
        convertedCompanyCommissionAmount = companyCommissionAmount * rate

        totalCompanyIncomeDict = {"originalCompanyIncome":"{:.2f}".format(float(companyCommissionAmount)) ,"convertedCompanyIncome": "{:.2f}".format(float(convertedCompanyCommissionAmount))}
        return totalCompanyIncomeDict


    def calculateTotalCommissionAmount(self):
        totalSale = float(self.ui.txt_total_sale.text())
        totalCommissionRate = float(self.ui.txt_def_guide_rate_2.text())
        rate =  float(self.ui.txt_rate.text())
        originalTotalCommission = ((totalSale * totalCommissionRate) /100) + float(self.ui.txt_calc_org_vip_comp.text()) + float(self.ui.txt_calc_org_vip_rep.text()) + float(self.ui.txt_calc_org_landing.text())
        convertedTotalCommission = originalTotalCommission * rate

        totalCommDict = {"originalTotalCommission" : "{:.2f}".format(float(originalTotalCommission)),"convertedTotalCommission": "{:.2f}".format(float(convertedTotalCommission))}
        return totalCommDict

    def calculateGuideCommissionAmounts(self):
        totalSale = float(self.ui.txt_total_sale.text())
        guideCommissionRate = 0
        if (GLOBAL_SELECTED_GUIDE == 0):
            guideCommissionRate = float(self.ui.txt_def_guide_rate.text())
        else:
            guideCommissionRate = float(self.ui.txt_def_reo_rate.text())

        rate = float(self.ui.txt_rate.text())

        originalGuideComm = (totalSale * guideCommissionRate) / 100
        convertedGuideComm = originalGuideComm * rate
        guideDict = {"originalGuideComm":"{:.2f}".format(float(originalGuideComm)),"convertedGuideComm":"{:.2f}".format(float(convertedGuideComm))}
        return guideDict

    def calculateDriverCommissionAmounts(self):
        totalSale = float(self.ui.txt_total_sale.text())
        driverCommissionRate = float(self.ui.txt_def_driver_rate.text())
        rate = float(self.ui.txt_rate.text())

        originalDriverComm = (totalSale * driverCommissionRate) / 100
        convertedDriverComm = originalDriverComm * rate
        driverDict = {"originalDriverComm":"{:.2f}".format(float(originalDriverComm)),"convertedDriverComm":"{:.2f}".format(float(convertedDriverComm))}
        return driverDict

    def calculateOperatorCommissionAmounts(self):
        totalSale = float(self.ui.txt_total_sale.text())
        operatorCommissionRate = float(self.ui.txt_def_opr_rate.text())
        rate = float(self.ui.txt_rate.text())

        originalOperatorComm = (totalSale * operatorCommissionRate) / 100
        convertedOperatorComm = originalOperatorComm * rate
        operatorDict = {"originalOperatorComm":"{:.2f}".format(float(originalOperatorComm)),"convertedOperatorComm":"{:.2f}".format(float(convertedOperatorComm))}
        return operatorDict

    def calculateChiefRepCommissionAmounts(self):
        if(self.ui.check_chief.isChecked()):
            totalSale = float(self.ui.txt_total_sale.text())
            chiefCommissionRate = float(GLOBAL_CHIEF_COMMISSION)
            rate = float(self.ui.txt_rate.text())

            originalChiefComm = (totalSale * chiefCommissionRate) / 100
            convertedChiefComm = originalChiefComm * rate
            chiefDict = {"originalChiefComm":"{:.2f}".format(float(originalChiefComm)),"convertedChiefComm":"{:.2f}".format(float(convertedChiefComm))}
            return chiefDict
        else:
            chiefDict = {"originalChiefComm": 0.0, "convertedChiefComm": 0.0}
            return chiefDict

    def calculateLandingFeeAmounts(self):
        landingFeeRate = 0
        originalCalculatedTotalLandingFee = 0
        convertedCalculatedTotalLandingFee = 0
        totalPax = int(self.ui.txt_pax.text())
        rate = float(self.ui.txt_rate.text())
        if(self.ui.check_landing.isChecked()):
            landingFeeRate = float(GLOBAL_LANDING_FEE)
            landingFeeCurrency = GLOBAL_SHOP_CURRENCY
            saleCurrency = self.ui.cmb_currency.currentText()
            if(landingFeeCurrency == saleCurrency):
                originalCalculatedTotalLandingFee = (totalPax * landingFeeRate)
                convertedCalculatedTotalLandingFee = originalCalculatedTotalLandingFee * rate
            else:
                global GLOBAL_INTERNAL_RATE
                if(GLOBAL_INTERNAL_RATE == None):
                    GLOBAL_INTERNAL_RATE = easygui.enterbox("Lütfen "+str(GLOBAL_SHOP_CURRENCY)+" - "+self.ui.cmb_currency.currentText()+" paritesini giriniz!")

                saleRateConvertedLanding = landingFeeRate * float(GLOBAL_INTERNAL_RATE)
                originalCalculatedTotalLandingFee = (totalPax * saleRateConvertedLanding)
                convertedCalculatedTotalLandingFee = originalCalculatedTotalLandingFee * rate

        landingDict = {"originalLandingFeeAmount":"{:.2f}".format(float(originalCalculatedTotalLandingFee)),"convertedLandingFeeAmount":"{:.2f}".format(float(convertedCalculatedTotalLandingFee))}
        return landingDict

    def calculateVipCommissionAmounts(self):
        originalCalculatedTotalVipRep = 0
        originalCalculatedTotalVipCompany = 0
        convertedCalculatedTotalVipRep = 0
        convertedCalculatedTotalVipCompany = 0
        rate = float(self.ui.txt_rate.text())
        if(self.ui.check_vip.isChecked()):
            vipCommCurrency = GLOBAL_SHOP_CURRENCY
            saleCurrency = self.ui.cmb_currency.currentText()
            if(vipCommCurrency == saleCurrency):
                originalCalculatedTotalVipRep = float(GLOBAL_VIP_REP)
                convertedCalculatedTotalVipRep = originalCalculatedTotalVipRep * rate

                originalCalculatedTotalVipCompany = float(GLOBAL_VIP_COMPANY)
                convertedCalculatedTotalVipCompany = originalCalculatedTotalVipCompany * rate
            else:
                global GLOBAL_INTERNAL_RATE
                if (GLOBAL_INTERNAL_RATE == None):
                    GLOBAL_INTERNAL_RATE = easygui.enterbox("Lütfen " + str(GLOBAL_SHOP_CURRENCY) + " - " + self.ui.cmb_currency.currentText() + " paritesini giriniz!")
                originalCalculatedTotalVipRep = float(GLOBAL_VIP_REP)
                originalCalculatedTotalVipCompany = float(GLOBAL_VIP_COMPANY)
                saleRateConvertedRepVipAmount = originalCalculatedTotalVipRep * float(GLOBAL_INTERNAL_RATE)
                saleRateConvertedCompanyVipAmount = originalCalculatedTotalVipCompany * float(GLOBAL_INTERNAL_RATE)

                originalCalculatedTotalVipRep = saleRateConvertedRepVipAmount
                convertedCalculatedTotalVipRep = originalCalculatedTotalVipRep * rate

                originalCalculatedTotalVipCompany = saleRateConvertedCompanyVipAmount
                convertedCalculatedTotalVipCompany = originalCalculatedTotalVipCompany * rate


        vipDict = {"originalVipRep":"{:.2f}".format(float(originalCalculatedTotalVipRep)),"convertedVipRep":"{:.2f}".format(float(convertedCalculatedTotalVipRep)),"originalVipCompany":"{:.2f}".format(float(originalCalculatedTotalVipCompany)),"convertedVipCompany":"{:.2f}".format(float(convertedCalculatedTotalVipCompany))}
        return vipDict



    def setChiefCommission(self,id):
        global GLOBAL_CHIEF_COMMISSION
        list = database.operator_db.getChiefCommission(id)[0]
        for i in list:
            GLOBAL_CHIEF_COMMISSION = float(i)

    def checkNessessarySelections(self):
        if (self.ui.cmb_guide.currentIndex() != -1 and self.ui.cmb_product.currentIndex() != -1 and self.ui.cmb_shop.currentIndex() != -1 and self.ui.cmb_currency.currentText() != -1):
            return True
        else:
            return False

    def getShopCommissionRates(self,id):
        shop_commissions = database.shop_db.getShopCommissionRates(id)
        global GLOBAL_VIP_REP
        global GLOBAL_LANDING_FEE
        global GLOBAL_VIP_COMPANY
        global GLOBAL_SHOP_CURRENCY

        for item in shop_commissions:
            GLOBAL_VIP_COMPANY = float(item[1])
            GLOBAL_LANDING_FEE = float(item[2])
            GLOBAL_VIP_REP = float(item[3])
            GLOBAL_SHOP_CURRENCY = str(item[4])

    def backToShopSalePanel(self):
        self.window = shop_sale.main_shop_sale.ShopSaleWindow()
        self.window.show()
        self.hide()

    def getShopList(self):
        return database.shop_db.getShopList()

    def getGuideList(self):
        return database.guide_db.getGuideList()

    def getOperatorList(self):
        return database.operator_db.getOperatorList()




    def saveToDb(self):
        if(GLOBAL_IS_CALCULATED == False):
            pyautogui.alert("Lütfen Önce Hesaplatma Yapınız!")
            return
        if(self.ui.check_forward.isChecked() == True and (self.ui.dtp_sale.date() > self.ui.dtp_forward.date()) == True):
            pyautogui.alert("Vade Tarihi , Satış Tarihinden Büyük Olamaz!")
            return
        else:

            if(shop_sale.main_shop_sale.GLOBAL_UPDATE == 1):
                ShopSale = shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE
                ShopSale.guideId = self.guide_model.data(self.guide_model.index(self.ui.cmb_guide.currentIndex(), 0))
                ShopSale.tourName = self.ui.txt_tour_name.text()
                ShopSale.tourType = self.ui.cmb_tour_type.currentText()
                ShopSale.hotel = self.ui.txt_hotel.text()
                ShopSale.note = self.ui.txt_note.toPlainText()
                ShopSale.operatorId = self.operator_model.data(self.operator_model.index(self.ui.cmb_operator.currentIndex(), 0))
                ShopSale.shopId = self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0))
                ShopSale.shopProductId = self.product_model.data(self.product_model.index(self.ui.cmb_product.currentIndex(), 0))
                ShopSale.totalPax = self.ui.txt_pax.text()
                ShopSale.totalSale = self.ui.txt_total_sale.text()
                ShopSale.totalCommissionAmount = self.ui.txt_calc_org_comp.text()
                ShopSale.guideCommissionAmount = self.ui.txt_calc_org_guide.text()
                ShopSale.operatorCommissionAmount = self.ui.txt_calc_org_operator.text()
                ShopSale.driverCommissionAmount = self.ui.txt_calc_org_driver.text()
                ShopSale.chiefCommissionAmount = self.ui.txt_calc_org_chief.text()
                ShopSale.totalLandingFeeAmount = self.ui.txt_calc_org_landing.text()
                ShopSale.totalVipCommissionAmount = self.ui.txt_calc_org_vip_comp.text()
                ShopSale.moneyOnGuide = self.ui.check_money_on_guide.isChecked()
                ShopSale.moneyReceived = self.ui.check_received.isChecked()
                ShopSale.isForwardedSale = self.ui.check_forward.isChecked()
                ShopSale.saleDate = self.ui.dtp_sale.date().toString("dd-MM-yyyy") + " 01:00:00"
                ShopSale.forwardDate = self.ui.dtp_forward.date().toString("dd-MM-yyyy") + " 01:00:00"
                ShopSale.shopCurrency = self.ui.cmb_currency.currentText()
                ShopSale.convertCurrency = "EUR"
                ShopSale.rate = self.ui.txt_rate.text()
                ShopSale.convertedTotalSale = str(float(self.ui.txt_total_sale.text()) * float(self.ui.txt_rate.text()))
                ShopSale.convertedTotalCommissionAmount = self.ui.txt_calc_eur_comp.text()
                ShopSale.convertedGuideCommissionAmount = self.ui.txt_calc_eur_guide.text()
                ShopSale.convertedOperatorCommissionAmount = self.ui.txt_calc_eur_operator.text()
                ShopSale.convertedDriverCommissionAmount = self.ui.txt_calc_eur_driver.text()
                ShopSale.convertedChiefCommissionAmount = self.ui.txt_calc_eur_chief.text()
                ShopSale.convertedTotalLandingFeeAmount = self.ui.txt_calc_eur_landing.text()
                ShopSale.convertedTotalVipCommissionAmount = self.ui.txt_calc_eur_vip_comp.text()
                ShopSale.totalCompanyIncome = self.ui.txt_calc_org_total.text()
                ShopSale.convertedCompanyIncome = self.ui.txt_calc_eur_total.text()
                ShopSale.addVip = self.ui.check_vip.isChecked()
                ShopSale.addLanding = self.ui.check_landing.isChecked()
                ShopSale.addChief = self.ui.check_landing.isChecked()
                ShopSale.productName = self.ui.cmb_product.currentText()
                ShopSale.guideSelection =GLOBAL_SELECTED_GUIDE
                ShopSale.vipCommissionAmountRep = self.ui.txt_calc_org_vip_rep.text()
                ShopSale.convertedVipCommissionAmountRep = self.ui.txt_calc_eur_vip_rep.text()
                ShopSale.shopName = self.ui.cmb_shop.currentText()
                ShopSale.totalCompReceive = self.ui.txt_calc_org_comp_receive.text()
                ShopSale.convertedTotalCompReceive = self.ui.txt_calc_eur_comp_receive.text()

                result = pyautogui.confirm("Satış Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    db_result = database.shop_sale_db.updateShopSale(ShopSale)
                    if(db_result):
                        pyautogui.alert("Satış Güncellendi!")
                        self.backToShopSalePanel()
                    else:pyautogui.alert("Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")
            else:
                ShopSale = shop_sale.obj_shop_sale.ShopSale
                ShopSale.id = None
                ShopSale.guideId = self.guide_model.data(self.guide_model.index(self.ui.cmb_guide.currentIndex(), 0))
                ShopSale.tourName = self.ui.txt_tour_name.text()
                ShopSale.tourType = self.ui.cmb_tour_type.currentText()
                ShopSale.hotel = self.ui.txt_hotel.text()
                ShopSale.note = self.ui.txt_note.toPlainText()
                ShopSale.operatorId = self.operator_model.data(
                    self.operator_model.index(self.ui.cmb_operator.currentIndex(), 0))
                ShopSale.shopId = self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0))
                ShopSale.shopProductId = self.product_model.data(
                    self.product_model.index(self.ui.cmb_product.currentIndex(), 0))
                ShopSale.totalPax = self.ui.txt_pax.text()
                ShopSale.totalSale = self.ui.txt_total_sale.text()
                ShopSale.totalCommissionAmount = self.ui.txt_calc_org_comp.text()
                ShopSale.guideCommissionAmount = self.ui.txt_calc_org_guide.text()
                ShopSale.operatorCommissionAmount = self.ui.txt_calc_org_operator.text()
                ShopSale.driverCommissionAmount = self.ui.txt_calc_org_driver.text()
                ShopSale.chiefCommissionAmount = self.ui.txt_calc_org_chief.text()
                ShopSale.totalLandingFeeAmount = self.ui.txt_calc_org_landing.text()
                ShopSale.totalVipCommissionAmount = self.ui.txt_calc_org_vip_comp.text()
                ShopSale.moneyOnGuide = self.ui.check_money_on_guide.isChecked()
                ShopSale.moneyReceived = self.ui.check_received.isChecked()
                ShopSale.isForwardedSale = self.ui.check_forward.isChecked()
                ShopSale.saleDate = self.ui.dtp_sale.date().toString("dd-MM-yyyy") + " 01:00:00"
                ShopSale.forwardDate = self.ui.dtp_forward.date().toString("dd-MM-yyyy") +" 01:00:00"
                ShopSale.shopCurrency = self.ui.cmb_currency.currentText()
                ShopSale.convertCurrency = "EUR"
                ShopSale.rate = self.ui.txt_rate.text()
                ShopSale.convertedTotalSale = str(float(self.ui.txt_total_sale.text()) * float(self.ui.txt_rate.text()))
                ShopSale.convertedTotalCommissionAmount = self.ui.txt_calc_eur_comp.text()
                ShopSale.convertedGuideCommissionAmount = self.ui.txt_calc_eur_guide.text()
                ShopSale.convertedOperatorCommissionAmount = self.ui.txt_calc_eur_operator.text()
                ShopSale.convertedDriverCommissionAmount = self.ui.txt_calc_eur_driver.text()
                ShopSale.convertedChiefCommissionAmount = self.ui.txt_calc_eur_chief.text()
                ShopSale.convertedTotalLandingFeeAmount = self.ui.txt_calc_eur_landing.text()
                ShopSale.convertedTotalVipCommissionAmount = self.ui.txt_calc_eur_vip_comp.text()
                ShopSale.totalCompanyIncome = self.ui.txt_calc_org_total.text()
                ShopSale.convertedCompanyIncome = self.ui.txt_calc_eur_total.text()
                ShopSale.addVip = self.ui.check_vip.isChecked()
                ShopSale.addLanding = self.ui.check_landing.isChecked()
                ShopSale.addChief = self.ui.check_landing.isChecked()
                ShopSale.productName = self.ui.cmb_product.currentText()
                ShopSale.guideSelection = GLOBAL_SELECTED_GUIDE
                ShopSale.vipCommissionAmountRep = self.ui.txt_calc_org_vip_rep.text()
                ShopSale.convertedVipCommissionAmountRep = self.ui.txt_calc_eur_vip_rep.text()
                ShopSale.shopName = self.ui.cmb_shop.currentText()
                ShopSale.status = 1
                ShopSale.totalCompReceive = self.ui.txt_calc_org_comp_receive.text()
                ShopSale.convertedTotalCompReceive = self.ui.txt_calc_eur_comp_receive.text()
                result = pyautogui.confirm("Yeni Satış Eklenecek.Onaylıyor Musunuz ?")
                if (result == "OK"):
                    db_result = database.shop_sale_db.addShopSale(ShopSale)
                    if (db_result):
                        pyautogui.alert("Satış Eklendi!")
                        self.backToShopSalePanel()
                    else:
                        pyautogui.alert(
                            "Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop_sale.ui_shop_sale_entry.ShopSaleEntryPanel()
        self.ui.setupUi(self)
        self.guide_model = self.ui.cmb_guide.model()
        self.shop_model = self.ui.cmb_shop.model()
        self.product_model = self.ui.cmb_product.model()
        self.operator_model = self.ui.cmb_operator.model()
        self.ui.cmb_product.setEnabled(False)
        self.ui.dtp_sale.setDate(datetime.date.today())
        self.ui.dtp_sale.setDisplayFormat("dd-MM-yyyy")
        self.ui.cmb_shop.setEnabled(False)
        self.ui.dtp_sale.setEnabled(False)

        self.ui.txt_pax.setValidator(QtGui.QIntValidator())
        self.ui.txt_total_sale.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_rate.setValidator(QtGui.QDoubleValidator())
        self.ui.frame_10.setEnabled(False)

        operator_list = self.getOperatorList()

        for i in operator_list:
            it8 = QtGui.QStandardItem(str(i[0]))
            it9 = QtGui.QStandardItem(str(i[1]))
            self.operator_model.appendRow((it8, it9))

        self.ui.cmb_operator.setModel(self.operator_model)
        self.ui.cmb_operator.setModelColumn(1)
        self.ui.cmb_operator.setCurrentIndex(-1)


        guide_list = self.getGuideList()

        for i in guide_list:
            it1 = QtGui.QStandardItem(str(i[0]))
            it2 = QtGui.QStandardItem(str(i[1]))
            it3 = QtGui.QStandardItem(str(i[4]))
            self.guide_model.appendRow((it1, it2, it3))

        self.ui.cmb_guide.setModel(self.guide_model)
        self.ui.cmb_guide.setModelColumn(1)
        self.ui.cmb_guide.setCurrentIndex(-1)

        shop_list = self.getShopList()

        for i in shop_list:
            it3 = QtGui.QStandardItem(str(i[0]))
            it4 = QtGui.QStandardItem(str(i[2]))
            it11 = QtGui.QStandardItem(str(i[11]))
            self.shop_model.appendRow((it3,it4,it11))

        self.ui.cmb_shop.setModel(self.shop_model)
        self.ui.cmb_shop.setModelColumn(1)
        self.ui.cmb_shop.setCurrentIndex(-1)

        if(shop_sale.main_shop_sale.GLOBAL_UPDATE == 1):
            global GLOBAL_CHIEF_COMMISSION
            GLOBAL_CHIEF_COMMISSION = self.setChiefCommission(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.operatorId)

            self.ui.cmb_shop.setEnabled(True)
            self.ui.dtp_sale.setEnabled(True)
            self.fillSelectedShopProductCommissions()
            self.ui.cmb_shop.setCurrentIndex(self.ui.cmb_shop.findText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.shopName))
            self.ui.cmb_product.setEnabled(True)
            self.fillShopProducts(datetime.datetime.strptime(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.saleDate,"%d-%m-%Y %H:%M:%S"))

            self.ui.cmb_product.setCurrentIndex(self.ui.cmb_product.findText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.productName))
            self.fillSelectedShopProductCommissions()
            self.ui.cmb_guide.setCurrentIndex(self.ui.cmb_guide.findText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.guideName))
            self.ui.dtp_sale.setDate(datetime.datetime.strptime(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.saleDate,"%d-%m-%Y %H:%M:%S"))

            self.ui.txt_tour_name.setText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.tourName)
            self.ui.cmb_tour_type.setCurrentIndex(self.ui.cmb_tour_type.findText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.tourType))
            self.ui.txt_hotel.setText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.hotel)
            self.ui.cmb_operator.setCurrentIndex(self.ui.cmb_operator.findText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.operatorName))
            self.ui.txt_pax.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalPax))
            self.ui.txt_total_sale.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalSale))
            self.ui.cmb_currency.setCurrentIndex(self.ui.cmb_currency.findText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.shopCurrency))
            self.ui.check_forward.setChecked(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.isForwardedSale)
            self.ui.dtp_forward.setDate(datetime.datetime.strptime(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.forwardDate,"%d-%m-%Y %H:%M:%S"))
            self.ui.check_vip.setChecked(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.addVip)
            self.ui.check_landing.setChecked(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.addLanding)
            self.ui.check_chief.setChecked(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.addChief)
            self.ui.check_received.setChecked(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.moneyReceived)
            self.ui.check_money_on_guide.setChecked(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.moneyOnGuide)
            self.ui.txt_rate.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.rate))
            self.ui.txt_note.setText(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.note)

            self.ui.txt_calc_org_guide.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.guideCommissionAmount))
            self.ui.txt_calc_eur_guide.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedGuideCommissionAmount))

            self.ui.txt_calc_org_driver.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.driverCommissionAmount))
            self.ui.txt_calc_eur_driver.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedDriverCommissionAmount))

            self.ui.txt_calc_org_operator.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.operatorCommissionAmount))
            self.ui.txt_calc_eur_operator.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedOperatorCommissionAmount))

            self.ui.txt_calc_org_chief.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.chiefCommissionAmount))
            self.ui.txt_calc_eur_chief.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedChiefCommissionAmount))

            self.ui.txt_calc_org_landing.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalLandingFeeAmount))
            self.ui.txt_calc_eur_landing.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedTotalLandingFeeAmount))

            self.ui.txt_calc_org_vip_rep.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.vipCommissionAmountRep))
            self.ui.txt_calc_eur_vip_rep.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedVipCommissionAmountRep))

            self.ui.txt_calc_org_vip_comp.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalVipCommissionAmount))
            self.ui.txt_calc_eur_vip_comp.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedTotalVipCommissionAmount))

            self.ui.txt_calc_org_comp.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalCommissionAmount))
            self.ui.txt_calc_eur_comp.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedTotalCommissionAmount))

            self.ui.txt_calc_org_total.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalCompanyIncome))
            self.ui.txt_calc_eur_total.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedCompanyIncome))

            self.ui.txt_calc_org_comp_receive.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.totalCompReceive))
            self.ui.txt_calc_eur_comp_receive.setText(str(shop_sale.main_shop_sale.GLOBAL_OBJECT_SHOP_SALE.convertedTotalCompReceive))
        else:
            """if (self.ui.cmb_shop.currentIndex() != 0):
                self.ui.cmb_shop.currentIndexChanged(self.fillShopProducts(self.product_model.data(self.product_model.index(self.ui.cmb_product.currentIndex(), 0)),self.ui.dtp_sale.date().toString("dd-MM-yyyy")))
                self.ui.txt_def_guide_rate.setText(GLOBAL_SELECTED_SHOP_PRODUCT.guideCommission)
                self.ui.txt_def_driver_rate.setText(GLOBAL_SELECTED_SHOP_PRODUCT.driverCommission)
                self.ui.txt_def_opr_rate.setText(GLOBAL_SELECTED_SHOP_PRODUCT.operatorCommission)
                self.ui.txt_def_guide_rate_2.setText(GLOBAL_SELECTED_SHOP_PRODUCT.totalCommission)
                self.ui.txt_def_guide_rate_3.setText(GLOBAL_SELECTED_SHOP_PRODUCT.companyCommissionWithGuide)
                self.ui.txt_def_guide_rate_4.setText(GLOBAL_SELECTED_SHOP_PRODUCT.companyCommissionWithHotel)"""

            """if(self.ui.cmb_operator.currentIndex() != 0):
                self.ui.cmb_operator.currentIndexChanged(self.setChiefCommission(self.operator_model.data(self.operator_model.index(self.ui.cmb_operator.currentIndex(), 0))))"""

            """if (self.ui.cmb_shop.currentIndex() != 0):
                self.ui.cmb_shop.currentIndexChanged(self.getShopCommissionRates(
                    self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0))))"""






            #self.ui.cmb_shop.currentIndexChanged.connect(self.fillShopProducts(self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0)),self.ui.dtp_sale.date().toString("dd-mm-yyyy")))
            #self.ui.dtp_sale.dateChanged.connect(self.fillShopProducts(self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0)),self.ui.dtp_sale.date().toString("dd-mm-yyyy")))

        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if self.returnStatus() == 1:
                self.maximize_restore()

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()



        # SET TITLE BAR
        self.ui.frame_move.mouseMoveEvent = moveWindow
        self.uiDefinitions()
        self.show()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 158, 171, 255), stop:1 rgba(238, 242, 243, 255));border-radius:10px; ")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 158, 171, 255), stop:1 rgba(238, 242, 243, 255));border-radius:10px; ")
            self.ui.btn_maximize.setToolTip("Maximize")

    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showMaximized()
        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        """self.ui.dtp_sale.setCorrectionMode(0)

        self.ui.dtp_forward.setCorrectionMode(0)"""

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: self.maximize_restore())

        # BACK TO HOME PANEL
        self.ui.btn_back.clicked.connect(lambda: self.backToShopSalePanel())

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # GUIDE COMBO INDEX CHANGE EVENT
        self.ui.cmb_guide.currentIndexChanged.connect(self.changeGuideEvent)

        # SHOP COMBO INDEX CHANGE EVENT
        self.ui.cmb_shop.currentIndexChanged.connect(self.fillShopProducts)

        # SALE DATE INDEX CHANGE EVENT
        self.ui.dtp_sale.dateChanged.connect(self.fillShopProducts)

        # PRODUCT COMBO INDEX CHANGE EVENT
        self.ui.cmb_product.currentIndexChanged.connect(self.fillSelectedShopProductCommissions)

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        # ADD SHOP SALE
        self.ui.btn_save.clicked.connect(lambda : self.saveToDb())

        # CALCULATE BUTTON
        self.ui.btn_calculate.clicked.connect(self.calculate)

        # GET GUIDE TYPE
        self.ui.cmb_guide.currentIndexChanged.connect(self.setGuideType)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopSaleDefWindow()
    sys.exit(app.exec_())