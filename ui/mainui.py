import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
from user import login
import qframelesswindow

class mainwindows(login.Ui_Form,QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindows,self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=mainwindows()
    window.show()
    sys.exit(app.exec())