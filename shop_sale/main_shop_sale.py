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
import pyautogui
import shop_sale.obj_shop_sale
import shop_sale.main_shop_sale_def
GLOBAL_STATE = 0
GLOBAL_SELECTED_SHOP_SALE = None
GLOBAL_OBJECT_SHOP_SALE = None
GLOBAL_UPDATE = 0


class ShopSaleWindow(QMainWindow):
    """def openShopSaleDefPanel(self):
        self.window = shop_sale.main_shop_sale_def.ShopSaleDefWindow()
        self.window.show()
        self.hide()"""

    """def updateShopSale(self):
        if(len(self.ui.tableWidget.selectedItems())==0):
            pyautogui.alert("Lütfen Güncellemek İstediğiniz Satışı Seçiniz!")
        else:
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            self.ui.tableWidget.setColumnHidden(5, False)
            self.ui.tableWidget.setColumnHidden(7, False)
            self.ui.tableWidget.setColumnHidden(8, False)
            item = self.ui.tableWidget.selectedItems()
            global GLOBAL_OBJECT_SHOP_SALE
            global GLOBAL_UPDATE
            GLOBAL_UPDATE = 1
            result = database.shop_sale_db.getById(item[0].text())
            GLOBAL_OBJECT_SHOP_SALE = shop_sale.obj_shop_sale.ShopSale(
                result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],
                result[0][7],result[0][8],result[0][9],result[0][10],result[0][11],result[0][12],result[0][13],
                result[0][14],result[0][15],result[0][16],result[0][17],result[0][18],result[0][19],result[0][20],result[0][21],
                result[0][22],result[0][23],result[0][24],result[0][25],result[0][26],result[0][27],
                result[0][28],result[0][29],result[0][30],result[0][31],result[0][32],result[0][33],result[0][34],
                result[0][35],result[0][36],result[0][37],result[0][38],result[0][39],result[0][40],result[0][41],result[0][42],result[0][43],result[0][44],result[0][45],result[0][46],result[0][47])
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            self.ui.tableWidget.setColumnHidden(5, False)
            self.ui.tableWidget.setColumnHidden(7, False)
            self.ui.tableWidget.setColumnHidden(8, False)
            self.window = shop_sale.main_shop_sale_def.ShopSaleDefWindow()
            self.window.show()
            self.hide()"""



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


    """def fill_table(self):
        shop_sale_list =  database.shop_sale_db.getShortList()
        if(shop_sale_list):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(shop_sale_list):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    self.ui.tableWidget.setItem(row,column, QTableWidgetItem(str(item)))
                   # align = self.ui.tableWidget.item(row, column)
                   # align.setTextAlignment(QtCore.Qt.AlignCenter)"""

    def getShopList(self):
        return database.shop_db.getShopList()

    def getGuideList(self):
        return database.guide_db.getGuideList()

    def search(self):
        self.ui.tableWidget.setRowCount(0)
        start_date = self.ui.dtp_start.date().toString("dd-MM-yyyy") + " 01:00:00"
        finish_date = self.ui.dtp_finish.date().toString("dd-MM-yyyy") + " 23:59:00"
        start_date_formatted = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
        formatted_start_date = start_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        finish_date_formatted = datetime.datetime.strptime(finish_date, "%d-%m-%Y %H:%M:%S")
        formatted_finish_date = finish_date_formatted.strftime('%Y-%m-%d %H:%M:%S')
        base_query = """SELECT shop_sale.id,DATE_FORMAT(shop_sale.sale_date,'%d-%m-%Y'),shop_sale.guide_id,guide.full_name,shop_sale.tour_type,shop_sale.shop_id,shop.name,shop_sale.shop_product_id,shop_product.product_id,product.name,shop_sale.total_sale,shop_sale.shop_currency 
        from shop_sale inner join guide on shop_sale.guide_id = guide.id 
        inner join shop on shop_sale.shop_id = shop.id
        inner join shop_product on shop_sale.shop_product_id = shop_product.id
        inner join product on shop_product.product_id = product.id where shop_sale.status = true"""
        continues_query =""
        if(self.ui.cmb_shop.currentIndex() != -1 and self.ui.cmb_shop.currentIndex() != 0):
            continues_query = continues_query + " and shop_sale.shop_id ="+self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0))
        if (self.ui.cmb_guide.currentIndex() != -1 and self.ui.cmb_guide.currentIndex() != 0):
            continues_query =continues_query + " and shop_sale.guide_id =" + self.guide_model.data(
                self.guide_model.index(self.ui.cmb_guide.currentIndex(), 0))
        if (self.ui.cmb_tour_type.currentIndex() != -1 and self.ui.cmb_tour_type.currentIndex() != 0):
            continues_query = continues_query + " and shop_sale.tour_type ='"+self.ui.cmb_tour_type.currentText()+"'"
        continues_query = continues_query + " and sale_date between CAST('"+formatted_start_date+"' as datetime) and CAST('"+formatted_finish_date+"' as datetime)"
        complete_query = base_query + continues_query
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

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop_sale.ui_shop_sale.ShopSalePanel()
        self.ui.setupUi(self)
        #self.fill_table()
        self.ui.dtp_start.setDate(datetime.date.today())
        self.ui.dtp_start.setDisplayFormat("dd-MM-yyyy")
        self.ui.dtp_finish.setDate(datetime.date.today())
        self.ui.dtp_finish.setDisplayFormat("dd-MM-yyyy")

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
                event.accept()
            if event.key() == Qt.Key_Up:
                current_row = self.ui.tableWidget.currentRow()
                self.ui.tableWidget.selectRow(current_row-1)
                event.accept()

        # SET TITLE BAR
        self.ui.frame_move.mouseMoveEvent = moveWindow
        self.ui.tableWidget.keyPressEvent = keyPressEvent
        self.uiDefinitions()
        self.show()
        """thread = threading.Thread(target=self.fillSearchBars)
        thread.start()
        thread.join()"""
        self.shop_model = self.ui.cmb_shop.model()
        self.guide_model = self.ui.cmb_guide.model()

        shop_list = self.getShopList()
        it_def_0 = QtGui.QStandardItem(str(0))
        it_def_1 = QtGui.QStandardItem(str(""))
        self.shop_model.appendRow((it_def_0, it_def_1))
        self.guide_model.appendRow((it_def_0, it_def_1))
        for i in shop_list:
            it0 = QtGui.QStandardItem(str(i[0]))
            it1 = QtGui.QStandardItem(str(i[2]))
            self.shop_model.appendRow((it0, it1))

        self.ui.cmb_shop.setModel(self.shop_model)
        self.ui.cmb_shop.setModelColumn(1)
        self.ui.cmb_shop.setCurrentIndex(-1)

        guide_list = self.getGuideList()

        for i in guide_list:
            it2 = QtGui.QStandardItem(str(i[0]))
            it3 = QtGui.QStandardItem(str(i[1]))
            self.guide_model.appendRow((it2, it3))

        self.ui.cmb_guide.setModel(self.guide_model)
        self.ui.cmb_guide.setModelColumn(1)
        self.ui.cmb_guide.setCurrentIndex(-1)



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

        #self.ui.btn_update.clicked.connect(lambda: self.updateShopSale())

        self.ui.btn_search.clicked.connect(lambda: self.search())


        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        #HIDE FIRST COLUMN
        self.ui.tableWidget.setColumnHidden(0,True)


        # OPEN ADD NEW SHOP SALE
        #self.ui.btn_add.clicked.connect(lambda : self.openShopSaleDefPanel())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopSaleWindow()
    sys.exit(app.exec_())