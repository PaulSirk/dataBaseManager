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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

import ui_options


class Ui_Widget(object):
    def optionsForm(self):
        options = ui_options.QDialog()
        ui = ui_options.Ui_Dialog()
        ui.setupUi(options)
        options.show()
        options.exec()

    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(291, 262)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(Widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frmLogin = QFormLayout()
        self.frmLogin.setObjectName(u"frmLogin")
        self.lblUsername = QLabel(Widget)
        self.lblUsername.setObjectName(u"lblUsername")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblUsername.sizePolicy().hasHeightForWidth())
        self.lblUsername.setSizePolicy(sizePolicy1)

        self.frmLogin.setWidget(1, QFormLayout.LabelRole, self.lblUsername)

        self.lUsername = QLineEdit(Widget)
        self.lUsername.setObjectName(u"lUsername")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lUsername.sizePolicy().hasHeightForWidth())
        self.lUsername.setSizePolicy(sizePolicy2)

        self.frmLogin.setWidget(1, QFormLayout.FieldRole, self.lUsername)

        self.lblPassword = QLabel(Widget)
        self.lblPassword.setObjectName(u"lblPassword")
        sizePolicy1.setHeightForWidth(self.lblPassword.sizePolicy().hasHeightForWidth())
        self.lblPassword.setSizePolicy(sizePolicy1)

        self.frmLogin.setWidget(2, QFormLayout.LabelRole, self.lblPassword)

        self.lPassword = QLineEdit(Widget)
        self.lPassword.setObjectName(u"lPassword")
        sizePolicy2.setHeightForWidth(self.lPassword.sizePolicy().hasHeightForWidth())
        self.lPassword.setSizePolicy(sizePolicy2)

        self.frmLogin.setWidget(2, QFormLayout.FieldRole, self.lPassword)

        self.pbLogin = QPushButton(Widget)
        self.pbLogin.setObjectName(u"pbLogin")
        sizePolicy2.setHeightForWidth(self.pbLogin.sizePolicy().hasHeightForWidth())
        self.pbLogin.setSizePolicy(sizePolicy2)
        self.pbLogin.clicked.connect(self.optionsForm)
        font = QFont()
        font.setPointSize(24)
        self.pbLogin.setFont(font)

        self.frmLogin.setWidget(3, QFormLayout.SpanningRole, self.pbLogin)

        self.pbExit = QPushButton(Widget)
        self.pbExit.setObjectName(u"pbExit")
        font1 = QFont()
        font1.setPointSize(12)
        self.pbExit.setFont(font1)

        self.frmLogin.setWidget(4, QFormLayout.SpanningRole, self.pbExit)

        self.lblLogin = QLabel(Widget)
        self.lblLogin.setObjectName(u"lblLogin")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblLogin.sizePolicy().hasHeightForWidth())
        self.lblLogin.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(36)
        self.lblLogin.setFont(font2)
        self.lblLogin.setAlignment(Qt.AlignCenter)

        self.frmLogin.setWidget(0, QFormLayout.FieldRole, self.lblLogin)


        self.verticalLayout_5.addLayout(self.frmLogin)


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
