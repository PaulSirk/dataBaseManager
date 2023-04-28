# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifySeasons.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 395)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblOperation = QLabel(Dialog)
        self.lblOperation.setObjectName(u"lblOperation")
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setPointSize(36)
        self.lblOperation.setFont(font)
        self.lblOperation.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblOperation)

        self.frmSeasons = QFormLayout()
        self.frmSeasons.setObjectName(u"frmSeasons")
        self.lblCountry = QLabel(Dialog)
        self.lblCountry.setObjectName(u"lblCountry")

        self.frmSeasons.setWidget(0, QFormLayout.LabelRole, self.lblCountry)

        self.lblNum = QLabel(Dialog)
        self.lblNum.setObjectName(u"lblNum")

        self.frmSeasons.setWidget(1, QFormLayout.LabelRole, self.lblNum)

        self.lblTeamNum = QLabel(Dialog)
        self.lblTeamNum.setObjectName(u"lblTeamNum")

        self.frmSeasons.setWidget(2, QFormLayout.LabelRole, self.lblTeamNum)

        self.lblPremiere = QLabel(Dialog)
        self.lblPremiere.setObjectName(u"lblPremiere")

        self.frmSeasons.setWidget(3, QFormLayout.LabelRole, self.lblPremiere)

        self.lblFinale = QLabel(Dialog)
        self.lblFinale.setObjectName(u"lblFinale")

        self.frmSeasons.setWidget(4, QFormLayout.LabelRole, self.lblFinale)

        self.lblEpisodes = QLabel(Dialog)
        self.lblEpisodes.setObjectName(u"lblEpisodes")

        self.frmSeasons.setWidget(5, QFormLayout.LabelRole, self.lblEpisodes)

        self.leCountry = QLineEdit(Dialog)
        self.leCountry.setObjectName(u"leCountry")
        self.leCountry.setMaxLength(3)

        self.frmSeasons.setWidget(0, QFormLayout.FieldRole, self.leCountry)

        self.sbSeason = QSpinBox(Dialog)
        self.sbSeason.setObjectName(u"sbSeason")
        self.sbSeason.setMinimum(1)

        self.frmSeasons.setWidget(1, QFormLayout.FieldRole, self.sbSeason)

        self.sbTeams = QSpinBox(Dialog)
        self.sbTeams.setObjectName(u"sbTeams")
        self.sbTeams.setMinimum(1)
        self.sbTeams.setMaximum(20)

        self.frmSeasons.setWidget(2, QFormLayout.FieldRole, self.sbTeams)

        self.dePremiere = QDateEdit(Dialog)
        self.dePremiere.setObjectName(u"dePremiere")

        self.frmSeasons.setWidget(3, QFormLayout.FieldRole, self.dePremiere)

        self.deFinale = QDateEdit(Dialog)
        self.deFinale.setObjectName(u"deFinale")

        self.frmSeasons.setWidget(4, QFormLayout.FieldRole, self.deFinale)

        self.sbEpisodes = QSpinBox(Dialog)
        self.sbEpisodes.setObjectName(u"sbEpisodes")
        self.sbEpisodes.setMinimum(1)

        self.frmSeasons.setWidget(5, QFormLayout.FieldRole, self.sbEpisodes)


        self.verticalLayout.addLayout(self.frmSeasons)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbAccept = QPushButton(Dialog)
        self.pbAccept.setObjectName(u"pbAccept")
        font1 = QFont()
        font1.setPointSize(16)
        self.pbAccept.setFont(font1)

        self.horizontalLayout.addWidget(self.pbAccept)

        self.pbCancel = QPushButton(Dialog)
        self.pbCancel.setObjectName(u"pbCancel")
        self.pbCancel.setFont(font1)

        self.horizontalLayout.addWidget(self.pbCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.pbCancel.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblOperation.setText(QCoreApplication.translate("Dialog", u"Seasons", None))
        self.lblCountry.setText(QCoreApplication.translate("Dialog", u"Country:", None))
        self.lblNum.setText(QCoreApplication.translate("Dialog", u"Season #:", None))
        self.lblTeamNum.setText(QCoreApplication.translate("Dialog", u"Number of Teams:", None))
        self.lblPremiere.setText(QCoreApplication.translate("Dialog", u"Premiere:", None))
        self.lblFinale.setText(QCoreApplication.translate("Dialog", u"Finale:", None))
        self.lblEpisodes.setText(QCoreApplication.translate("Dialog", u"Episodes:", None))
        self.dePremiere.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-mm-dd", None))
        self.deFinale.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-mm-dd", None))
        self.pbAccept.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.pbCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

