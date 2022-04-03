# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Child_menu_pageQKwMnV.ui'
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
        MainWindow.resize(754, 465)
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
        self.label.setGeometry(QRect(60, 0, 111, 121))
        self.label.setStyleSheet(u"background-image: url(assets/logo3_1.png);")
        self.label.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.transaction_btn = QPushButton(self.centralwidget)
        self.transaction_btn.setObjectName(u"transaction_btn")
        self.transaction_btn.setGeometry(QRect(10, 250, 201, 41))
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
        self.withdraw_btn = QPushButton(self.centralwidget)
        self.withdraw_btn.setObjectName(u"withdraw_btn")
        self.withdraw_btn.setGeometry(QRect(10, 300, 201, 41))
        self.withdraw_btn.setStyleSheet(u"QPushButton {\n"
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
        self.transfer_btn.setGeometry(QRect(10, 350, 201, 41))
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
        self.deposit_btn = QPushButton(self.centralwidget)
        self.deposit_btn.setObjectName(u"deposit_btn")
        self.deposit_btn.setGeometry(QRect(10, 400, 201, 41))
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 140, 181, 41))
        self.label_2.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
                                   "color: rgb(255, 210, 93);\n"
                                   "font: 75 24pt \"Goudy Old Style\";")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 110, 521, 351))
        self.transaction_page = QWidget()
        self.transaction_page.setObjectName(u"transaction_page")
        self.label_3 = QLabel(self.transaction_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 20, 371, 41))
        self.label_3.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
                                   "color: rgb(255, 210, 93);\n"
                                   "font: 75 24pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.transaction_page)
        self.withdraw_page = QWidget()
        self.withdraw_page.setObjectName(u"withdraw_page")
        self.label_4 = QLabel(self.withdraw_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 30, 161, 41))
        self.label_4.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
                                   "color: rgb(255, 210, 93);\n"
                                   "font: 75 24pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.withdraw_page)
        self.depost_page = QWidget()
        self.depost_page.setObjectName(u"depost_page")
        self.label_5 = QLabel(self.depost_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 180, 101, 41))
        self.label_5.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
                                   "color: rgb(255, 210, 93);\n"
                                   "font: 75 24pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.depost_page)
        self.transfer_page = QWidget()
        self.transfer_page.setObjectName(u"transfer_page")
        self.stackedWidget_2 = QStackedWidget(self.transfer_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(20, 69, 481, 251))
        self.verify_account_page = QWidget()
        self.verify_account_page.setObjectName(u"verify_account_page")
        self.label_6 = QLabel(self.verify_account_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 211, 41))
        self.label_6.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.acc_edt = QLineEdit(self.verify_account_page)
        self.acc_edt.setObjectName(u"acc_edt")
        self.acc_edt.setGeometry(QRect(260, 60, 181, 31))
        self.verify_btn = QPushButton(self.verify_account_page)
        self.verify_btn.setObjectName(u"verify_btn")
        self.verify_btn.setGeometry(QRect(130, 140, 201, 41))
        self.verify_btn.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget_2.addWidget(self.verify_account_page)
        self.amount_enter_page = QWidget()
        self.amount_enter_page.setObjectName(u"amount_enter_page")
        self.label_13 = QLabel(self.amount_enter_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 50, 81, 21))
        self.label_13.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.Name_edt = QLineEdit(self.amount_enter_page)
        self.Name_edt.setObjectName(u"Name_edt")
        self.Name_edt.setGeometry(QRect(240, 50, 161, 21))
        self.label_14 = QLabel(self.amount_enter_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 90, 121, 21))
        self.label_14.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.Name_edt_2 = QLineEdit(self.amount_enter_page)
        self.Name_edt_2.setObjectName(u"Name_edt_2")
        self.Name_edt_2.setGeometry(QRect(240, 90, 161, 21))
        self.Name_edt_3 = QLineEdit(self.amount_enter_page)
        self.Name_edt_3.setObjectName(u"Name_edt_3")
        self.Name_edt_3.setGeometry(QRect(240, 130, 161, 21))
        self.label_15 = QLabel(self.amount_enter_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(90, 130, 141, 21))
        self.label_15.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.confirm_btn = QPushButton(self.amount_enter_page)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(150, 190, 201, 41))
        self.confirm_btn.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget_2.addWidget(self.amount_enter_page)
        self.Confirm_amount_page = QWidget()
        self.Confirm_amount_page.setObjectName(u"Confirm_amount_page")
        self.label_12 = QLabel(self.Confirm_amount_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 60, 131, 21))
        self.label_12.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.lineEdit = QLineEdit(self.Confirm_amount_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 60, 121, 21))
        self.label_16 = QLabel(self.Confirm_amount_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(80, 100, 131, 21))
        self.label_16.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.lineEdit_2 = QLineEdit(self.Confirm_amount_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 100, 121, 21))
        self.Transfer_btn = QPushButton(self.Confirm_amount_page)
        self.Transfer_btn.setObjectName(u"Transfer_btn")
        self.Transfer_btn.setGeometry(QRect(130, 160, 201, 41))
        self.Transfer_btn.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget_2.addWidget(self.Confirm_amount_page)
        self.label_11 = QLabel(self.transfer_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 20, 151, 41))
        self.label_11.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 20pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.transfer_page)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 10, 201, 41))
        self.label_7.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 20pt \"Goudy Old Style\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 10, 201, 41))
        self.label_8.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 20pt \"Goudy Old Style\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 50, 231, 41))
        self.label_9.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                   "font: 75 20pt \"Goudy Old Style\";")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(480, 50, 201, 41))
        self.label_10.setStyleSheet(u"color: rgb(21, 84, 93);\n"
                                    "font: 75 20pt \"Goudy Old Style\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.withdraw_btn.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.transfer_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.deposit_btn.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pavan Kumar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION HISTORY", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Withdrawal", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter Account Number", None))
        self.verify_btn.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Re- Enter Amount", None))
        self.confirm_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Transfer_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TRANSFER", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Available Balance :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rs. 20000", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Amount used today :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Rs. 1000", None))
    # retranslateUi
