import api
import ui
import sys
ui_rc=ui.resource.ui_rc
QPixmap=ui.user.QtGui.QPixmap
app=ui.user.QtWidgets.QApplication(sys.argv)
userwindow=ui.user.mainwindow()
userwindow.setWindowIcon(QPixmap(u":/test/test.ico"))
userwindow.show()
sys.exit(app.exec())