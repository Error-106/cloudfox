import api
import uis
import sys
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class login(uis.userlogin.mainloginwindow):
    def __init__(self) -> None:
        self.uisid=0
        super().__init__()
        from uis.resource.user import ui_rc
        self.setWindowIcon(uis.QtGui.QPixmap(u":/test/favicon.ico"))
        self.child.login_in_later_pushButton.clicked.connect(self.login_in_later)
        self.child.change_pushButton.clicked.connect(self.uichange)
        self.child.login_pushButton.clicked.connect(self.uilogin)
    def login_in_later(self):
        self.close()
    def uilogin(self):
        if self.uisid:
            self.login(self)
        else:
            self.reg(self)
    def login(self):
        pass
    def reg(self):
        pass
    def uichange(self):
        if self.uisid:
            self.uisid-=1
            self.loginsui()
        else:
            self.uisid+=1
            self.regsui()
    def loginsui(self):
        pass
    def regsui(self):
        pass


