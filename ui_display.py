# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_qdDisplay(object):
    def setupUi(self, qdDisplay):
        if not qdDisplay.objectName():
            qdDisplay.setObjectName(u"qdDisplay")
        qdDisplay.resize(400, 427)
        self.lblDisplay = QLabel(qdDisplay)
        self.lblDisplay.setObjectName(u"lblDisplay")
        self.lblDisplay.setGeometry(QRect(20, 20, 351, 61))
        font = QFont()
        font.setPointSize(36)
        self.lblDisplay.setFont(font)
        self.lblDisplay.setAlignment(Qt.AlignCenter)
        self.tbTeam = QTableView(qdDisplay)
        self.tbTeam.setObjectName(u"tbTeam")
        self.tbTeam.setGeometry(QRect(30, 90, 341, 221))
        self.pbExit = QPushButton(qdDisplay)
        self.pbExit.setObjectName(u"pbExit")
        self.pbExit.setGeometry(QRect(30, 340, 341, 61))
        font1 = QFont()
        font1.setPointSize(35)
        self.pbExit.setFont(font1)

        self.retranslateUi(qdDisplay)
        self.pbExit.clicked.connect(qdDisplay.close)

        QMetaObject.connectSlotsByName(qdDisplay)
    # setupUi

    def retranslateUi(self, qdDisplay):
        qdDisplay.setWindowTitle(QCoreApplication.translate("qdDisplay", u"Dialog", None))
        self.lblDisplay.setText(QCoreApplication.translate("qdDisplay", u"Display Team", None))
        self.pbExit.setText(QCoreApplication.translate("qdDisplay", u"Exit", None))
    # retranslateUi

