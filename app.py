import connect
import sys
app=connect.uis.userlogin.QtWidgets.QApplication(sys.argv)
userwindow=connect.login()

userwindow.show()
sys.exit(app.exec())