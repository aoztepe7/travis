import datetime
import sys

# GUI FILE
import threading

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QEvent, QThread, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QColor, QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem, QWidget

import shop_sale.ui_shop_sale
import shop_sale.main_shop_sale_def
import home.panel
import database.shop_sale_db
import database.shop_db
import database.guide_db
import shop_product.obj_shop_product
import database.shop_product_db
import pyautogui
import shop_sale.object_sale
import shop_sale.main_shop_sale_def
import database.product_db
import database.operator_db
GLOBAL_STATE = 0
GLOBAL_SELECTED_SHOP_SALE = None
GLOBAL_OBJECT_SHOP_SALE = None
GLOBAL_SELECTED_SHOP_PRODUCT = None
GLOBAL_UPDATE = 0
GLOBAL_EVENTS_ACTIVE = 0
GLOBAL_PRODUCT_LIST =None


class ShopSaleWindow(QMainWindow):
    def resetProductCombo(self):
        for i in GLOBAL_PRODUCT_LIST:
            it0 = QtGui.QStandardItem(str(i[0]))
            it1 = QtGui.QStandardItem(str(i[1]))
            self.product_model.appendRow((it0, it1))

        self.ui.cmb_product.setModel(self.product_model)
        self.ui.cmb_product.setModelColumn(1)
        self.ui.cmb_product.setCurrentIndex(-1)

    """def openShopSaleDefPanel(self):
        self.window = shop_sale.main_shop_sale_def.ShopSaleDefWindow()
        self.window.show()
        self.hide()"""
    def fillSearchValues(self):
        self.shop_model = self.ui.cmb_shop.model()
        self.guide_model = self.ui.cmb_guide.model()
        self.product_model = self.ui.cmb_product.model()
        self.operator_model = self.ui.cmb_operator.model()


        it_def_0 = QtGui.QStandardItem(str(0))
        it_def_1 = QtGui.QStandardItem(str(""))
        self.shop_model.appendRow((it_def_0, it_def_1))
        self.guide_model.appendRow((it_def_0, it_def_1))
        self.product_model.appendRow((it_def_0, it_def_1))
        self.operator_model.appendRow((it_def_0, it_def_1))

        operator_list = self.getOperatorList()

        for i in operator_list:
            it0 = QtGui.QStandardItem(str(i[0]))
            it1 = QtGui.QStandardItem(str(i[1]))
            self.operator_model.appendRow((it0, it1))

        self.ui.cmb_operator.setModel(self.operator_model)
        self.ui.cmb_operator.setModelColumn(1)
        self.ui.cmb_operator.setCurrentIndex(-1)

        product_list = self.getProductList()
        global  GLOBAL_PRODUCT_LIST
        GLOBAL_PRODUCT_LIST = product_list

        for i in product_list:
            it0 = QtGui.QStandardItem(str(i[0]))
            it1 = QtGui.QStandardItem(str(i[1]))
            self.product_model.appendRow((it0, it1))

        self.ui.cmb_product.setModel(self.product_model)
        self.ui.cmb_product.setModelColumn(1)
        self.ui.cmb_product.setCurrentIndex(-1)

        shop_list = self.getShopList()
        for i in shop_list:
            it0 = QtGui.QStandardItem(str(i[0]))
            it1 = QtGui.QStandardItem(str(i[2]))
            self.shop_model.appendRow((it0, it1))

        self.ui.cmb_shop.setModel(self.shop_model)
        self.ui.cmb_shop_2.setModel(self.shop_model)
        self.ui.cmb_shop.setModelColumn(1)
        self.ui.cmb_shop_2.setModelColumn(1)
        self.ui.cmb_shop.setCurrentIndex(-1)
        self.ui.cmb_shop_2.setCurrentIndex(-1)

        guide_list = self.getGuideList()

        for i in guide_list:
            it2 = QtGui.QStandardItem(str(i[0]))
            it3 = QtGui.QStandardItem(str(i[1]))
            self.guide_model.appendRow((it2, it3))

        self.ui.cmb_guide.setModel(self.guide_model)
        self.ui.cmb_guide_2.setModel(self.guide_model)
        self.ui.cmb_guide.setModelColumn(1)
        self.ui.cmb_guide_2.setModelColumn(1)
        self.ui.cmb_guide.setCurrentIndex(-1)
        self.ui.cmb_guide_2.setCurrentIndex(-1)


    def fillBoxes(self):
        if(len(self.ui.tableWidget.selectedItems()) == 0):
            pyautogui.alert("Lütfen Bir Satış Seçiniz!")
        else:
            self.ui.tableWidget.setColumnHidden(0, False)
            item = self.ui.tableWidget.selectedItems()
            result = database.shop_sale_db.fillBoxesWithValues(item[0].text())
            if(result):
                shopSale = shop_sale.object_sale.ShopSale(
                    id=result[0][0],
                    guideId=result[0][1],
                    tourName=result[0][2],
                    tourType=result[0][3],
                    hotel=result[0][4],
                    note=result[0][5],
                    operatorId=result[0][6],
                    shopId=result[0][7],
                    shopProductId=result[0][8],
                    totalPax=result[0][9],
                    totalSale=result[0][10],
                    moneyOnGuide=result[0][11],
                    moneyReceived=result[0][12],
                    isForwardedSale=result[0][13],
                    saleDate=result[0][14],
                    forwardDate=result[0][15],
                    shopCurrency=result[0][16],
                    rate=result[0][17],
                    addVip=result[0][18],
                    addLanding=result[0][19],
                    addChief=result[0][20],
                    productName=result[0][21],
                    guideSelection=result[0][22],
                    guideName=result[0][23],
                    operatorName=result[0][24],
                    shopName=result[0][25],
                    guideCommRate=result[0][26],
                    driverCommRate=result[0][27],
                    operatorCommRate=result[0][28],
                    hotelRepCommRate=result[0][29],
                    totalCommRate=result[0][30],
                    compRateGuide=result[0][31],
                    compRateHotel=result[0][32]
                   )
                self.ui.tableWidget.setColumnHidden(0, True)


                self.ui.cmb_guide_2.setCurrentIndex(
                    self.ui.cmb_guide_2.findText(shopSale.guideName))
                self.ui.cmb_shop_2.setCurrentIndex(
                    self.ui.cmb_shop_2.findText(shopSale.shopName))
                self.ui.dtp_sale.setDate(
                    datetime.datetime.strptime(shopSale.saleDate,
                                               "%d-%m-%Y %H:%M:%S"))
                self.ui.cmb_product.setCurrentIndex(
                    self.ui.cmb_product.findText(shopSale.productName))

                self.ui.txt_def_guide_rate.setText(str(shopSale.guideCommRate))
                self.ui.txt_def_driver_rate.setText(str(shopSale.driverCommRate))
                self.ui.txt_def_opr_rate.setText(str(shopSale.operatorCommRate))
                self.ui.txt_def_reo_rate.setText(str(shopSale.hotelRepCommRate))
                self.ui.txt_def_guide_rate_2.setText(str(shopSale.totalCommRate))
                self.ui.txt_def_guide_rate_3.setText(str(shopSale.compRateGuide))
                self.ui.txt_def_guide_rate_4.setText(str(shopSale.compRateHotel))

                self.ui.txt_tour_name.setText(str(shopSale.tourName))
                self.ui.cmb_tour_type_2.setCurrentIndex(
                    self.ui.cmb_tour_type_2.findText(shopSale.tourType))
                self.ui.txt_hotel.setText(shopSale.hotel)
                self.ui.cmb_operator.setCurrentIndex(
                    self.ui.cmb_operator.findText(shopSale.operatorName))
                self.ui.txt_pax.setText(str(shopSale.totalPax))
                self.ui.txt_total_sale.setText(str(shopSale.totalSale))
                self.ui.cmb_currency.setCurrentIndex(
                    self.ui.cmb_currency.findText(shopSale.shopCurrency))
                self.ui.check_forward.setChecked(shopSale.isForwardedSale)
                self.ui.dtp_forward.setDate(
                    datetime.datetime.strptime(shopSale.forwardDate,
                                               "%d-%m-%Y %H:%M:%S"))
                self.ui.check_vip.setChecked(shopSale.addVip)
                self.ui.check_landing.setChecked(shopSale.addLanding)
                self.ui.check_chief.setChecked(shopSale.addChief)
                self.ui.check_received.setChecked(shopSale.moneyReceived)
                self.ui.check_money_on_guide.setChecked(shopSale.moneyOnGuide)
                self.ui.txt_rate.setText(str(shopSale.rate))
                self.ui.txt_note.setText(shopSale.note)

    def fillSelectedShopProductCommissions(self):
        if(GLOBAL_EVENTS_ACTIVE != 0):
            if(self.ui.cmb_product.currentIndex() != -1 ):
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

    def clearAndGetNewShopProducts(self,oldProductText):
        if(GLOBAL_EVENTS_ACTIVE != 0):
            if (self.ui.cmb_shop_2.currentIndex() != -1 and self.ui.cmb_shop_2.currentIndex() != 0 ):
                product_list = database.shop_product_db.getShopProductsByShopIdAndDate(
                    self.shop_model.data(self.shop_model.index(self.ui.cmb_shop_2.currentIndex(), 0)),
                    self.ui.dtp_sale.date().toString("dd-MM-yyyy"))
                if (product_list):
                    for i in product_list:
                        it5 = QtGui.QStandardItem(str(i[0]))
                        it6 = QtGui.QStandardItem(str(i[2]))
                        self.product_model.appendRow((it5, it6))


                self.ui.cmb_product.setModel(self.product_model)
                self.ui.cmb_product.setModelColumn(1)
                self.ui.cmb_product.setCurrentIndex(self.ui.cmb_product.findText(oldProductText))
                self.fillSelectedShopProductCommissions()
                self.ui.cmb_product.setEnabled(True)

    def fillShopProducts(self):
        if(GLOBAL_EVENTS_ACTIVE != 0):
            self.ui.cmb_product.clear()
            if(self.ui.cmb_shop_2.currentIndex() != 0 and self.ui.cmb_shop_2.currentIndex() != -1):
                product_list = database.shop_product_db.getShopProductsByShopIdAndDate(self.shop_model.data(self.shop_model.index(self.ui.cmb_shop_2.currentIndex(), 0)),self.ui.dtp_sale.date().toString("dd-MM-yyyy"))
                if (product_list):
                    it_def_0 = QtGui.QStandardItem(str(0))
                    it_def_1 = QtGui.QStandardItem(str(""))
                    self.product_model.appendRow((it_def_0, it_def_1))
                    for i in product_list:
                        it5 = QtGui.QStandardItem(str(i[0]))
                        it6 = QtGui.QStandardItem(str(i[2]))
                        self.product_model.appendRow((it5, it6))

                self.ui.cmb_product.setModel(self.product_model)
                self.ui.cmb_product.setModelColumn(1)
                self.ui.cmb_product.setCurrentIndex(0)



    def updateEnabled(self):
        if (len(self.ui.tableWidget.selectedItems()) != 0):
            global GLOBAL_UPDATE
            GLOBAL_UPDATE = 1
            global GLOBAL_EVENTS_ACTIVE
            GLOBAL_EVENTS_ACTIVE = 1
            self.ui.frame_25.setEnabled(True)
            oldProductText = self.ui.cmb_product.currentText()
            self.ui.cmb_product.clear()
            self.clearAndGetNewShopProducts(oldProductText)
        else:
            pyautogui.alert("Lütfen Bir Seçim Yapınız!")
            return


    def deleteSelectedShopSale(self):
        self.ui.tableWidget.setColumnHidden(0, False)
        item = self.ui.tableWidget.selectedItems()
        global GLOBAL_SELECTED_SHOP_SALE
        GLOBAL_SELECTED_SHOP_SALE = item[0].text()
        self.ui.tableWidget.setColumnHidden(0, True)
        result = pyautogui.confirm("Seçilen Satış Silinecek. Onaylıyor Musunuz?")
        if(result == "OK"):
            database.shop_sale_db.deleteShopSale(GLOBAL_SELECTED_SHOP_SALE)
            self.fill_table()
            pyautogui.alert("Satış Silindi!")

    def backToMainPanel(self):
        self.window = home.panel.Panel()
        self.window.show()
        self.hide()

    def getShopList(self):
        return database.shop_db.getShopList()

    def getProductList(self):
        return database.product_db.getProductList()

    def getGuideList(self):
        return database.guide_db.getGuideList()

    def getOperatorList(self):
        return database.operator_db.getOperatorList()

    def search(self):
        self.ui.tableWidget.setRowCount(0)
        start_date = self.ui.dtp_start.date().toString("dd-MM-yyyy") + " 01:00:00"
        finish_date = self.ui.dtp_finish.date().toString("dd-MM-yyyy") + " 23:59:00"
        start_date_formatted = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        finish_date_formatted = datetime.datetime.strptime(finish_date, "%d-%m-%Y %H:%M:%S")
        formatted_finish_date = finish_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        base_query = """SELECT shop_sale.id,DATE_FORMAT(shop_sale.sale_date,'%d-%m-%Y'),guide.full_name,shop.name,shop_sale.tour_type,shop_sale.total_sale,shop_sale.shop_currency 
        from shop_sale inner join guide on shop_sale.guide_id = guide.id 
        inner join shop on shop_sale.shop_id = shop.id
        inner join shop_product on shop_sale.shop_product_id = shop_product.id where shop_sale.status = true"""
        continues_query =""
        if(self.ui.cmb_shop.currentIndex() != -1 and self.ui.cmb_shop.currentIndex() != 0):
            continues_query = continues_query + " and shop_sale.shop_id ="+self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0))
        if (self.ui.cmb_guide.currentIndex() != -1 and self.ui.cmb_guide.currentIndex() != 0):
            continues_query =continues_query + " and shop_sale.guide_id =" + self.guide_model.data(
                self.guide_model.index(self.ui.cmb_guide.currentIndex(), 0))
        if (self.ui.cmb_tour_type.currentIndex() != -1 and self.ui.cmb_tour_type.currentIndex() != 0):
            continues_query = continues_query + " and shop_sale.tour_type ='"+self.ui.cmb_tour_type.currentText()+"'"
        continues_query = continues_query + " and sale_date between CAST('"+formatted_start_date+"' as datetime) and CAST('"+formatted_finish_date+"' as datetime)"
        complete_query = base_query + continues_query + " order by shop_sale.sale_date"
        result = database.shop_sale_db.getSearchQueryResult(complete_query)
        print(complete_query)
        if (result):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(result):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    #align = self.ui.tableWidget.item(row, column)
                    #align.setTextAlignment(QtCore.Qt.AlignCenter)

    def mousePressEv(self):
        if(len(self.ui.tableWidget.selectedItems()) != 0):
            global  GLOBAL_UPDATE
            global GLOBAL_EVENTS_ACTIVE
            GLOBAL_EVENTS_ACTIVE = 0
            GLOBAL_UPDATE = 0
            self.resetProductCombo()
            self.ui.frame_25.setEnabled(False)
            self.fillBoxes()

    def clearBoxes(self):
        self.ui.cmb_guide_2.setCurrentIndex(0)
        self.ui.cmb_shop_2.setCurrentIndex(0)
        self.ui.cmb_shop_2.setCurrentIndex(0)
        self.ui.dtp_sale.setDate(datetime.date.today())
        self.ui.txt_def_guide_rate.clear()
        self.ui.txt_def_driver_rate.clear()
        self.ui.txt_def_opr_rate.clear()
        self.ui.txt_def_reo_rate.clear()
        self.ui.txt_def_guide_rate_2.clear()
        self.ui.txt_def_guide_rate_3.clear()
        self.ui.txt_def_guide_rate_4.clear()
        self.ui.txt_tour_name.clear()
        self.ui.cmb_tour_type.setCurrentIndex(0)
        self.ui.txt_hotel.clear()
        self.ui.cmb_operator.setCurrentIndex(0)
        self.ui.txt_pax.clear()
        self.ui.txt_total_sale.clear()
        self.ui.cmb_currency.setCurrentIndex(0)
        self.ui.check_forward.setChecked(False)
        self.ui.dtp_forward.setDate(datetime.date.today())
        self.ui.check_vip.setChecked(False)
        self.ui.check_landing.setChecked(False)
        self.ui.check_chief.setChecked(False)
        self.ui.check_received.setChecked(False)
        self.ui.check_money_on_guide.setChecked(False)
        self.ui.txt_rate.clear()
        self.ui.txt_note.clear()
        global GLOBAL_UPDATE
        GLOBAL_UPDATE = 0
        global GLOBAL_EVENTS_ACTIVE
        GLOBAL_EVENTS_ACTIVE = 1
        self.ui.cmb_product.clear()
        self.ui.cmb_product.setEnabled(False)


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop_sale.ui_shop_sale.ShopSalePanel()
        self.ui.setupUi(self)
        self.showMaximized()
        self.ui.dtp_start.setDate(datetime.date.today())
        self.ui.dtp_start.setDisplayFormat("dd-MM-yyyy")
        self.ui.dtp_finish.setDate(datetime.date.today())
        self.ui.dtp_finish.setDisplayFormat("dd-MM-yyyy")
        self.ui.dtp_sale.setDate(datetime.date.today())
        self.ui.dtp_sale.setDisplayFormat("dd-MM-yyyy")
        self.ui.dtp_forward.setDate(datetime.date.today())
        self.ui.dtp_forward.setDisplayFormat("dd-MM-yyyy")
        self.ui.frame_25.setEnabled(False)

        global GLOBAL_UPDATE
        GLOBAL_UPDATE = 0
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if self.returnStatus() == 1:
                self.maximize_restore()

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        def keyPressEvent(event):
            # IF Q PRESSED GET ID
            if event.key() == Qt.Key_R:
                self.ui.tableWidget.setColumnHidden(0, False)
                item = self.ui.tableWidget.selectedItems()
                self.ui.tableWidget.setColumnHidden(0, True)
                pyautogui.alert("Referans ID : "+ item[0].text())
                event.accept()
            if event.key() == Qt.Key_Down:
                current_row = self.ui.tableWidget.currentRow()
                self.ui.tableWidget.selectRow(current_row+1)
                self.fillBoxes()
                event.accept()
            if event.key() == Qt.Key_Up:
                current_row = self.ui.tableWidget.currentRow()
                self.ui.tableWidget.selectRow(current_row-1)
                self.fillBoxes()
                event.accept()
            if event.key() == Qt.LeftButton:
                current_row = self.ui.tableWidget.currentRow()
                self.ui.tableWidget.selectRow(current_row-1)
                self.fillBoxes()
                event.accept()



        # SET TITLE BAR
        self.ui.frame_move.mouseMoveEvent = moveWindow
        self.ui.tableWidget.keyPressEvent = keyPressEvent
        self.ui.tableWidget.clicked.connect(lambda : self.mousePressEv())
        self.uiDefinitions()
        self.show()
        self.fillSearchValues()

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

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: self.maximize_restore())

        # BACK TO HOME PANEL
        self.ui.btn_back.clicked.connect(lambda: self.backToMainPanel())

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # DELETE
        self.ui.btn_delete.clicked.connect(lambda: self.deleteSelectedShopSale())

        self.ui.btn_edit.clicked.connect(lambda: self.updateEnabled())

        self.ui.btn_search.clicked.connect(lambda: self.search())


        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        #HIDE FIRST COLUMN
        self.ui.tableWidget.setColumnHidden(0,True)

        # NEW ENTRY
        self.ui.btn_new.clicked.connect(lambda : self.clearBoxes())

        # SHOP COMBO INDEX CHANGE EVENT
        self.ui.cmb_shop_2.currentIndexChanged.connect(lambda : self.fillShopProducts())

        self.ui.cmb_product.currentIndexChanged.connect(lambda: self.fillSelectedShopProductCommissions())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopSaleWindow()
    sys.exit(app.exec_())