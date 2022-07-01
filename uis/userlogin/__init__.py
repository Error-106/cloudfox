from operator import truediv
from .Ui_main_login_page import Ui_MainWindow
from .login_and_reg_ui import *
import win32con
from win32api import SendMessage
from win32gui import ReleaseCapture
class mainloginwindow(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.child=self.children()
        self.child=self.loginwindow()
        self.gridLayout.addWidget(self.child,0,1)
        self.child.show()
    def mouseMoveEvent(self, event):
        if not 0 < event.pos().x() < self.width() - 46 * 3:return
        ReleaseCapture()
        SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,win32con.SC_MOVE + win32con.HTCAPTION, 0)
        event.ignore()
    class loginwindow(Ui_login_and_reg.Ui_Form,QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.text_inf_label.setHidden(True)
            self.text_mail_label.setHidden(True)
            self.mail_lineEdit.setHidden(True)
            self.text_qnum_label.setHidden(True)
            self.qnum_lineEdit.setHidden(True)
            self.text_inv_label.setHidden(True)
            self.inv_lineEdit.setHidden(True)
            self.login_lineEdit.setPlaceholderText("你的用户名")
            self.password_lineEdit.setPlaceholderText("你的密码")
            self.mail_lineEdit.setPlaceholderText("你的邮箱")
            self.inv_lineEdit.setPlaceholderText("邀请码，非必填")
            self.qnum_lineEdit.setPlaceholderText("你的QQ，非必填")
            self.pixverify_lineEdit.setPlaceholderText("图片验证码")
            self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)