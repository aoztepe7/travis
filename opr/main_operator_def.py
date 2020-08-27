import sys
# GUI FILE
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import opr.ui_operator_def
import opr.main_operator
import database.operator_db
import pyautogui
import opr.obj_operator
import utils.helper

GLOBAL_STATE = 0
GLOBAL_UPDATE = 0

class OperatorDefWindow(QMainWindow):
    def backToOperatorPanel(self):
        self.window = opr.main_operator.OperatorWindow()
        self.window.show()
        self.hide()

    def saveToDb(self):
        if (utils.helper.fieldCheck(self.ui.txt_name.text()) != True):
            pyautogui.alert("Operatör Adı Boş Olamaz!")
        else:
            if (utils.helper.fieldCheck(self.ui.txt_chief_amount.text()) != True):
                self.ui.txt_chief_amount.setText(str(0.0))
            if(opr.main_operator.GLOBAL_UPDATE == 1):
                Operator = opr.main_operator.GLOBAL_OBJECT_OPERATOR
                Operator.name = self.ui.txt_name.text()
                Operator.chiefCommissionAmount = self.ui.txt_chief_amount.text()
                result = pyautogui.confirm("Operatör Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    db_result = database.operator_db.updateOperator(Operator)
                    if(db_result):
                        pyautogui.alert("Operatör Güncellendi!")
                        self.backToOperatorPanel()
                    else:pyautogui.alert("Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")
            else:
                Operator = opr.obj_operator.Operator(None,self.ui.txt_name.text(),self.ui.txt_chief_amount.text())
                result = pyautogui.confirm(Operator.name + " Operatörü Eklenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    db_result = database.operator_db.addOperator(Operator)
                    if (db_result):
                        pyautogui.alert("Operatör Eklendi!")
                        self.backToOperatorPanel()
                    else:
                        pyautogui.alert(
                            "Kayıt Sırasında Bir Hata Oluştu \n *Veritabanı Bağlantısı Kopmuş Olabilir \n *Aynı İsimde Veri Daha Önce Eklenmiş Olabilir")

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = opr.ui_operator_def.OperatorDefWindow()
        self.ui.setupUi(self)
        self.ui.txt_chief_amount.setValidator(QtGui.QDoubleValidator())
        if (opr.main_operator.GLOBAL_UPDATE == 1):
            self.ui.txt_name.setText(opr.main_operator.GLOBAL_OBJECT_OPERATOR.name)
            self.ui.txt_chief_amount.setText(opr.main_operator.GLOBAL_OBJECT_OPERATOR.chiefCommissionAmount)

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
        self.ui.btn_back.clicked.connect(lambda: self.backToOperatorPanel())

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        # ADD AREA
        self.ui.btn_save.clicked.connect(lambda : self.saveToDb())


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OperatorDefWindow()
    sys.exit(app.exec_())