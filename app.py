import api
import ui
import sys
from ui.resource.user import ui_rc
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

app=ui.user.QtWidgets.QApplication(sys.argv)
userwindow=ui.user.mainwindow()

userwindow.setWindowIcon(ui.QtGui.QPixmap(u":/test/test.ico"))

userwindow.show()
sys.exit(app.exec())