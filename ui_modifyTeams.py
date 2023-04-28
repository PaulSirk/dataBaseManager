# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyTeams.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(342, 382)
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

        self.frmDataset = QFormLayout()
        self.frmDataset.setObjectName(u"frmDataset")
        self.lblTeamName = QLabel(Dialog)
        self.lblTeamName.setObjectName(u"lblTeamName")

        self.frmDataset.setWidget(0, QFormLayout.LabelRole, self.lblTeamName)

        self.leTeamName = QLineEdit(Dialog)
        self.leTeamName.setObjectName(u"leTeamName")
        self.leTeamName.setMaxLength(20)

        self.frmDataset.setWidget(0, QFormLayout.FieldRole, self.leTeamName)

        self.lblRelationship = QLabel(Dialog)
        self.lblRelationship.setObjectName(u"lblRelationship")

        self.frmDataset.setWidget(1, QFormLayout.LabelRole, self.lblRelationship)

        self.lblGenders = QLabel(Dialog)
        self.lblGenders.setObjectName(u"lblGenders")

        self.frmDataset.setWidget(2, QFormLayout.LabelRole, self.lblGenders)

        self.lblSeasonId = QLabel(Dialog)
        self.lblSeasonId.setObjectName(u"lblSeasonId")

        self.frmDataset.setWidget(3, QFormLayout.LabelRole, self.lblSeasonId)

        self.lblPlacement = QLabel(Dialog)
        self.lblPlacement.setObjectName(u"lblPlacement")

        self.frmDataset.setWidget(4, QFormLayout.LabelRole, self.lblPlacement)

        self.leRelationship = QLineEdit(Dialog)
        self.leRelationship.setObjectName(u"leRelationship")
        self.leRelationship.setMaxLength(20)

        self.frmDataset.setWidget(1, QFormLayout.FieldRole, self.leRelationship)

        self.cbGenders = QComboBox(Dialog)
        self.cbGenders.addItem("")
        self.cbGenders.addItem("")
        self.cbGenders.addItem("")
        self.cbGenders.setObjectName(u"cbGenders")

        self.frmDataset.setWidget(2, QFormLayout.FieldRole, self.cbGenders)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(4)

        self.frmDataset.setWidget(3, QFormLayout.FieldRole, self.spinBox)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(2)

        self.frmDataset.setWidget(4, QFormLayout.FieldRole, self.lineEdit)


        self.verticalLayout.addLayout(self.frmDataset)

        self.hozLayoutTeams = QHBoxLayout()
        self.hozLayoutTeams.setObjectName(u"hozLayoutTeams")
        self.pbAccept = QPushButton(Dialog)
        self.pbAccept.setObjectName(u"pbAccept")
        font1 = QFont()
        font1.setPointSize(16)
        self.pbAccept.setFont(font1)

        self.hozLayoutTeams.addWidget(self.pbAccept)

        self.pbCancel = QPushButton(Dialog)
        self.pbCancel.setObjectName(u"pbCancel")
        self.pbCancel.setFont(font1)

        self.hozLayoutTeams.addWidget(self.pbCancel)


        self.verticalLayout.addLayout(self.hozLayoutTeams)


        self.retranslateUi(Dialog)
        self.pbCancel.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblOperation.setText(QCoreApplication.translate("Dialog", u"Teams", None))
        self.lblTeamName.setText(QCoreApplication.translate("Dialog", u"Team Name: ", None))
        self.lblRelationship.setText(QCoreApplication.translate("Dialog", u"Relationship: ", None))
        self.lblGenders.setText(QCoreApplication.translate("Dialog", u"Genders: ", None))
        self.lblSeasonId.setText(QCoreApplication.translate("Dialog", u"Season Id: ", None))
        self.lblPlacement.setText(QCoreApplication.translate("Dialog", u"Placement: ", None))
        self.cbGenders.setItemText(0, QCoreApplication.translate("Dialog", u"mm", None))
        self.cbGenders.setItemText(1, QCoreApplication.translate("Dialog", u"mf", None))
        self.cbGenders.setItemText(2, QCoreApplication.translate("Dialog", u"ff", None))

        self.pbAccept.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.pbCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

