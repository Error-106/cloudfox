# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(398, 217)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.user_label = QLabel(Form)
        self.user_label.setObjectName(u"user_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_label.sizePolicy().hasHeightForWidth())
        self.user_label.setSizePolicy(sizePolicy1)
        self.user_label.setMinimumSize(QSize(65, 20))
        self.user_label.setMaximumSize(QSize(100, 20))
        self.user_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.user_label, 0, 0, 1, 1)

        self.login_lineEdit = QLineEdit(Form)
        self.login_lineEdit.setObjectName(u"login_lineEdit")

        self.gridLayout.addWidget(self.login_lineEdit, 0, 1, 1, 2)

        self.password_label = QLabel(Form)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(65, 20))
        self.password_label.setMaximumSize(QSize(100, 20))
        self.password_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)

        self.password_lineEdit = QLineEdit(Form)
        self.password_lineEdit.setObjectName(u"password_lineEdit")

        self.gridLayout.addWidget(self.password_lineEdit, 1, 1, 1, 2)

        self.login_pushButton = QPushButton(Form)
        self.login_pushButton.setObjectName(u"login_pushButton")
        sizePolicy.setHeightForWidth(self.login_pushButton.sizePolicy().hasHeightForWidth())
        self.login_pushButton.setSizePolicy(sizePolicy)
        self.login_pushButton.setMinimumSize(QSize(85, 25))

        self.gridLayout.addWidget(self.login_pushButton, 2, 0, 1, 1)

        self.reg_pushButton = QPushButton(Form)
        self.reg_pushButton.setObjectName(u"reg_pushButton")
        sizePolicy.setHeightForWidth(self.reg_pushButton.sizePolicy().hasHeightForWidth())
        self.reg_pushButton.setSizePolicy(sizePolicy)
        self.reg_pushButton.setMinimumSize(QSize(85, 25))

        self.gridLayout.addWidget(self.reg_pushButton, 2, 1, 1, 1)

        self.login_in_later_pushButton = QPushButton(Form)
        self.login_in_later_pushButton.setObjectName(u"login_in_later_pushButton")
        sizePolicy.setHeightForWidth(self.login_in_later_pushButton.sizePolicy().hasHeightForWidth())
        self.login_in_later_pushButton.setSizePolicy(sizePolicy)
        self.login_in_later_pushButton.setMinimumSize(QSize(85, 25))

        self.gridLayout.addWidget(self.login_in_later_pushButton, 2, 2, 1, 1)

#if QT_CONFIG(shortcut)
        self.user_label.setBuddy(self.login_lineEdit)
        self.password_label.setBuddy(self.password_lineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.user_label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.password_label.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.login_pushButton.setText(QCoreApplication.translate("Form", u"\u73b0\u5728\u767b\u5f55", None))
        self.reg_pushButton.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.login_in_later_pushButton.setText(QCoreApplication.translate("Form", u"\u7a0d\u540e\u767b\u5f55", None))
    # retranslateUi

