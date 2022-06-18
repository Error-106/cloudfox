from ui import qframelesswindow
from user import *
from qframelesswindow import *
class mainwindow(qframelesswindow):

    #login
    class loginwindow(Ui_login.Ui_Form,QtWidgets.QMainWindow):
        def __init__(self):
            super(self).__init__()
            self.login_lineEdit.setToolTip("登录")
            self.setupUi(self)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec())