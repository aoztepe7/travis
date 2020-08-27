# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_operator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class OperatorPanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 158, 171, 255), stop:1 rgba(238, 242, 243, 255));\n"
"border-radius:10px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.drop_shadow_layout_2 = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout_2.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout_2.setSpacing(0)
        self.drop_shadow_layout_2.setObjectName("drop_shadow_layout_2")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_bar.setFont(font)
        self.title_bar.setStyleSheet("background-color:none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setContentsMargins(5, 4, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_title_2 = QtWidgets.QFrame(self.title_bar)
        self.frame_title_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_title_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_title_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_2.setObjectName("frame_title_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_title_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_title_2 = QtWidgets.QLabel(self.frame_title_2)
        self.label_title_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_title_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet("color: rgb(50, 130, 184);")
        self.label_title_2.setIndent(0)
        self.label_title_2.setObjectName("label_title_2")
        self.verticalLayout_6.addWidget(self.label_title_2)
        self.horizontalLayout_3.addWidget(self.frame_title_2)
        self.frame_move_2 = QtWidgets.QFrame(self.title_bar)
        self.frame_move_2.setMinimumSize(QtCore.QSize(45, 15))
        self.frame_move_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_move_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_move_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_move_2.setObjectName("frame_move_2")
        self.horizontalLayout_3.addWidget(self.frame_move_2)
        self.frame_btns_2 = QtWidgets.QFrame(self.title_bar)
        self.frame_btns_2.setMaximumSize(QtCore.QSize(100, 40))
        self.frame_btns_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_2.setObjectName("frame_btns_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_btns_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_minimize_2 = QtWidgets.QPushButton(self.frame_btns_2)
        self.btn_minimize_2.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize_2.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize_2.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color:rgb(255,170,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(255,170,0,150);\n"
"}")
        self.btn_minimize_2.setText("")
        self.btn_minimize_2.setObjectName("btn_minimize_2")
        self.horizontalLayout_6.addWidget(self.btn_minimize_2)
        self.btn_maximize_2 = QtWidgets.QPushButton(self.frame_btns_2)
        self.btn_maximize_2.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize_2.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize_2.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color:rgb(85,255,127);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(85,255,127,150);\n"
"}\n"
"")
        self.btn_maximize_2.setText("")
        self.btn_maximize_2.setObjectName("btn_maximize_2")
        self.horizontalLayout_6.addWidget(self.btn_maximize_2)
        self.btn_close_2 = QtWidgets.QPushButton(self.frame_btns_2)
        self.btn_close_2.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close_2.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close_2.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0,150);\n"
"}\n"
"")
        self.btn_close_2.setText("")
        self.btn_close_2.setObjectName("btn_close_2")
        self.horizontalLayout_6.addWidget(self.btn_close_2)
        self.horizontalLayout_3.addWidget(self.frame_btns_2)
        self.drop_shadow_layout_2.addWidget(self.title_bar)
        self.frame_6 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setStyleSheet("background-color:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_add = QtWidgets.QPushButton(self.frame_6)
        self.btn_add.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton {    \n"
"  color: rgb(246, 244, 230);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 150), stop:1 rgba(61, 114, 180, 150));\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_7.addWidget(self.btn_add)
        self.btn_update = QtWidgets.QPushButton(self.frame_6)
        self.btn_update.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_update.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("QPushButton {    \n"
"  color: rgb(246, 244, 230);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 150), stop:1 rgba(61, 114, 180, 150));\n"
"}")
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_7.addWidget(self.btn_update)
        self.btn_delete = QtWidgets.QPushButton(self.frame_6)
        self.btn_delete.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_delete.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("QPushButton {    \n"
"  color: rgb(246, 244, 230);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 150), stop:1 rgba(61, 114, 180, 150));\n"
"}")
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_7.addWidget(self.btn_delete)
        spacerItem = QtWidgets.QSpacerItem(367, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.btn_back_2 = QtWidgets.QPushButton(self.frame_6)
        self.btn_back_2.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_back_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_back_2.setFont(font)
        self.btn_back_2.setStyleSheet("QPushButton {    \n"
"  color: rgb(246, 244, 230);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 150), stop:1 rgba(61, 114, 180, 150));\n"
"}")
        self.btn_back_2.setObjectName("btn_back_2")
        self.horizontalLayout_7.addWidget(self.btn_back_2)
        self.drop_shadow_layout_2.addWidget(self.frame_6)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setStyleSheet("background-color:none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.content_bar)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"    background-color: transparent;\n"
"    border-radius:10px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.drop_shadow_layout_2.addWidget(self.content_bar)
        self.frame_label_credits = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_label_credits.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_credits.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_label_credits)
        self.frame_7.setStyleSheet("background-color:none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.frame_grip_2 = QtWidgets.QFrame(self.frame_label_credits)
        self.frame_grip_2.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip_2.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip_2.setStyleSheet("padding:5px;background-color:none;")
        self.frame_grip_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip_2.setObjectName("frame_grip_2")
        self.horizontalLayout_8.addWidget(self.frame_grip_2)
        self.drop_shadow_layout_2.addWidget(self.frame_label_credits)
        self.verticalLayout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_2.setText(_translate("MainWindow", "<strong>TRAVIS </strong> - Operatörler"))
        self.btn_add.setText(_translate("MainWindow", "Yeni Ekle"))
        self.btn_update.setText(_translate("MainWindow", "Güncelle"))
        self.btn_delete.setText(_translate("MainWindow", "Sil"))
        self.btn_back_2.setText(_translate("MainWindow", "Geri"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ADI"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ŞEF KOMİSYON ORANI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = OperatorPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

