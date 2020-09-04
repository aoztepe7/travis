import sys
import platform

# GUI FILE
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip

import home.home_panel
import area.main_area
import opr.main_operator
import guide.main_guide
import shop.main_shop
import product.main_product
import shop_product.main_shop_product
import shop_sale.main_shop_sale
import reports.shop_report.main_shop_report
GLOBAL_STATE = 0

class Panel(QMainWindow):
    def openShopSalePanel(self):
        self.window = shop_sale.main_shop_sale.ShopSaleWindow()
        self.window.show()
        self.hide()
    def openAreaPanel(self):
        self.window = area.main_area.AreaWindow()
        self.window.show()
        self.hide()

    def openGuidePanel(self):
        self.window = guide.main_guide.GuideWindow()
        self.window.show()
        self.hide()

    def openOperatorPanel(self):
        self.window = opr.main_operator.OperatorWindow()
        self.window.show()
        self.hide()

    def openShopPanel(self):
        self.window = shop.main_shop.ShopWindow()
        self.window.show()
        self.hide()

    def openProductPanel(self):
        self.window = product.main_product.ProductWindow()
        self.window.show()
        self.hide()

    def openShopProductPanel(self):
        self.window = shop_product.main_shop_product.ShopProductWindow()
        self.window.show()
        self.hide()

    def openShopReport(self):
        self.window = reports.shop_report.main_shop_report.ShopReportWindow()
        self.window.show()
        self.hide()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = home.home_panel.Ui_HomePanel()
        self.ui.setupUi(self)

        def moveWindow(event):
            # RESTORE BEFORE MOVE
            #if self.returnStatus() == 1:
                #self.maximize_restore()

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

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # AREA PANEL
        self.ui.btn_area.clicked.connect(lambda: self.openAreaPanel())

        # GUIDE PANEL
        self.ui.btn_guide.clicked.connect(lambda: self.openGuidePanel())

        # OPERATOR PANEL
        self.ui.btn_operator.clicked.connect(lambda: self.openOperatorPanel())

        # SHOP PANEL
        self.ui.btn_shop.clicked.connect(lambda: self.openShopPanel())

        # PRODUCT PANEL
        self.ui.btn_product.clicked.connect(lambda: self.openProductPanel())

        # SHOP PRODUCT PANEL
        self.ui.btn_shop_product.clicked.connect(lambda: self.openShopProductPanel())

        # SHOP SALE PANEL
        self.ui.btn_sale.clicked.connect(lambda: self.openShopSalePanel())

        self.ui.btn_maximize.setEnabled(False)
        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        self.ui.btn_shop_report.clicked.connect(lambda: self.openShopReport())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Panel()
    sys.exit(app.exec_())