import sys
# GUI FILE
from PyQt5 import QtCore, QtSql, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import shop_product.ui_shop_product_def
import shop_product.main_shop_product
import database.shop_product_db
import database.shop_db
import database.product_db
import pyautogui
import shop_product.obj_shop_product
import utils.helper
import datetime

GLOBAL_STATE = 0
GLOBAL_UPDATE = 0
GLOBAL_TOTAL_COMMISSION = 0
GLOBAL_COMP_COM_GUIDE = 0
GLOBAL_COMP_COM_REP = 0
GLOBAL_REP_COM = 0
GLOBAL_OPR_COM = 0
GLOBAL_DRIVER_COM = 0
GLOBAL_GUIDE_COM = 0

class ShopProductDefWindow(QMainWindow):
    def isExistInDb(self):
        result = database.shop_product_db.getExistingShopProduct(self.ui.dtp_start.date().toString("dd-MM-yyyy")+ " 00:01:00",self.ui.dtp_finish.date().toString("dd-MM-yyyy")+" 00:01:00")
        if(result):
            return True
        else:
            return False

    def isExistInDbUpdate(self):
        result = database.shop_product_db.getExistingShopProduct(self.ui.dtp_start.date().toString("dd-MM-yyyy")+ " 00:01:00",self.ui.dtp_finish.date().toString("dd-MM-yyyy")+" 00:01:00")
        if(result):
            return True
        else:
            return False

    def setTotalComToGlobal(self,text):
        global GLOBAL_TOTAL_COMMISSION
        if (text != ""):
            GLOBAL_TOTAL_COMMISSION = float(text)

    def setGuideComToGlobal(self,text):
        global GLOBAL_GUIDE_COM
        if (text != ""):
            GLOBAL_GUIDE_COM = float(text)

    def setDriverComToGlobal(self,text):
        global GLOBAL_DRIVER_COM
        if (text != ""):
            GLOBAL_DRIVER_COM = float(text)

    def setOperatorComToGlobal(self, text):
        global GLOBAL_OPR_COM
        if (text != ""):
            GLOBAL_OPR_COM = float(text)

    def setHotelRepComToGlobal(self, text):
        global GLOBAL_REP_COM
        if (text != ""):
            GLOBAL_REP_COM = float(text)

    def calculateCompGuideCommission(self):
        global GLOBAL_COMP_COM_GUIDE
        GLOBAL_COMP_COM_GUIDE = GLOBAL_TOTAL_COMMISSION - (GLOBAL_GUIDE_COM + GLOBAL_DRIVER_COM + GLOBAL_OPR_COM)
        self.ui.txt_comp_rate_guide.setText(str(GLOBAL_COMP_COM_GUIDE))

    def calculateCompRepCommission(self):
        global GLOBAL_COMP_COM_REP
        GLOBAL_COMP_COM_REP = GLOBAL_TOTAL_COMMISSION - (GLOBAL_REP_COM + GLOBAL_DRIVER_COM + GLOBAL_OPR_COM)
        self.ui.txt_comp_rate_rep.setText(str(GLOBAL_COMP_COM_REP))

    def backToShopProductPanel(self):
        self.window = shop_product.main_shop_product.ShopProductWindow()
        self.window.show()
        self.hide()

    def getShopList(self):
        return database.shop_db.getShopList()

    def getProductList(self):
        return database.product_db.getProductList()

    def saveToDb(self):
        if (self.ui.cmb_shop.currentIndex() == 0 or self.ui.cmb_product.currentIndex() == 0 or self.ui.cmb_shop.currentText() == "Mağaza Seçin..." or self.ui.cmb_product.currentText() == "Ürün Seçin..."):
            pyautogui.alert("Mağaza ve Ürün Boş Olamaz!")
            return
        if ((self.ui.dtp_start.date() > self.ui.dtp_finish.date()) == True):
            pyautogui.alert("Bitiş Tarihi Başlangıç Tarihinden Küçük Olamaz!")
            return
        total = GLOBAL_TOTAL_COMMISSION
        self.setDriverComToGlobal(self.ui.txt_driver_com_rate.text())
        self.setGuideComToGlobal(self.ui.txt_guide_com_rate.text())
        self.setOperatorComToGlobal(self.ui.txt_operator_com_rate.text())
        self.setHotelRepComToGlobal(self.ui.txt_rep_com_rate.text())
        self.setTotalComToGlobal(self.ui.txt_total_com_rate.text())
        self.calculateCompGuideCommission()
        self.calculateCompRepCommission()
        entered_guide_total = abs(GLOBAL_OPR_COM) + abs(GLOBAL_DRIVER_COM) + abs(GLOBAL_GUIDE_COM) + abs(GLOBAL_COMP_COM_GUIDE)
        entered_rep_total = abs(GLOBAL_OPR_COM) + abs(GLOBAL_DRIVER_COM) + abs(GLOBAL_REP_COM) + abs(GLOBAL_COMP_COM_REP)
        if (total != entered_guide_total or total != entered_rep_total):
            pyautogui.alert("Toplam Komisyon Oranı İle Girmiş Olduğunuz Komisyon Oranları Birbirini Tutmuyor!")
            return
        if (self.isExistInDb()):
            pyautogui.alert("Belirtilen Tarih Aralığında Aynı Mağaza ve Ürüne Ait Komisyon Zaten Tanımlı!")
            return
        else:
            if (utils.helper.fieldCheck(self.ui.txt_total_com_rate.text()) != True):
                self.ui.txt_total_com_rate.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_guide_com_rate.text()) != True):
                self.ui.txt_guide_com_rate.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_driver_com_rate.text()) != True):
                self.ui.txt_driver_com_rate.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_operator_com_rate.text()) != True):
                self.ui.txt_operator_com_rate.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_rep_com_rate.text()) != True):
                self.ui.txt_rep_com_rate.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_comp_rate_guide.text()) != True):
                self.ui.txt_comp_rate_guide.setText(str(0.0))

            if (utils.helper.fieldCheck(self.ui.txt_comp_rate_rep.text()) != True):
                self.ui.txt_comp_rate_rep.setText(str(0.0))


            if(shop_product.main_shop_product.GLOBAL_UPDATE == 1):
                ShopProduct = shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT
                ShopProduct.shopId = self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0))
                ShopProduct.shopName = self.ui.cmb_shop.currentText()
                ShopProduct.productId = self.product_model.data(self.product_model.index(self.ui.cmb_product.currentIndex(), 0))
                ShopProduct.productName = self.ui.cmb_product.currentText()
                ShopProduct.totalCommission = self.ui.txt_total_com_rate.text()
                ShopProduct.guideCommission = self.ui.txt_guide_com_rate.text()
                ShopProduct.driverCommission = self.ui.txt_driver_com_rate.text()
                ShopProduct.operatorCommission = self.ui.txt_operator_com_rate.text()
                ShopProduct.hotelRepCommission = self.ui.txt_rep_com_rate.text()
                ShopProduct.companyCommissionWithGuide = self.ui.txt_comp_rate_guide.text()
                ShopProduct.companyCommissionWithHotel = self.ui.txt_comp_rate_rep.text()
                ShopProduct.startDate = self.ui.dtp_start.date().toString("dd-MM-yyyy") + " 01:00:00"
                ShopProduct.finishDate = self.ui.dtp_finish.date().toString("dd-MM-yyyy") + " 01:00:00"

                result = pyautogui.confirm("Mağaza Ürünü Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    db_result = database.shop_product_db.updateShopProduct(ShopProduct)
                    if(db_result):
                        pyautogui.alert("Mağaza Ürünü Güncellendi!")
                        self.backToShopProductPanel()
                    else:pyautogui.alert("Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")
            else:
                ShopProduct = shop_product.obj_shop_product.ShopProduct(None,self.shop_model.data(self.shop_model.index(self.ui.cmb_shop.currentIndex(), 0)),self.ui.cmb_shop.currentText(),
                                                                        self.product_model.data(self.product_model.index(self.ui.cmb_product.currentIndex(), 0)),self.ui.cmb_product.currentText(),
                                                                        self.ui.txt_total_com_rate.text(),self.ui.txt_guide_com_rate.text(),self.ui.txt_driver_com_rate.text(),
                                                                        self.ui.txt_comp_rate_guide.text(),self.ui.txt_operator_com_rate.text(),self.ui.txt_rep_com_rate.text(),
                                                                        self.ui.txt_comp_rate_rep.text(),self.ui.dtp_start.date().toString("dd-MM-yyyy"),self.ui.dtp_finish.date().toString("dd-MM-yyyy"))
                result = pyautogui.confirm(ShopProduct.shopName + " Mağazasına " + ShopProduct.productName + "Ürünü Eklenecek. Komisyon Bilgileri : \n"
                                                                                                             "* Rehber Komisyon Tutarı   : " + ShopProduct.guideCommission+"\n"
                                                                                                             "* Şoför Komisyon Tutarı    : " + ShopProduct.driverCommission+"\n"
                                                                                                             "* Operatör Komisyon Tutarı : " + ShopProduct.operatorCommission+"\n"
                                                                                                             "* Otel Rep Komisyon Tutarı : " + ShopProduct.hotelRepCommission+"\n"
                                                                                                             "* Şirket Komisyon Tutarı (Kokartlı) : " + ShopProduct.companyCommissionWithGuide+"\n"
                                                                                                             "* Şirket Komisyon Tutarı (Rep) : " + ShopProduct.companyCommissionWithHotel+"\n"
                                                                                                             "* Toplam Komisyon Tutaru : " + ShopProduct.totalCommission+"\n"
                                                                                                             "Onaylıyor Musunuz ?")
                if (result == "OK"):
                    db_result = database.shop_product_db.addShopProduct(ShopProduct)
                    if (db_result):
                        pyautogui.alert("Ürün Mağazaya Eklendi!")
                        self.backToShopProductPanel()
                    else:
                        pyautogui.alert(
                            "Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = shop_product.ui_shop_product_def.ShopProductDefPanel()
        self.ui.setupUi(self)
        self.shop_model = self.ui.cmb_shop.model()
        self.product_model = self.ui.cmb_product.model()
        shop_list = self.getShopList()

        for i in shop_list:
            it1 = QtGui.QStandardItem(str(i[0]))
            it2 = QtGui.QStandardItem(str(i[2]))
            self.shop_model.appendRow((it1,it2))

        product_list = self.getProductList()

        itdef0 = QtGui.QStandardItem(str(0))
        itdef1 = QtGui.QStandardItem("Mağaza Seçin...")
        itdef2 = QtGui.QStandardItem("Ürün Seçin...")

        self.product_model.appendRow((itdef0,itdef2))
        self.shop_model.appendRow((itdef0,itdef1))
        if(product_list):
            for i in product_list:
                it1 = QtGui.QStandardItem(str(i[0]))
                it2 = QtGui.QStandardItem(str(i[1]))
                self.product_model.appendRow((it1, it2))

        self.ui.cmb_shop.setModel(self.shop_model)
        self.ui.cmb_shop.setModelColumn(1)

        self.ui.cmb_product.setModel(self.product_model)
        self.ui.cmb_product.setModelColumn(1)

        self.ui.cmb_shop.setCurrentIndex(self.ui.cmb_shop.findText("Mağaza Seçin..."))
        self.ui.cmb_product.setCurrentIndex(self.ui.cmb_product.findText("Ürün Seçin..."))
        self.ui.txt_total_com_rate.textChanged.connect(self.setTotalComToGlobal)

        self.ui.txt_guide_com_rate.textChanged.connect(self.setGuideComToGlobal)
        self.ui.txt_guide_com_rate.editingFinished.connect(self.calculateCompGuideCommission)

        self.ui.txt_driver_com_rate.textChanged.connect(self.setDriverComToGlobal)
        self.ui.txt_driver_com_rate.editingFinished.connect(self.calculateCompGuideCommission)
        self.ui.txt_driver_com_rate.editingFinished.connect(self.calculateCompRepCommission)

        self.ui.txt_operator_com_rate.textChanged.connect(self.setOperatorComToGlobal)
        self.ui.txt_operator_com_rate.editingFinished.connect(self.calculateCompGuideCommission)
        self.ui.txt_operator_com_rate.editingFinished.connect(self.calculateCompRepCommission)

        self.ui.txt_rep_com_rate.textChanged.connect(self.setHotelRepComToGlobal)
        self.ui.txt_rep_com_rate.editingFinished.connect(self.calculateCompRepCommission)

        if (shop_product.main_shop_product.GLOBAL_UPDATE == 1):
            self.ui.cmb_shop.setCurrentText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.shopName)
            self.ui.cmb_product.setCurrentText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.productName)
            self.ui.txt_total_com_rate.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.totalCommission)
            self.ui.txt_guide_com_rate.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.guideCommission)
            self.ui.txt_driver_com_rate.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.driverCommission)
            self.ui.txt_operator_com_rate.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.operatorCommission)
            self.ui.txt_rep_com_rate.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.hotelRepCommission)
            self.ui.txt_comp_rate_guide.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.companyCommissionWithGuide)
            self.ui.txt_comp_rate_rep.setText(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.companyCommissionWithHotel)
            self.ui.dtp_start.setDate(datetime.datetime.strptime(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.startDate,"%d-%m-%Y %H:%M:%S"))
            self.ui.dtp_finish.setDate(datetime.datetime.strptime(shop_product.main_shop_product.GLOBAL_OBJECT_SHOP_PRODUCT.finishDate,"%d-%m-%Y %H:%M:%S"))

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
            self.ui.d.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 158, 171, 255), stop:1 rgba(238, 242, 243, 255));border-radius:10px; ")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.d.setContentsMargins(10, 10, 10, 10)
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
        self.ui.dtp_start.setCorrectionMode(0)

        self.ui.dtp_finish.setCorrectionMode(0)

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: self.maximize_restore())

        # BACK TO HOME PANEL
        self.ui.btn_back.clicked.connect(lambda: self.backToShopProductPanel())

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        # ADD SHOP PRODUCT
        self.ui.btn_save.clicked.connect(lambda : self.saveToDb())

        self.ui.txt_comp_rate_rep.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_comp_rate_guide.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_rep_com_rate.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_driver_com_rate.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_guide_com_rate.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_operator_com_rate.setValidator(QtGui.QDoubleValidator())
        self.ui.txt_total_com_rate.setValidator(QtGui.QDoubleValidator())

        self.ui.txt_comp_rate_guide.setEnabled(False)
        self.ui.txt_comp_rate_rep.setEnabled(False)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopProductDefWindow()
    sys.exit(app.exec_())