from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from backend import signup


class Create_account(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(727, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(21, 84, 93);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 0, 131, 121))
        self.label.setStyleSheet(u"background-image: url(assets/logo3_1.png);")
        self.label.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.transaction_btn = QPushButton(self.centralwidget)
        self.transaction_btn.setObjectName(u"transaction_btn")
        self.transaction_btn.setGeometry(QRect(80, 130, 231, 41))
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
        self.transaction_btn_2 = QPushButton(self.centralwidget)
        self.transaction_btn_2.setObjectName(u"transaction_btn_2")
        self.transaction_btn_2.setGeometry(QRect(440, 130, 231, 41))
        self.transaction_btn_2.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 200, 721, 361))

        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.label_15 = QLabel(self.Home_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(230, 30, 291, 71))
        self.label_15.setStyleSheet(u"font: 75 22pt \"Goudy Old Style\";\n"
                                    "color: rgb(255, 212, 93);")
        self.stackedWidget.addWidget(self.Home_page)
        self.Parent_page = QWidget()
        self.Parent_page.setObjectName(u"Parent_page")

        self.label_2 = QLabel(self.Parent_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 80, 91, 21))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.label_4 = QLabel(self.Parent_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 160, 151, 21))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.label_5 = QLabel(self.Parent_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 200, 91, 21))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.label_6 = QLabel(self.Parent_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 240, 91, 21))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.label_7 = QLabel(self.Parent_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 280, 151, 21))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.Name_edt = QLineEdit(self.Parent_page)
        self.Name_edt.setObjectName(u"Name_edt")
        self.Name_edt.setGeometry(QRect(390, 70, 191, 31))
        self.phone_edt = QLineEdit(self.Parent_page)
        self.phone_edt.setObjectName(u"phone_edt")
        self.phone_edt.setGeometry(QRect(390, 150, 191, 31))
        self.username_edt = QLineEdit(self.Parent_page)
        self.username_edt.setObjectName(u"username_edt")
        self.username_edt.setGeometry(QRect(390, 190, 191, 31))
        self.pass_edit = QLineEdit(self.Parent_page)
        self.pass_edit.setObjectName(u"pass_edit")
        self.pass_edit.setGeometry(QRect(390, 230, 191, 31))
        self.repass_edt = QLineEdit(self.Parent_page)
        self.repass_edt.setObjectName(u"repass_edt")
        self.repass_edt.setGeometry(QRect(390, 270, 191, 31))
        self.label_8 = QLabel(self.Parent_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(260, 10, 221, 21))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 24pt \"Goudy Old Style\";")
        self.Submit_btn = QPushButton(self.Parent_page)
        self.Submit_btn.setObjectName(u"Submit_btn")
        self.Submit_btn.setGeometry(QRect(230, 320, 181, 31))
        self.Submit_btn.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.Parent_page)
        self.Child_page = QWidget()
        self.Child_page.setObjectName(u"Child_page")
        self.label_9 = QLabel(self.Child_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 30, 191, 30))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 24pt \"Goudy Old Style\";")
        self.label_3 = QLabel(self.Child_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 120, 100, 30))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Goudy Old Style\";")
        self.label_10 = QLabel(self.Child_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 290, 100, 30))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.label_11 = QLabel(self.Child_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 240, 100, 30))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.label_12 = QLabel(self.Child_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(120, 80, 100, 30))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")
        self.label_13 = QLabel(self.Child_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(120, 200, 100, 30))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")

        self.label_14 = QLabel(self.Child_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(120, 160, 131, 30))
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Goudy Old Style\";")

        self.child_Name_edt = QLineEdit(self.Child_page)
        self.child_Name_edt.setObjectName(u"child_Name_edt")
        self.child_Name_edt.setGeometry(QRect(430, 70, 191, 31))
        self.Acc_edt = QLineEdit(self.Child_page)
        self.Acc_edt.setObjectName(u"Acc_edt")
        self.Acc_edt.setGeometry(QRect(430, 120, 191, 31))
        self.dateEdit = QDateEdit(self.Child_page)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(430, 160, 191, 31))
        self.child_username_edt = QLineEdit(self.Child_page)
        self.child_username_edt.setObjectName(u"child_username_edt")
        self.child_username_edt.setGeometry(QRect(430, 200, 191, 31))
        self.chid_pass_edit = QLineEdit(self.Child_page)
        self.chid_pass_edit.setObjectName(u"chid_pass_edit")
        self.chid_pass_edit.setGeometry(QRect(430, 240, 191, 31))
        self.child_repass_edt = QLineEdit(self.Child_page)
        self.child_repass_edt.setObjectName(u"child_repass_edt")
        self.child_repass_edt.setGeometry(QRect(430, 290, 191, 31))
        self.child_submit_btn = QPushButton(self.Child_page)
        self.child_submit_btn.setObjectName(u"child_submit_btn")
        self.child_submit_btn.setGeometry(QRect(270, 340, 181, 31))
        self.child_submit_btn.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.Child_page)
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentWidget(self.Parent_page)
        self.transaction_btn.clicked.connect(self.open_parent_account_page)
        self.transaction_btn_2.clicked.connect(self.open_child_account_page)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def open_parent_account_page(self):
        self.stackedWidget.setCurrentWidget(self.Parent_page)

    def open_child_account_page(self):
        self.stackedWidget.setCurrentWidget(self.Child_page)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Create Account Parent", None))
        self.transaction_btn_2.setText(QCoreApplication.translate("MainWindow", u"Create Account Child", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Welcome To Balya Bank", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Re-enter Password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Parent Account", None))
        self.Submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Child Account", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Re-enter Password", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None))
        self.child_submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        # retranslateUi

        # Onclick
        self.Submit_btn.clicked.connect(self.parentSignUp)

    def parentSignUp(self):
        if self.pass_edit.text() == self.repass_edt.text():
            parent_signup_success = signup.parent_signup(self.Name_edt.text(), self.username_edt.text(),
                                                         self.pass_edit.text(), self.phone_edt.text())

            # if parent_signup_success:
            #     self.
