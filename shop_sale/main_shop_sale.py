import sys

# GUI FILE
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import shop_sale.ui_shop_sale
import shop_sale.main_shop_sale_def
import home.panel
import database.shop_sale_db
import pyautogui
import shop_sale.obj_shop_sale
GLOBAL_STATE = 0
GLOBAL_SELECTED_SHOP_SALE = None
GLOBAL_OBJECT_SHOP_SALE = None
GLOBAL_UPDATE = 0

class ShopSaleWindow(QMainWindow):
    def openShopSaleDefPanel(self):
        self.window = shop_sale.main_shop_sale_def.ShopSaleDefWindow()
        self.window.show()
        self.hide()

    def updateShopSale(self):
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
            for i in result:
                print(i)
            GLOBAL_OBJECT_SHOP_SALE = shop_sale.obj_shop_sale.ShopSale(
                result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],
                result[0][7],result[0][8],result[0][9],result[0][10],result[0][11],result[0][12],result[0][13],
                result[0][14],result[0][15],result[0][16],result[0][17],result[0][18],result[0][19],result[0][20],result[0][21],
                result[0][22],result[0][23],result[0][24],result[0][25],result[0][26],result[0][27],
                result[0][28],result[0][29],result[0][30],result[0][31],result[0][32],result[0][33],result[0][34],
                result[0][35],result[0][36],result[0][37],result[0][38],result[0][39],result[0][40],result[0][41],result[0][42],result[0][43],result[0][44],result[0][45])
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            self.ui.tableWidget.setColumnHidden(5, False)
            self.ui.tableWidget.setColumnHidden(7, False)
            self.ui.tableWidget.setColumnHidden(8, False)
            self.window = shop_sale.main_shop_sale_def.ShopSaleDefWindow()
            self.window.show()
            self.hide()

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

    def fill_table(self):
        shop_sale_list =  database.shop_sale_db.getShopSaleList()
        if(shop_sale_list):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(shop_sale_list):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    self.ui.tableWidget.setItem(row,column, QTableWidgetItem(str(item)))
                    align = self.ui.tableWidget.item(row, column)
                    align.setTextAlignment(QtCore.Qt.AlignCenter)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop_sale.ui_shop_sale.ShopSalePanel()
        self.ui.setupUi(self)
        self.fill_table()
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

        self.ui.btn_update.clicked.connect(lambda: self.updateShopSale())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        #HIDE FIRST COLUMN
        self.ui.tableWidget.setColumnHidden(0,True)
        self.ui.tableWidget.setColumnHidden(2, True)
        self.ui.tableWidget.setColumnHidden(5, True)
        self.ui.tableWidget.setColumnHidden(7, True)
        self.ui.tableWidget.setColumnHidden(8, True)

        # OPEN ADD NEW SHOP SALE
        self.ui.btn_add.clicked.connect(lambda : self.openShopSaleDefPanel())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopSaleWindow()
    sys.exit(app.exec_())