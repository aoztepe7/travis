# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_guide_def.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class GuideDefPanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 321)
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
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.title_frame = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title_frame.setStyleSheet("background-color:none;")
        self.title_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_frame)
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(50, 130, 184);")
        self.label_title.setIndent(0)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_3.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_move = QtWidgets.QFrame(self.title_frame)
        self.frame_move.setMinimumSize(QtCore.QSize(45, 15))
        self.frame_move.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_move.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_move.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_move.setObjectName("frame_move")
        self.horizontalLayout.addWidget(self.frame_move)
        self.frame_btns = QtWidgets.QFrame(self.title_frame)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 40))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color:rgb(255,170,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(255,170,0,150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_4.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color:rgb(85,255,127);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(85,255,127,150);\n"
"}\n"
"")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_4.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0,150);\n"
"}\n"
"")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.drop_shadow_layout.addWidget(self.title_frame)
        self.title_frame_2 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_frame_2.setStyleSheet("background-color:none;")
        self.title_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame_2.setObjectName("title_frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.title_frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.title_frame_2)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txt_fullname = QtWidgets.QLineEdit(self.frame)
        self.txt_fullname.setMinimumSize(QtCore.QSize(150, 0))
        self.txt_fullname.setToolTip("Adı Soyadı")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_fullname.setFont(font)
        self.txt_fullname.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_fullname.setText("")
        self.txt_fullname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txt_fullname.setObjectName("txt_fullname")
        self.verticalLayout_4.addWidget(self.txt_fullname)
        self.txt_phone = QtWidgets.QLineEdit(self.frame)
        self.txt_phone.setMinimumSize(QtCore.QSize(150, 0))
        self.txt_phone.setToolTip("Telefon Numarası")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_phone.setFont(font)
        self.txt_phone.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_phone.setText("")
        self.txt_phone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txt_phone.setObjectName("txt_phone")
        self.verticalLayout_4.addWidget(self.txt_phone)
        self.txt_mail = QtWidgets.QLineEdit(self.frame)
        self.txt_mail.setMinimumSize(QtCore.QSize(150, 0))
        self.txt_mail.setToolTip("E-Posta Adresi")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_mail.setFont(font)
        self.txt_mail.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_mail.setText("")
        self.txt_mail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txt_mail.setObjectName("txt_mail")
        self.verticalLayout_4.addWidget(self.txt_mail)
        self.cmb_type = QtWidgets.QComboBox(self.frame)
        self.cmb_type.setToolTip("Rehberlik Türü")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.cmb_type.setFont(font)
        self.cmb_type.setStyleSheet("QComboBox{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.cmb_type.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cmb_type.setObjectName("cmb_type")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.verticalLayout_4.addWidget(self.cmb_type)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.title_frame_2)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_save = QtWidgets.QPushButton(self.frame_5)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton {    \n"
"  color: rgb(246, 244, 230);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 150), stop:1 rgba(61, 114, 180, 150));\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_5.addWidget(self.btn_save)
        self.btn_back = QtWidgets.QPushButton(self.frame_5)
        self.btn_back.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_back.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton {    \n"
"  color: rgb(246, 244, 230);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 255), stop:1 rgba(61, 114, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 82, 82, 150), stop:1 rgba(61, 114, 180, 150));\n"
"}")
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_5.addWidget(self.btn_back)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.drop_shadow_layout.addWidget(self.title_frame_2)
        self.title_frame_3 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title_frame_3.setStyleSheet("background-color:none;")
        self.title_frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame_3.setObjectName("title_frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.title_frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.title_frame_3)
        self.frame_3.setStyleSheet("background-color:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_grip = QtWidgets.QFrame(self.title_frame_3)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding:5px;background-color:none;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.drop_shadow_layout.addWidget(self.title_frame_3)
        self.verticalLayout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<strong>TRAVIS </strong> - Yeni Rehber"))
        self.txt_fullname.setPlaceholderText(_translate("MainWindow", "REHBER ADI SOYADI"))
        self.txt_phone.setPlaceholderText(_translate("MainWindow", "TELEFONU"))
        self.txt_mail.setPlaceholderText(_translate("MainWindow", "E-POSTA ADRESİ"))
        self.cmb_type.setItemText(0, _translate("MainWindow", "REHBERLİK TÜRÜ"))
        self.cmb_type.setItemText(1, _translate("MainWindow", "BAĞLI REHBER"))
        self.cmb_type.setItemText(2, _translate("MainWindow", "OTEL REHBERİ"))
        self.cmb_type.setItemText(3, _translate("MainWindow", "KİRALIK REHBER"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet"))
        self.btn_back.setText(_translate("MainWindow", "Geri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GuideDefPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

