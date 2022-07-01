# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_and_reg.ui'
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
        Form.resize(398, 172)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.login_lineEdit = QLineEdit(Form)
        self.login_lineEdit.setObjectName(u"login_lineEdit")

        self.gridLayout.addWidget(self.login_lineEdit, 0, 1, 1, 2)

        self.text_pixverify_label = QLabel(Form)
        self.text_pixverify_label.setObjectName(u"text_pixverify_label")
        self.text_pixverify_label.setMinimumSize(QSize(65, 20))
        self.text_pixverify_label.setMaximumSize(QSize(100, 16777215))
        self.text_pixverify_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_pixverify_label, 5, 0, 2, 1)

        self.change_pushButton = QPushButton(Form)
        self.change_pushButton.setObjectName(u"change_pushButton")
        sizePolicy.setHeightForWidth(self.change_pushButton.sizePolicy().hasHeightForWidth())
        self.change_pushButton.setSizePolicy(sizePolicy)
        self.change_pushButton.setMinimumSize(QSize(85, 25))

        self.gridLayout.addWidget(self.change_pushButton, 8, 1, 1, 1)

        self.text_mail_label = QLabel(Form)
        self.text_mail_label.setObjectName(u"text_mail_label")
        self.text_mail_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_mail_label, 1, 0, 1, 1)

        self.text_password_label = QLabel(Form)
        self.text_password_label.setObjectName(u"text_password_label")
        self.text_password_label.setMinimumSize(QSize(65, 20))
        self.text_password_label.setMaximumSize(QSize(100, 20))
        self.text_password_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_password_label, 3, 0, 1, 1)

        self.text_qnum_label = QLabel(Form)
        self.text_qnum_label.setObjectName(u"text_qnum_label")
        self.text_qnum_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_qnum_label, 2, 0, 1, 1)

        self.qnum_lineEdit = QLineEdit(Form)
        self.qnum_lineEdit.setObjectName(u"qnum_lineEdit")

        self.gridLayout.addWidget(self.qnum_lineEdit, 2, 1, 1, 2)

        self.pixverify_lineEdit = QLineEdit(Form)
        self.pixverify_lineEdit.setObjectName(u"pixverify_lineEdit")

        self.gridLayout.addWidget(self.pixverify_lineEdit, 6, 1, 1, 2)

        self.text_user_label = QLabel(Form)
        self.text_user_label.setObjectName(u"text_user_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_user_label.sizePolicy().hasHeightForWidth())
        self.text_user_label.setSizePolicy(sizePolicy1)
        self.text_user_label.setMinimumSize(QSize(65, 20))
        self.text_user_label.setMaximumSize(QSize(100, 20))
        self.text_user_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_user_label, 0, 0, 1, 1)

        self.mail_lineEdit = QLineEdit(Form)
        self.mail_lineEdit.setObjectName(u"mail_lineEdit")

        self.gridLayout.addWidget(self.mail_lineEdit, 1, 1, 1, 2)

        self.login_pushButton = QPushButton(Form)
        self.login_pushButton.setObjectName(u"login_pushButton")
        sizePolicy.setHeightForWidth(self.login_pushButton.sizePolicy().hasHeightForWidth())
        self.login_pushButton.setSizePolicy(sizePolicy)
        self.login_pushButton.setMinimumSize(QSize(85, 25))

        self.gridLayout.addWidget(self.login_pushButton, 8, 0, 1, 1)

        self.password_lineEdit = QLineEdit(Form)
        self.password_lineEdit.setObjectName(u"password_lineEdit")

        self.gridLayout.addWidget(self.password_lineEdit, 3, 1, 1, 2)

        self.text_inv_label = QLabel(Form)
        self.text_inv_label.setObjectName(u"text_inv_label")
        self.text_inv_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_inv_label, 4, 0, 1, 1)

        self.login_in_later_pushButton = QPushButton(Form)
        self.login_in_later_pushButton.setObjectName(u"login_in_later_pushButton")
        sizePolicy.setHeightForWidth(self.login_in_later_pushButton.sizePolicy().hasHeightForWidth())
        self.login_in_later_pushButton.setSizePolicy(sizePolicy)
        self.login_in_later_pushButton.setMinimumSize(QSize(85, 25))

        self.gridLayout.addWidget(self.login_in_later_pushButton, 8, 2, 1, 1)

        self.inv_lineEdit = QLineEdit(Form)
        self.inv_lineEdit.setObjectName(u"inv_lineEdit")
        self.inv_lineEdit.setInputMethodHints(Qt.ImhNone)

        self.gridLayout.addWidget(self.inv_lineEdit, 4, 1, 1, 2)

        self.text_pixverify_label_2 = QLabel(Form)
        self.text_pixverify_label_2.setObjectName(u"text_pixverify_label_2")

        self.gridLayout.addWidget(self.text_pixverify_label_2, 5, 1, 1, 2)

        self.text_inf_label = QLabel(Form)
        self.text_inf_label.setObjectName(u"text_inf_label")

        self.gridLayout.addWidget(self.text_inf_label, 7, 0, 1, 3)

#if QT_CONFIG(shortcut)
        self.text_password_label.setBuddy(self.password_lineEdit)
        self.text_user_label.setBuddy(self.login_lineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text_pixverify_label.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u9a8c\u8bc1\u7801", None))
        self.change_pushButton.setText(QCoreApplication.translate("Form", u"\u53bb\u6ce8\u518c", None))
        self.text_mail_label.setText(QCoreApplication.translate("Form", u"\u90ae\u7bb1", None))
        self.text_password_label.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.text_qnum_label.setText(QCoreApplication.translate("Form", u"QQ\u53f7", None))
        self.text_user_label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.login_pushButton.setText(QCoreApplication.translate("Form", u"\u73b0\u5728\u767b\u5f55", None))
        self.text_inv_label.setText(QCoreApplication.translate("Form", u"\u9080\u8bf7\u7801", None))
        self.login_in_later_pushButton.setText(QCoreApplication.translate("Form", u"\u7a0d\u540e\u767b\u5f55", None))
        self.text_pixverify_label_2.setText("")
        self.text_inf_label.setText("")
    # retranslateUi

