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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(342, 309)
        self.lblOperation = QLabel(Dialog)
        self.lblOperation.setObjectName(u"lblOperation")
        self.lblOperation.setGeometry(QRect(20, 10, 301, 61))
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setPointSize(36)
        self.lblOperation.setFont(font)
        self.lblOperation.setAlignment(Qt.AlignCenter)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 70, 301, 171))
        self.frmDataset = QFormLayout(self.formLayoutWidget)
        self.frmDataset.setObjectName(u"frmDataset")
        self.frmDataset.setContentsMargins(0, 0, 0, 0)
        self.lblTeamName = QLabel(self.formLayoutWidget)
        self.lblTeamName.setObjectName(u"lblTeamName")

        self.frmDataset.setWidget(0, QFormLayout.LabelRole, self.lblTeamName)

        self.leTeamName = QLineEdit(self.formLayoutWidget)
        self.leTeamName.setObjectName(u"leTeamName")
        self.leTeamName.setMaxLength(20)

        self.frmDataset.setWidget(0, QFormLayout.FieldRole, self.leTeamName)

        self.lblRelationship = QLabel(self.formLayoutWidget)
        self.lblRelationship.setObjectName(u"lblRelationship")

        self.frmDataset.setWidget(1, QFormLayout.LabelRole, self.lblRelationship)

        self.lblGenders = QLabel(self.formLayoutWidget)
        self.lblGenders.setObjectName(u"lblGenders")

        self.frmDataset.setWidget(2, QFormLayout.LabelRole, self.lblGenders)

        self.lblSeasonId = QLabel(self.formLayoutWidget)
        self.lblSeasonId.setObjectName(u"lblSeasonId")

        self.frmDataset.setWidget(3, QFormLayout.LabelRole, self.lblSeasonId)

        self.lblPlacement = QLabel(self.formLayoutWidget)
        self.lblPlacement.setObjectName(u"lblPlacement")

        self.frmDataset.setWidget(4, QFormLayout.LabelRole, self.lblPlacement)

        self.leRelationship = QLineEdit(self.formLayoutWidget)
        self.leRelationship.setObjectName(u"leRelationship")
        self.leRelationship.setMaxLength(20)

        self.frmDataset.setWidget(1, QFormLayout.FieldRole, self.leRelationship)

        self.cbGenders = QComboBox(self.formLayoutWidget)
        self.cbGenders.addItem("")
        self.cbGenders.addItem("")
        self.cbGenders.addItem("")
        self.cbGenders.setObjectName(u"cbGenders")

        self.frmDataset.setWidget(2, QFormLayout.FieldRole, self.cbGenders)

        self.spinBox = QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(4)

        self.frmDataset.setWidget(3, QFormLayout.FieldRole, self.spinBox)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(2)

        self.frmDataset.setWidget(4, QFormLayout.FieldRole, self.lineEdit)

        self.pbAccept = QPushButton(Dialog)
        self.pbAccept.setObjectName(u"pbAccept")
        self.pbAccept.setGeometry(QRect(180, 250, 141, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.pbAccept.setFont(font1)
        self.pbAccept_2 = QPushButton(Dialog)
        self.pbAccept_2.setObjectName(u"pbAccept_2")
        self.pbAccept_2.setGeometry(QRect(20, 250, 141, 41))
        self.pbAccept_2.setFont(font1)

        self.retranslateUi(Dialog)

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
        self.pbAccept_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

