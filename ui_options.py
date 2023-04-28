# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(449, 375)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblOptions = QLabel(Dialog)
        self.lblOptions.setObjectName(u"lblOptions")
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setPointSize(36)
        self.lblOptions.setFont(font)
        self.lblOptions.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblOptions)

        self.vlTables = QVBoxLayout()
        self.vlTables.setObjectName(u"vlTables")
        self.lblTables = QLabel(Dialog)
        self.lblTables.setObjectName(u"lblTables")

        self.vlTables.addWidget(self.lblTables)

        self.rdSeasons = QRadioButton(Dialog)
        self.rdSeasons.setObjectName(u"rdSeasons")

        self.vlTables.addWidget(self.rdSeasons)

        self.rdTeams = QRadioButton(Dialog)
        self.rdTeams.setObjectName(u"rdTeams")

        self.vlTables.addWidget(self.rdTeams)


        self.verticalLayout.addLayout(self.vlTables)

        self.vlOptionButtons = QVBoxLayout()
        self.vlOptionButtons.setObjectName(u"vlOptionButtons")
        self.pbAdd = QPushButton(Dialog)
        self.pbAdd.setObjectName(u"pbAdd")
        font1 = QFont()
        font1.setPointSize(18)
        self.pbAdd.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbAdd)

        self.pbDelete = QPushButton(Dialog)
        self.pbDelete.setObjectName(u"pbDelete")
        self.pbDelete.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbDelete)

        self.pbUpdate = QPushButton(Dialog)
        self.pbUpdate.setObjectName(u"pbUpdate")
        self.pbUpdate.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbUpdate)

        self.pbDisplay = QPushButton(Dialog)
        self.pbDisplay.setObjectName(u"pbDisplay")
        self.pbDisplay.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbDisplay)


        self.verticalLayout.addLayout(self.vlOptionButtons)

        self.pbExit = QPushButton(Dialog)
        self.pbExit.setObjectName(u"pbExit")
        font2 = QFont()
        font2.setPointSize(20)
        self.pbExit.setFont(font2)

        self.verticalLayout.addWidget(self.pbExit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblOptions.setText(QCoreApplication.translate("Dialog", u"Options", None))
        self.lblTables.setText(QCoreApplication.translate("Dialog", u"Select Table to Modify", None))
        self.rdSeasons.setText(QCoreApplication.translate("Dialog", u"Seasons", None))
        self.rdTeams.setText(QCoreApplication.translate("Dialog", u"Teams", None))
        self.pbAdd.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.pbDelete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pbUpdate.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.pbDisplay.setText(QCoreApplication.translate("Dialog", u"Display", None))
        self.pbExit.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi
