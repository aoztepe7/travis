import sys

# GUI FILE
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

import opr.ui_operator
import opr.main_operator_def
import home.panel
import database.operator_db
import opr.obj_operator
import pyautogui
GLOBAL_STATE = 0
GLOBAL_SELECTED_OPERATOR = None
GLOBAL_OBJECT_OPERATOR = None
GLOBAL_UPDATE = 0

class OperatorWindow(QMainWindow):
    def openOperatorDefPanel(self):
        self.window = opr.main_operator_def.OperatorDefWindow()
        self.window.show()
        self.hide()

    def updateOperator(self):
        if(len(self.ui.tableWidget.selectedItems())==0):
            pyautogui.alert("Lütfen Güncellemek İstediğiniz Operatörü Seçiniz!")
        else:
            self.ui.tableWidget.setColumnHidden(0, False)
            item = self.ui.tableWidget.selectedItems()
            global GLOBAL_OBJECT_OPERATOR
            global GLOBAL_UPDATE
            GLOBAL_UPDATE = 1
            GLOBAL_OBJECT_OPERATOR = opr.obj_operator.Operator(item[0].text(), item[1].text(),item[2].text())
            self.ui.tableWidget.setColumnHidden(0, True)
            self.window = opr.main_operator_def.OperatorDefWindow()
            self.window.show()
            self.hide()

    def deleteSelectedOperator(self):
        self.ui.tableWidget.setColumnHidden(0, False)
        item = self.ui.tableWidget.selectedItems()
        global GLOBAL_SELECTED_OPERATOR
        GLOBAL_SELECTED_OPERATOR = item[0].text()
        self.ui.tableWidget.setColumnHidden(0, True)
        result = pyautogui.confirm("Seçilen Operatör Silinecek. Onaylıyor Musunuz?")
        if(result == "OK"):
            database.operator_db.deleteOperator(GLOBAL_SELECTED_OPERATOR)
            self.fill_table()
            pyautogui.alert("Operatör Silindi!")

    def backToMainPanel(self):
        self.window = home.panel.Panel()
        self.window.show()
        self.hide()

    def fill_table(self):
        operator_list =  database.operator_db.getOperatorList()
        if(operator_list):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(operator_list):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    self.ui.tableWidget.setItem(row,column, QTableWidgetItem(str(item)))

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = opr.ui_operator.OperatorPanel()
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
        self.ui.frame_move_2.mouseMoveEvent = moveWindow
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
            self.ui.drop_shadow_layout_2.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 158, 171, 255), stop:1 rgba(238, 242, 243, 255));border-radius:10px; ")
            self.ui.btn_maximize_2.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.drop_shadow_layout_2.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 158, 171, 255), stop:1 rgba(238, 242, 243, 255));border-radius:10px; ")
            self.ui.btn_maximize_2.setToolTip("Maximize")

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
        self.ui.btn_maximize_2.clicked.connect(lambda: self.maximize_restore())

        # BACK TO HOME PANEL
        self.ui.btn_back_2.clicked.connect(lambda: self.backToMainPanel())

        # MINIMIZE
        self.ui.btn_minimize_2.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close_2.clicked.connect(lambda: self.close())

        # DELETE
        self.ui.btn_delete.clicked.connect(lambda: self.deleteSelectedOperator())

        self.ui.btn_update.clicked.connect(lambda: self.updateOperator())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip_2)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        #HIDE FIRST COLUMN
        self.ui.tableWidget.setColumnHidden(0,True)

        # OPEN ADD NEW AREA PANEL
        self.ui.btn_add.clicked.connect(lambda : self.openOperatorDefPanel())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OperatorWindow()
    sys.exit(app.exec_())