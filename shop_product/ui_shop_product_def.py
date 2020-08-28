# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_shop_product_def.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ShopProductDefPanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 566)
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
        self.d = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.d.setContentsMargins(5, 0, 5, 0)
        self.d.setSpacing(0)
        self.d.setObjectName("d")
        self.frame_3 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setStyleSheet("background-color:none,")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.frame_3)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_title.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        self.label_title.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(50, 130, 184);")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_3.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_move = QtWidgets.QFrame(self.frame_3)
        self.frame_move.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_move.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_move.setObjectName("frame_move")
        self.horizontalLayout.addWidget(self.frame_move)
        self.frame_btns = QtWidgets.QFrame(self.frame_3)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 40))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns)
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
        self.d.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_4.setStyleSheet("background-color:none,")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmb_shop = QtWidgets.QComboBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.cmb_shop.setFont(font)
        self.cmb_shop.setStyleSheet("QComboBox{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color: white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.cmb_shop.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cmb_shop.setObjectName("cmb_shop")
        self.cmb_shop.addItem("")
        self.horizontalLayout_3.addWidget(self.cmb_shop)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cmb_product = QtWidgets.QComboBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.cmb_product.setFont(font)
        self.cmb_product.setStyleSheet("QComboBox{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color: white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.cmb_product.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cmb_product.setObjectName("cmb_product")
        self.cmb_product.addItem("")
        self.horizontalLayout_5.addWidget(self.cmb_product)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txt_total_com_rate = QtWidgets.QLineEdit(self.frame_7)
        self.txt_total_com_rate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_total_com_rate.setFont(font)
        self.txt_total_com_rate.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_total_com_rate.setText("")
        self.txt_total_com_rate.setObjectName("txt_total_com_rate")
        self.horizontalLayout_6.addWidget(self.txt_total_com_rate)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txt_guide_com_rate = QtWidgets.QLineEdit(self.frame_8)
        self.txt_guide_com_rate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_guide_com_rate.setFont(font)
        self.txt_guide_com_rate.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_guide_com_rate.setText("")
        self.txt_guide_com_rate.setObjectName("txt_guide_com_rate")
        self.horizontalLayout_7.addWidget(self.txt_guide_com_rate)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.txt_driver_com_rate = QtWidgets.QLineEdit(self.frame_10)
        self.txt_driver_com_rate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_driver_com_rate.setFont(font)
        self.txt_driver_com_rate.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_driver_com_rate.setText("")
        self.txt_driver_com_rate.setObjectName("txt_driver_com_rate")
        self.horizontalLayout_8.addWidget(self.txt_driver_com_rate)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.txt_operator_com_rate = QtWidgets.QLineEdit(self.frame_11)
        self.txt_operator_com_rate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_operator_com_rate.setFont(font)
        self.txt_operator_com_rate.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_operator_com_rate.setText("")
        self.txt_operator_com_rate.setObjectName("txt_operator_com_rate")
        self.horizontalLayout_9.addWidget(self.txt_operator_com_rate)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.txt_rep_com_rate = QtWidgets.QLineEdit(self.frame_12)
        self.txt_rep_com_rate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_rep_com_rate.setFont(font)
        self.txt_rep_com_rate.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_rep_com_rate.setText("")
        self.txt_rep_com_rate.setObjectName("txt_rep_com_rate")
        self.horizontalLayout_10.addWidget(self.txt_rep_com_rate)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.txt_comp_rate_guide = QtWidgets.QLineEdit(self.frame_13)
        self.txt_comp_rate_guide.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_comp_rate_guide.setFont(font)
        self.txt_comp_rate_guide.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_comp_rate_guide.setText("")
        self.txt_comp_rate_guide.setObjectName("txt_comp_rate_guide")
        self.horizontalLayout_11.addWidget(self.txt_comp_rate_guide)
        self.verticalLayout_2.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.txt_comp_rate_rep = QtWidgets.QLineEdit(self.frame_14)
        self.txt_comp_rate_rep.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txt_comp_rate_rep.setFont(font)
        self.txt_comp_rate_rep.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.txt_comp_rate_rep.setText("")
        self.txt_comp_rate_rep.setObjectName("txt_comp_rate_rep")
        self.horizontalLayout_12.addWidget(self.txt_comp_rate_rep)
        self.verticalLayout_2.addWidget(self.frame_14)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.dtp_start = QtWidgets.QDateEdit(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dtp_start.setFont(font)
        self.dtp_start.setStyleSheet("QDateEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.dtp_start.setObjectName("dtp_start")
        self.horizontalLayout_14.addWidget(self.dtp_start)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_17 = QtWidgets.QFrame(self.frame_4)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.dtp_finish = QtWidgets.QDateEdit(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dtp_finish.setFont(font)
        self.dtp_finish.setStyleSheet("QDateEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom:1px solid #717072\n"
"}")
        self.dtp_finish.setObjectName("dtp_finish")
        self.horizontalLayout_15.addWidget(self.dtp_finish)
        self.verticalLayout_2.addWidget(self.frame_17)
        self.d.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setStyleSheet("background-color:none")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_save = QtWidgets.QPushButton(self.frame)
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
        self.horizontalLayout_13.addWidget(self.btn_save)
        self.btn_back = QtWidgets.QPushButton(self.frame)
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
        self.horizontalLayout_13.addWidget(self.btn_back)
        self.d.addWidget(self.frame)
        self.frame_15 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_15.setStyleSheet("background-color:none")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.d.addWidget(self.frame_15)
        self.frame_2 = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color:none,")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_16 = QtWidgets.QFrame(self.frame_2)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_2.addWidget(self.frame_16)
        self.frame_grip = QtWidgets.QFrame(self.frame_2)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.d.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cmb_shop.setCurrentIndex(0)
        self.cmb_product.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<strong>TRAVIS </strong> - Mağaza Ürünü Oluşturma"))
        self.cmb_shop.setToolTip(_translate("MainWindow", "MAĞAZA"))
        self.cmb_shop.setCurrentText(_translate("MainWindow", "MAĞAZA"))
        self.cmb_shop.setItemText(0, _translate("MainWindow", "MAĞAZA"))
        self.cmb_product.setToolTip(_translate("MainWindow", "ÜRÜN"))
        self.cmb_product.setCurrentText(_translate("MainWindow", "ÜRÜN"))
        self.cmb_product.setItemText(0, _translate("MainWindow", "ÜRÜN"))
        self.txt_total_com_rate.setToolTip(_translate("MainWindow", "TOPLAM KOMİSYON ORANI"))
        self.txt_total_com_rate.setPlaceholderText(_translate("MainWindow", "TOPLAM KOMİSYON ORANI"))
        self.txt_guide_com_rate.setToolTip(_translate("MainWindow", "REHBER KOMİSYON ORANI"))
        self.txt_guide_com_rate.setPlaceholderText(_translate("MainWindow", "REHBER KOMİSYON ORANI"))
        self.txt_driver_com_rate.setToolTip(_translate("MainWindow", "ŞOFÖR KOMİSYON ORANI"))
        self.txt_driver_com_rate.setPlaceholderText(_translate("MainWindow", "ŞOFÖR KOMİSYON ORANI"))
        self.txt_operator_com_rate.setToolTip(_translate("MainWindow", "OPERATÖR KOMİSYON ORANI"))
        self.txt_operator_com_rate.setPlaceholderText(_translate("MainWindow", "OPERATÖR KOMİSYON ORANI"))
        self.txt_rep_com_rate.setToolTip(_translate("MainWindow", "OTEL REP KOMİSYON ORANI"))
        self.txt_rep_com_rate.setPlaceholderText(_translate("MainWindow", "OTEL REP KOMİSYON ORANI"))
        self.txt_comp_rate_guide.setToolTip(_translate("MainWindow", "KOKARTLI İLE ŞİRKET KOMİSYONU"))
        self.txt_comp_rate_guide.setPlaceholderText(_translate("MainWindow", "KOKARTLI İLE ŞİRKET KOMİSYON ORANI"))
        self.txt_comp_rate_rep.setToolTip(_translate("MainWindow", "OTEL REHBERİ İLE ŞİRKET KOMİSYONU"))
        self.txt_comp_rate_rep.setPlaceholderText(_translate("MainWindow", "OTEL REP İLE ŞİRKET KOMİSYON ORANI"))
        self.dtp_start.setToolTip(_translate("MainWindow", "BAŞLANGIÇ TARİHİ"))
        self.dtp_start.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.dtp_finish.setToolTip(_translate("MainWindow", "BİTİŞ TARİHİ"))
        self.dtp_finish.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet"))
        self.btn_back.setText(_translate("MainWindow", "Geri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ShopProductDefPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

