import ui
import sys
app=ui.uis.userlogin.QtWidgets.QApplication(sys.argv)
userwindow=ui.login()

userwindow.show()
sys.exit(app.exec())