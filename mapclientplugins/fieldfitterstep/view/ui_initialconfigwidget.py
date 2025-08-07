# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'initialconfigwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QSizePolicy,
    QSpinBox, QWidget)

from cmlibs.widgets.fieldchooserwidget import FieldChooserWidget

class Ui_InitialConfig(object):
    def setupUi(self, InitialConfig):
        if not InitialConfig.objectName():
            InitialConfig.setObjectName(u"InitialConfig")
        InitialConfig.resize(404, 223)
        self.formLayout = QFormLayout(InitialConfig)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.configDataCoordinates_label = QLabel(InitialConfig)
        self.configDataCoordinates_label.setObjectName(u"configDataCoordinates_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.configDataCoordinates_label)

        self.configDataCoordinates_fieldChooser = FieldChooserWidget(InitialConfig)
        self.configDataCoordinates_fieldChooser.setObjectName(u"configDataCoordinates_fieldChooser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configDataCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataCoordinates_fieldChooser.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.configDataCoordinates_fieldChooser)

        self.configModelCoordinates_label = QLabel(InitialConfig)
        self.configModelCoordinates_label.setObjectName(u"configModelCoordinates_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.configModelCoordinates_label)

        self.configModelCoordinates_fieldChooser = FieldChooserWidget(InitialConfig)
        self.configModelCoordinates_fieldChooser.setObjectName(u"configModelCoordinates_fieldChooser")
        sizePolicy.setHeightForWidth(self.configModelCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configModelCoordinates_fieldChooser.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.configModelCoordinates_fieldChooser)

        self.configModelFitGroup_label = QLabel(InitialConfig)
        self.configModelFitGroup_label.setObjectName(u"configModelFitGroup_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.configModelFitGroup_label)

        self.configModelFitGroup_fieldChooser = FieldChooserWidget(InitialConfig)
        self.configModelFitGroup_fieldChooser.setObjectName(u"configModelFitGroup_fieldChooser")
        sizePolicy.setHeightForWidth(self.configModelFitGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configModelFitGroup_fieldChooser.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.configModelFitGroup_fieldChooser)

        self.configFibreOrientation_label = QLabel(InitialConfig)
        self.configFibreOrientation_label.setObjectName(u"configFibreOrientation_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.configFibreOrientation_label)

        self.configFibreOrientation_fieldChooser = FieldChooserWidget(InitialConfig)
        self.configFibreOrientation_fieldChooser.setObjectName(u"configFibreOrientation_fieldChooser")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.configFibreOrientation_fieldChooser)

        self.configDiagnosticLevel_label = QLabel(InitialConfig)
        self.configDiagnosticLevel_label.setObjectName(u"configDiagnosticLevel_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.configDiagnosticLevel_label)

        self.configDiagnosticLevel_spinBox = QSpinBox(InitialConfig)
        self.configDiagnosticLevel_spinBox.setObjectName(u"configDiagnosticLevel_spinBox")
        self.configDiagnosticLevel_spinBox.setMaximum(2)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.configDiagnosticLevel_spinBox)


        self.retranslateUi(InitialConfig)

        QMetaObject.connectSlotsByName(InitialConfig)
    # setupUi

    def retranslateUi(self, InitialConfig):
        InitialConfig.setWindowTitle(QCoreApplication.translate("InitialConfig", u"Initial Config.", None))
        self.configDataCoordinates_label.setText(QCoreApplication.translate("InitialConfig", u"Data coordinates:", None))
        self.configModelCoordinates_label.setText(QCoreApplication.translate("InitialConfig", u"Model coordinates:", None))
        self.configModelFitGroup_label.setText(QCoreApplication.translate("InitialConfig", u"Model fit group:", None))
        self.configFibreOrientation_label.setText(QCoreApplication.translate("InitialConfig", u"Fibre orientation:", None))
#if QT_CONFIG(tooltip)
        self.configFibreOrientation_fieldChooser.setToolTip(QCoreApplication.translate("InitialConfig", u"<html><head/><body><p>Field supplying Euler angles to rotate local 'fibre' axes on which strain and curvature penalties are applied. Clear to apply on global x, y, z axes. Required for fitting 2D meshes with 3 coordinate components.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configDiagnosticLevel_label.setText(QCoreApplication.translate("InitialConfig", u"Diagnostic level:", None))
    # retranslateUi

