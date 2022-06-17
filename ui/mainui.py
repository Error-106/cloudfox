import sys
import PySide6
from user import login

class mainwindows(PySide6.QtWidgets,login.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(PySide6.QtWidgets)

if __name__=="__main__":
    app=PySide6.QtWidgets.QApplication(sys.argv)
    window=mainwindows()
    window.show()
    sys.exit(app.exec())