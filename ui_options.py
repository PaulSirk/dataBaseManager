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
        Dialog.resize(448, 369)
        self.lblOptions = QLabel(Dialog)
        self.lblOptions.setObjectName(u"lblOptions")
        self.lblOptions.setGeometry(QRect(10, 10, 431, 61))
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setPointSize(36)
        self.lblOptions.setFont(font)
        self.lblOptions.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(210, 80, 229, 271))
        self.vlOptionButtons = QVBoxLayout(self.verticalLayoutWidget)
        self.vlOptionButtons.setObjectName(u"vlOptionButtons")
        self.vlOptionButtons.setContentsMargins(0, 0, 0, 0)
        self.pbAdd = QPushButton(self.verticalLayoutWidget)
        self.pbAdd.setObjectName(u"pbAdd")
        font1 = QFont()
        font1.setPointSize(18)
        self.pbAdd.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbAdd)

        self.pbDelete = QPushButton(self.verticalLayoutWidget)
        self.pbDelete.setObjectName(u"pbDelete")
        self.pbDelete.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbDelete)

        self.pbUpdate = QPushButton(self.verticalLayoutWidget)
        self.pbUpdate.setObjectName(u"pbUpdate")
        self.pbUpdate.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbUpdate)

        self.pbDisplay = QPushButton(self.verticalLayoutWidget)
        self.pbDisplay.setObjectName(u"pbDisplay")
        self.pbDisplay.setFont(font1)

        self.vlOptionButtons.addWidget(self.pbDisplay)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 80, 166, 80))
        self.vlTables = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlTables.setObjectName(u"vlTables")
        self.vlTables.setContentsMargins(0, 0, 0, 0)
        self.lblTables = QLabel(self.verticalLayoutWidget_2)
        self.lblTables.setObjectName(u"lblTables")

        self.vlTables.addWidget(self.lblTables)

        self.rdSeasons = QRadioButton(self.verticalLayoutWidget_2)
        self.rdSeasons.setObjectName(u"rdSeasons")

        self.vlTables.addWidget(self.rdSeasons)

        self.rdTeams = QRadioButton(self.verticalLayoutWidget_2)
        self.rdTeams.setObjectName(u"rdTeams")

        self.vlTables.addWidget(self.rdTeams)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblOptions.setText(QCoreApplication.translate("Dialog", u"Options", None))
        self.pbAdd.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.pbDelete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pbUpdate.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.pbDisplay.setText(QCoreApplication.translate("Dialog", u"Display", None))
        self.lblTables.setText(QCoreApplication.translate("Dialog", u"Select Table to Modify", None))
        self.rdSeasons.setText(QCoreApplication.translate("Dialog", u"Seasons", None))
        self.rdTeams.setText(QCoreApplication.translate("Dialog", u"Teams", None))
    # retranslateUi

