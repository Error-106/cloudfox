import qframelesswindow
from Ui_main import Ui_MainWindow
from user import *

import win32con
from win32api import SendMessage
from win32gui import ReleaseCapture
class WindowsTitleBar(QtWidgets.QMainWindow):
    """ Title bar for Windows system """

    def mouseMoveEvent(self, event):
        """ Move the window """
        
        if not 0 < event.pos().x() < self.width() - 46 * 3:
            return

        ReleaseCapture()
        SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,
                    win32con.SC_MOVE + win32con.HTCAPTION, 0)
        event.ignore()

class mainwindow(Ui_MainWindow,WindowsTitleBar):
    #mainwindow

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.child=self.children()
        self.child=self.loginwindow()
        self.gridLayout.addWidget(self.child, 0, 1, 1, 1)
        #self.child.setVerticalStretch(1)
        #self.child.setHorizontalStretch(1)
        self.child.login_in_later_pushButton.clicked.connect(self.close)
        self.label.setPixmap(QtGui.QPixmap("test.png"))
        self.child.show()

    #loginwindow
    class loginwindow(Ui_login.Ui_Form,QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.text_pixverify_label.setHidden(True)
            self.login_lineEdit.setPlaceholderText("你的用户名")
            self.password_lineEdit.setPlaceholderText("你的密码")
            self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec())