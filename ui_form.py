# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(250, 305)
        self.formLayoutWidget = QWidget(Widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 90, 211, 71))
        self.frmLogin = QFormLayout(self.formLayoutWidget)
        self.frmLogin.setObjectName(u"frmLogin")
        self.frmLogin.setContentsMargins(0, 0, 0, 0)
        self.lblUsername = QLabel(self.formLayoutWidget)
        self.lblUsername.setObjectName(u"lblUsername")

        self.frmLogin.setWidget(0, QFormLayout.LabelRole, self.lblUsername)

        self.lUsername = QLineEdit(self.formLayoutWidget)
        self.lUsername.setObjectName(u"lUsername")

        self.frmLogin.setWidget(0, QFormLayout.FieldRole, self.lUsername)

        self.lblPassword = QLabel(self.formLayoutWidget)
        self.lblPassword.setObjectName(u"lblPassword")

        self.frmLogin.setWidget(1, QFormLayout.LabelRole, self.lblPassword)

        self.lPassword = QLineEdit(self.formLayoutWidget)
        self.lPassword.setObjectName(u"lPassword")

        self.frmLogin.setWidget(1, QFormLayout.FieldRole, self.lPassword)

        self.pbLogin = QPushButton(Widget)
        self.pbLogin.setObjectName(u"pbLogin")
        self.pbLogin.setGeometry(QRect(20, 180, 211, 51))
        font = QFont()
        font.setPointSize(24)
        self.pbLogin.setFont(font)
        self.pbExit = QPushButton(Widget)
        self.pbExit.setObjectName(u"pbExit")
        self.pbExit.setGeometry(QRect(20, 240, 211, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pbExit.setFont(font1)
        self.lblLogin = QLabel(Widget)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setGeometry(QRect(30, 20, 191, 51))
        font2 = QFont()
        font2.setPointSize(36)
        self.lblLogin.setFont(font2)
        self.lblLogin.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Widget)
        self.pbExit.clicked.connect(Widget.close)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Database Manager", None))
        self.lblUsername.setText(QCoreApplication.translate("Widget", u"Username:", None))
        self.lblPassword.setText(QCoreApplication.translate("Widget", u"Password:", None))
        self.pbLogin.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.pbExit.setText(QCoreApplication.translate("Widget", u"Exit", None))
        self.lblLogin.setText(QCoreApplication.translate("Widget", u"Login", None))
    # retranslateUi

