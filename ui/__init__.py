import qframelesswindow
from Ui_main import Ui_MainWindow
from user import *
from qframelesswindow import *
class mainwindow(Ui_MainWindow,qframelesswindow.FramelessWindow):
    #mainwindow
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

    #loginwindow
    class loginwindow(Ui_login.Ui_Form,QtWidgets.QMainWindow):
        def __init__(self):
            super(self).__init__()
            self.login_lineEdit.setPlaceholderText("你的用户名")
            self.password_lineEdit.setPalette("你的密码")
            self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
            self.setupUi(self)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec())