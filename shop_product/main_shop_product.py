import sys

# GUI FILE
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import shop_product.ui_shop_product
import shop_product.main_shop_product_def
import home.panel
import database.shop_product_db
import pyautogui
import shop_product.obj_shop_product
GLOBAL_STATE = 0
GLOBAL_SELECTED_SHOP_PRODUCT = None
GLOBAL_OBJECT_SHOP_PRODUCT = None
GLOBAL_UPDATE = 0

class ShopProductWindow(QMainWindow):
    def showDate(self):
        self.ui.tableWidget.setColumnHidden(0, False)
        self.ui.tableWidget.setColumnHidden(1, False)
        self.ui.tableWidget.setColumnHidden(2, False)
        print(self.ui.tableWidget.selectedItems()[12].text())
    def openShopProductDefPanel(self):
        self.window = shop_product.main_shop_product_def.ShopProductDefWindow()
        self.window.show()
        self.hide()

    def updateShopProduct(self):
        if(len(self.ui.tableWidget.selectedItems())==0):
            pyautogui.alert("Lütfen Güncellemek İstediğiniz Mağaza Ürününü Seçiniz!")
        else:
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(1, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            item = self.ui.tableWidget.selectedItems()
            global GLOBAL_OBJECT_SHOP_PRODUCT
            global GLOBAL_UPDATE
            GLOBAL_UPDATE = 1
            GLOBAL_OBJECT_SHOP_PRODUCT = shop_product.obj_shop_product.ShopProduct(item[0].text(), item[1].text(),item[3].text(),item[2].text(),item[4].text(),item[5].text(),item[6].text(),item[7].text(),item[8].text(),item[9].text(),item[10].text(),item[11].text(),item[12].text(),item[13].text())
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(1, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            self.window = shop_product.main_shop_product_def.ShopProductDefWindow()
            self.window.show()
            self.hide()

    def deleteSelectedShopProduct(self):
        self.ui.tableWidget.setColumnHidden(0, False)
        item = self.ui.tableWidget.selectedItems()
        global GLOBAL_SELECTED_SHOP_PRODUCT
        GLOBAL_SELECTED_SHOP_PRODUCT = item[0].text()
        self.ui.tableWidget.setColumnHidden(0, True)
        result = pyautogui.confirm("Seçilen Mağaza Ürünü Silinecek. Onaylıyor Musunuz?")
        if(result == "OK"):
            database.shop_product_db.deleteShopProduct(GLOBAL_SELECTED_SHOP_PRODUCT)
            self.fill_table()
            pyautogui.alert("Mağaza Ürünü Silindi!")

    def backToMainPanel(self):
        self.window = home.panel.Panel()
        self.window.show()
        self.hide()

    def fill_table(self):
        shop_product_list =  database.shop_product_db.getShopProductList()
        if(shop_product_list):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(shop_product_list):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    self.ui.tableWidget.setItem(row,column, QTableWidgetItem(str(item)))
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop_product.ui_shop_product.ShopProductPanel()
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
        self.ui.btn_delete.clicked.connect(lambda: self.deleteSelectedShopProduct())

        self.ui.btn_update.clicked.connect(lambda: self.updateShopProduct())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        #HIDE FIRST COLUMN
        self.ui.tableWidget.setColumnHidden(0,True)
        self.ui.tableWidget.setColumnHidden(1, True)
        self.ui.tableWidget.setColumnHidden(2, True)

        # OPEN ADD NEW AREA PANEL
        self.ui.btn_add.clicked.connect(lambda : self.openShopProductDefPanel())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopProductWindow()
    sys.exit(app.exec_())