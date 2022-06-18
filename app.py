import api
import ui
import sys
app=ui.user.QtWidgets.QApplication(sys.argv)
userwindow=ui.user.mainwindow()
#userwindow.setWindowIcon(ui.resource.ui_rc)
userwindow.show()
sys.exit(app.exec())