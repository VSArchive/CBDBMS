# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Parent_displayZDVYTY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(751, 466)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 210, 93);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-220, 0, 441, 471))
        self.line.setStyleSheet(u"background-color: rgb(21, 82, 93);\n"
                                "background-color: rgb(21, 84, 93);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 111, 121))
        self.label.setStyleSheet(u"\n"
                                 "background-image: url(assets/logo3_1.png);")
        self.label.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.Approval_btn = QPushButton(self.centralwidget)
        self.Approval_btn.setObjectName(u"Approval_btn")
        self.Approval_btn.setGeometry(QRect(10, 160, 201, 41))
        self.Approval_btn.setStyleSheet(u"QPushButton {\n"
                                        "font: italic 18pt \"Goudy Old Style\";\n"
                                        "background-color: rgb(255, 212, 93);\n"
                                        "color: rgb(21, 82, 93);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color:rgb(14, 54, 61);\n"
                                        "color:rgb(255,212,93);\n"
                                        "}")
        self.balance_btn = QPushButton(self.centralwidget)
        self.balance_btn.setObjectName(u"balance_btn")
        self.balance_btn.setGeometry(QRect(10, 210, 201, 41))
        self.balance_btn.setStyleSheet(u"QPushButton {\n"
                                       "font: italic 18pt \"Goudy Old Style\";\n"
                                       "background-color: rgb(255, 212, 93);\n"
                                       "color: rgb(21, 82, 93);\n"
                                       "border: 1px solid;\n"
                                       "border-radius: 15px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background-color:rgb(14, 54, 61);\n"
                                       "color:rgb(255,212,93);\n"
                                       "}")
        self.transfer_btn = QPushButton(self.centralwidget)
        self.transfer_btn.setObjectName(u"transfer_btn")
        self.transfer_btn.setGeometry(QRect(10, 260, 201, 41))
        self.transfer_btn.setStyleSheet(u"QPushButton {\n"
                                        "font: italic 18pt \"Goudy Old Style\";\n"
                                        "background-color: rgb(255, 212, 93);\n"
                                        "color: rgb(21, 82, 93);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color:rgb(14, 54, 61);\n"
                                        "color:rgb(255,212,93);\n"
                                        "}")
        self.transaction_btn = QPushButton(self.centralwidget)
        self.transaction_btn.setObjectName(u"transaction_btn")
        self.transaction_btn.setGeometry(QRect(10, 310, 201, 41))
        self.transaction_btn.setStyleSheet(u"QPushButton {\n"
                                           "font: italic 18pt \"Goudy Old Style\";\n"
                                           "background-color: rgb(255, 212, 93);\n"
                                           "color: rgb(21, 82, 93);\n"
                                           "border: 1px solid;\n"
                                           "border-radius: 15px;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background-color:rgb(14, 54, 61);\n"
                                           "color:rgb(255,212,93);\n"
                                           "}")
        self.deposit_btn = QPushButton(self.centralwidget)
        self.deposit_btn.setObjectName(u"deposit_btn")
        self.deposit_btn.setGeometry(QRect(10, 360, 201, 41))
        self.deposit_btn.setStyleSheet(u"QPushButton {\n"
                                       "font: italic 18pt \"Goudy Old Style\";\n"
                                       "background-color: rgb(255, 212, 93);\n"
                                       "color: rgb(21, 82, 93);\n"
                                       "border: 1px solid;\n"
                                       "border-radius: 15px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background-color:rgb(14, 54, 61);\n"
                                       "color:rgb(255,212,93);\n"
                                       "}")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 0, 231, 41))
        self.label_7.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 16pt \"Goudy Old Style\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 40, 231, 41))
        self.label_8.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 16pt \"Goudy Old Style\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(470, 0, 231, 41))
        self.label_9.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 16pt \"Goudy Old Style\";")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(460, 40, 231, 41))
        self.label_10.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 16pt \"Goudy Old Style\";")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(229, 100, 521, 361))
        self.Approval_message_page = QWidget()
        self.Approval_message_page.setObjectName(u"Approval_message_page")
        self.msg_list_view = QListView(self.Approval_message_page)
        self.msg_list_view.setObjectName(u"msg_list_view")
        self.msg_list_view.setGeometry(QRect(30, 40, 461, 281))
        self.stackedWidget.addWidget(self.Approval_message_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.Approval_btn.setText(QCoreApplication.translate("MainWindow", u"Approval Messages", None))
        self.balance_btn.setText(QCoreApplication.translate("MainWindow", u"Balance Overview", None))
        self.transfer_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.deposit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit transaction limit", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Parent Account Number :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Child Account Number :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"9638527445", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"2360588915", None))
    # retranslateUi
