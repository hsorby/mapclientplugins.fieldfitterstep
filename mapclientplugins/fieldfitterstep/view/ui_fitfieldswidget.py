# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fitfieldswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_FitFields(object):
    def setupUi(self, FitFields):
        if not FitFields.objectName():
            FitFields.setObjectName(u"FitFields")
        FitFields.resize(485, 487)
        self.verticalLayout = QVBoxLayout(FitFields)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fitFieldsCheck_frame = QFrame(FitFields)
        self.fitFieldsCheck_frame.setObjectName(u"fitFieldsCheck_frame")
        self.fitFieldsCheck_frame.setFrameShape(QFrame.NoFrame)
        self.fitFieldsCheck_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.fitFieldsCheck_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.fitFieldsCheckAll_pushButton = QPushButton(self.fitFieldsCheck_frame)
        self.fitFieldsCheckAll_pushButton.setObjectName(u"fitFieldsCheckAll_pushButton")

        self.horizontalLayout_10.addWidget(self.fitFieldsCheckAll_pushButton)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.fitFieldsCheckNone_pushButton = QPushButton(self.fitFieldsCheck_frame)
        self.fitFieldsCheckNone_pushButton.setObjectName(u"fitFieldsCheckNone_pushButton")

        self.horizontalLayout_10.addWidget(self.fitFieldsCheckNone_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.fitFieldsCheck_frame)

        self.fitFields_listView = QListView(FitFields)
        self.fitFields_listView.setObjectName(u"fitFields_listView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitFields_listView.sizePolicy().hasHeightForWidth())
        self.fitFields_listView.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.fitFields_listView)

        self.parameters_groupBox = QGroupBox(FitFields)
        self.parameters_groupBox.setObjectName(u"parameters_groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.parameters_groupBox.sizePolicy().hasHeightForWidth())
        self.parameters_groupBox.setSizePolicy(sizePolicy1)
        self.groupSettings_Layout = QFormLayout(self.parameters_groupBox)
        self.groupSettings_Layout.setObjectName(u"groupSettings_Layout")
        self.groupSettings_Layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.groupSettings_Layout.setContentsMargins(-1, 0, -1, 0)
        self.parametersGradient2Penalty_lineEdit = QLineEdit(self.parameters_groupBox)
        self.parametersGradient2Penalty_lineEdit.setObjectName(u"parametersGradient2Penalty_lineEdit")

        self.groupSettings_Layout.setWidget(1, QFormLayout.FieldRole, self.parametersGradient2Penalty_lineEdit)

        self.parametersGradient2Penalty_label = QLabel(self.parameters_groupBox)
        self.parametersGradient2Penalty_label.setObjectName(u"parametersGradient2Penalty_label")

        self.groupSettings_Layout.setWidget(1, QFormLayout.LabelRole, self.parametersGradient2Penalty_label)

        self.parametersGradient1Penalty_lineEdit = QLineEdit(self.parameters_groupBox)
        self.parametersGradient1Penalty_lineEdit.setObjectName(u"parametersGradient1Penalty_lineEdit")

        self.groupSettings_Layout.setWidget(0, QFormLayout.FieldRole, self.parametersGradient1Penalty_lineEdit)

        self.parametersGradient1Penalty_label = QLabel(self.parameters_groupBox)
        self.parametersGradient1Penalty_label.setObjectName(u"parametersGradient1Penalty_label")

        self.groupSettings_Layout.setWidget(0, QFormLayout.LabelRole, self.parametersGradient1Penalty_label)


        self.verticalLayout.addWidget(self.parameters_groupBox)

        self.fitButton_frame = QFrame(FitFields)
        self.fitButton_frame.setObjectName(u"fitButton_frame")
        self.fitButton_frame.setFrameShape(QFrame.NoFrame)
        self.fitButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fitButton_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(191, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.controlsFit_pushButton = QPushButton(self.fitButton_frame)
        self.controlsFit_pushButton.setObjectName(u"controlsFit_pushButton")

        self.horizontalLayout.addWidget(self.controlsFit_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(190, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.fitButton_frame)


        self.retranslateUi(FitFields)

        QMetaObject.connectSlotsByName(FitFields)
    # setupUi

    def retranslateUi(self, FitFields):
        FitFields.setWindowTitle(QCoreApplication.translate("FitFields", u"Fit Fields", None))
        self.fitFieldsCheckAll_pushButton.setText(QCoreApplication.translate("FitFields", u"Check All", None))
        self.fitFieldsCheckNone_pushButton.setText(QCoreApplication.translate("FitFields", u"Check None", None))
#if QT_CONFIG(tooltip)
        self.fitFields_listView.setToolTip(QCoreApplication.translate("FitFields", u"<html><head/><body><p>Check fields for fitting.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.parameters_groupBox.setTitle(QCoreApplication.translate("FitFields", u"Parameters", None))
        self.parametersGradient2Penalty_label.setText(QCoreApplication.translate("FitFields", u"Gradient 2 penalty:", None))
        self.parametersGradient1Penalty_label.setText(QCoreApplication.translate("FitFields", u"Gradient 1 penalty:", None))
#if QT_CONFIG(tooltip)
        self.controlsFit_pushButton.setToolTip(QCoreApplication.translate("FitFields", u"<html><head/><body><p>Fit currently highlighted field.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.controlsFit_pushButton.setText(QCoreApplication.translate("FitFields", u"Fit", None))
    # retranslateUi

