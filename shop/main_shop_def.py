import sys
# GUI FILE
from PyQt5 import QtCore, QtSql, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import shop.ui_shop_def
import shop.main_shop
import database.shop_db
import database.area_db
import pyautogui
import shop.obj_shop
import utils.helper

GLOBAL_STATE = 0
GLOBAL_UPDATE = 0

class ShopDefWindow(QMainWindow):
    def backToShopPanel(self):
        self.window = shop.main_shop.ShopWindow()
        self.window.show()
        self.hide()

    def getAreaList(self):
        return database.area_db.getAreaList()

    def printCurrentCmb(self):
        print(self.model.data(self.model.index(self.ui.cmb_area.currentIndex(), 0)))

    def saveToDb(self):
        if (utils.helper.fieldCheck(self.ui.txt_name.text()) != True or self.ui.cmb_area.currentIndex() == 0):
            pyautogui.alert("Mağaza Adı ve Bölgesi Boş Olamaz!")
        else:
            if (utils.helper.fieldCheck(self.ui.txt_landing.text()) != True):
                self.ui.txt_landing.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_vip_comp.text()) != True):
                self.ui.txt_vip_comp.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_vip_rep.text()) != True):
                self.ui.txt_vip_rep.setText(str(0.0))

            if(shop.main_shop.GLOBAL_UPDATE == 1):
                Shop = shop.main_shop.GLOBAL_OBJECT_SHOP
                Shop.name = self.ui.txt_name.text()
                Shop.mail = self.ui.txt_mail.text()
                Shop.phone = self.ui.txt_phone.text()
                Shop.commercialName = self.ui.txt_commercial.text()
                Shop.areaId = self.model.data(self.model.index(self.ui.cmb_area.currentIndex(), 0))
                Shop.currency = self.ui.cmb_currency.currentText()
                Shop.landingFee = self.ui.txt_landing.text()
                Shop.vipCommissionRep = self.ui.txt_vip_rep.text()
                Shop.vipCommission = self.ui.txt_vip_comp.text()
                result = pyautogui.confirm("Mağaza Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    db_result = database.shop_db.updateShop(Shop)
                    if(db_result):
                        pyautogui.alert("Mağaza Güncellendi!")
                        self.backToShopPanel()
                    else:pyautogui.alert("Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")
            else:
                Shop = shop.obj_shop.Shop(None,self.model.data(self.model.index(self.ui.cmb_area.currentIndex(), 0)),self.ui.cmb_area.currentText(),
                                          self.ui.txt_name.text(),self.ui.txt_commercial.text(),self.ui.txt_mail.text(),
                                          self.ui.txt_phone.text(),self.ui.txt_vip_comp.text(),self.ui.txt_landing.text(),
                                          self.ui.cmb_currency.currentText(),self.ui.txt_vip_rep.text())
                result = pyautogui.confirm(Shop.name + " Mağazası Eklenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    db_result = database.shop_db.addShop(Shop)
                    if (db_result):
                        pyautogui.alert("Mağaza Eklendi!")
                        self.backToShopPanel()
                    else:
                        pyautogui.alert(
                            "Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop.ui_shop_def.ShopDefPanel()
        self.ui.setupUi(self)
        self.ui.txt_phone.setInputMask("(000)-000-00-00")
        self.model = self.ui.cmb_area.model()
        area_list = self.getAreaList()
        for i in area_list:
            it1 = QtGui.QStandardItem(str(i[0]))
            it2 = QtGui.QStandardItem(str(i[1]))
            self.model.appendRow((it1,it2))

        self.ui.cmb_area.setModel(self.model)
        self.ui.cmb_area.setModelColumn(1)


        if (shop.main_shop.GLOBAL_UPDATE == 1):
            print(shop.main_shop.GLOBAL_OBJECT_SHOP.areaName)
            self.ui.cmb_area.setCurrentText(shop.main_shop.GLOBAL_OBJECT_SHOP.areaName)
            self.ui.txt_name.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.name)
            self.ui.txt_commercial.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.commercialName)
            self.ui.txt_mail.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.mail)
            self.ui.txt_phone.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.phone)
            self.ui.txt_vip_comp.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.vipCommission)
            self.ui.txt_vip_rep.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.vipCommissionRep)
            self.ui.txt_landing.setText(shop.main_shop.GLOBAL_OBJECT_SHOP.landingFee)
            self.ui.cmb_currency.setCurrentText(shop.main_shop.GLOBAL_OBJECT_SHOP.currency)

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
        self.ui.btn_back.clicked.connect(lambda: self.backToShopPanel())

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        # ADD SHOP
        self.ui.btn_save.clicked.connect(lambda : self.saveToDb())

        self.ui.txt_landing.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_vip_rep.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_vip_comp.setValidator(QtGui.QDoubleValidator())


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopDefWindow()
    sys.exit(app.exec_())