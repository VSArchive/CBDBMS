import sys

from UI.ui_Child_menu_page import *


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.transaction_page)
        self.ui.transaction_btn.clicked.connect(self.show_transaction_page)
        self.ui.transfer_btn.clicked.connect(self.show_transfer_page)
        self.ui.deposit_btn.clicked.connect(self.show_deposit_page)
        self.ui.withdraw_btn.clicked.connect(self.show_withdraw_page)

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.verify_account_page)
        self.ui.verify_btn.clicked.connect(self.show_amount_enter_page)
        self.ui.confirm_btn.clicked.connect(self.show_Confirm_amount_page)

    def show_amount_enter_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.amount_enter_page)

    def show_Confirm_amount_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.Confirm_amount_page)

    def show_transaction_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.transaction_page)

    def show_transfer_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.transfer_page)

    def show_deposit_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.depost_page)

    def show_withdraw_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.withdraw_page)

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
