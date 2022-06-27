import api
import uis
import sys
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class login(uis.user.mainloginwindow):
    def __init__(self) -> None:
        super().__init__()
        from uis.resource.user import ui_rc
        self.setWindowIcon(uis.QtGui.QPixmap(u":/test/favicon.ico"))
        self.child.login_in_later_pushButton.clicked.connect(self.close)
