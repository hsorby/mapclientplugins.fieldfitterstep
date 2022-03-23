# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fieldfitterwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.fieldchooserwidget import FieldChooserWidget
from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class Ui_FieldFitterWidget(object):
    def setupUi(self, FieldFitterWidget):
        if not FieldFitterWidget.objectName():
            FieldFitterWidget.setObjectName(u"FieldFitterWidget")
        FieldFitterWidget.resize(1702, 1134)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FieldFitterWidget.sizePolicy().hasHeightForWidth())
        FieldFitterWidget.setSizePolicy(sizePolicy)
        FieldFitterWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(FieldFitterWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(FieldFitterWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.identifier_label = QLabel(self.dockWidgetContents)
        self.identifier_label.setObjectName(u"identifier_label")
        sizePolicy.setHeightForWidth(self.identifier_label.sizePolicy().hasHeightForWidth())
        self.identifier_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.identifier_label)

        self.configInitial_groupBox = QGroupBox(self.dockWidgetContents)
        self.configInitial_groupBox.setObjectName(u"configInitial_groupBox")
        sizePolicy.setHeightForWidth(self.configInitial_groupBox.sizePolicy().hasHeightForWidth())
        self.configInitial_groupBox.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.configInitial_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.configModelCoordinates_label = QLabel(self.configInitial_groupBox)
        self.configModelCoordinates_label.setObjectName(u"configModelCoordinates_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.configModelCoordinates_label)

        self.configModelCoordinates_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configModelCoordinates_fieldChooser.setObjectName(u"configModelCoordinates_fieldChooser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.configModelCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configModelCoordinates_fieldChooser.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.configModelCoordinates_fieldChooser)

        self.configFibreOrientation_label = QLabel(self.configInitial_groupBox)
        self.configFibreOrientation_label.setObjectName(u"configFibreOrientation_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.configFibreOrientation_label)

        self.configFibreOrientation_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configFibreOrientation_fieldChooser.setObjectName(u"configFibreOrientation_fieldChooser")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.configFibreOrientation_fieldChooser)

        self.configDiagnosticLevel_label = QLabel(self.configInitial_groupBox)
        self.configDiagnosticLevel_label.setObjectName(u"configDiagnosticLevel_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.configDiagnosticLevel_label)

        self.configDiagnosticLevel_spinBox = QSpinBox(self.configInitial_groupBox)
        self.configDiagnosticLevel_spinBox.setObjectName(u"configDiagnosticLevel_spinBox")
        self.configDiagnosticLevel_spinBox.setMaximum(2)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.configDiagnosticLevel_spinBox)

        self.configModelFitGroup_label = QLabel(self.configInitial_groupBox)
        self.configModelFitGroup_label.setObjectName(u"configModelFitGroup_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.configModelFitGroup_label)

        self.configModelFitGroup_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configModelFitGroup_fieldChooser.setObjectName(u"configModelFitGroup_fieldChooser")
        sizePolicy2.setHeightForWidth(self.configModelFitGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configModelFitGroup_fieldChooser.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.configModelFitGroup_fieldChooser)

        self.configDataCoordinates_label = QLabel(self.configInitial_groupBox)
        self.configDataCoordinates_label.setObjectName(u"configDataCoordinates_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.configDataCoordinates_label)

        self.configDataCoordinates_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configDataCoordinates_fieldChooser.setObjectName(u"configDataCoordinates_fieldChooser")
        sizePolicy2.setHeightForWidth(self.configDataCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataCoordinates_fieldChooser.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.configDataCoordinates_fieldChooser)


        self.verticalLayout.addWidget(self.configInitial_groupBox)

        self.fitFields_groupBox = QGroupBox(self.dockWidgetContents)
        self.fitFields_groupBox.setObjectName(u"fitFields_groupBox")
        sizePolicy1.setHeightForWidth(self.fitFields_groupBox.sizePolicy().hasHeightForWidth())
        self.fitFields_groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.fitFields_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fitFieldsCheck_frame = QFrame(self.fitFields_groupBox)
        self.fitFieldsCheck_frame.setObjectName(u"fitFieldsCheck_frame")
        self.fitFieldsCheck_frame.setFrameShape(QFrame.StyledPanel)
        self.fitFieldsCheck_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.fitFieldsCheck_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.fitFieldsCheckAll_pushButton = QPushButton(self.fitFieldsCheck_frame)
        self.fitFieldsCheckAll_pushButton.setObjectName(u"fitFieldsCheckAll_pushButton")

        self.horizontalLayout_10.addWidget(self.fitFieldsCheckAll_pushButton)

        self.fitFieldsCheckNone_pushButton = QPushButton(self.fitFieldsCheck_frame)
        self.fitFieldsCheckNone_pushButton.setObjectName(u"fitFieldsCheckNone_pushButton")

        self.horizontalLayout_10.addWidget(self.fitFieldsCheckNone_pushButton)


        self.verticalLayout_2.addWidget(self.fitFieldsCheck_frame)

        self.fitFields_listView = QListView(self.fitFields_groupBox)
        self.fitFields_listView.setObjectName(u"fitFields_listView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fitFields_listView.sizePolicy().hasHeightForWidth())
        self.fitFields_listView.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.fitFields_listView)

        self.parameters_groupBox = QGroupBox(self.fitFields_groupBox)
        self.parameters_groupBox.setObjectName(u"parameters_groupBox")
        sizePolicy.setHeightForWidth(self.parameters_groupBox.sizePolicy().hasHeightForWidth())
        self.parameters_groupBox.setSizePolicy(sizePolicy)
        self.groupSettings_Layout = QFormLayout(self.parameters_groupBox)
        self.groupSettings_Layout.setObjectName(u"groupSettings_Layout")
        self.groupSettings_Layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.groupSettings_Layout.setContentsMargins(-1, 0, -1, 0)
        self.parametersGradient1Penalty_lineEdit = QLineEdit(self.parameters_groupBox)
        self.parametersGradient1Penalty_lineEdit.setObjectName(u"parametersGradient1Penalty_lineEdit")

        self.groupSettings_Layout.setWidget(1, QFormLayout.FieldRole, self.parametersGradient1Penalty_lineEdit)

        self.parametersGradient2Penalty_lineEdit = QLineEdit(self.parameters_groupBox)
        self.parametersGradient2Penalty_lineEdit.setObjectName(u"parametersGradient2Penalty_lineEdit")

        self.groupSettings_Layout.setWidget(2, QFormLayout.FieldRole, self.parametersGradient2Penalty_lineEdit)

        self.parametersGradient1Penalty_label = QLabel(self.parameters_groupBox)
        self.parametersGradient1Penalty_label.setObjectName(u"parametersGradient1Penalty_label")

        self.groupSettings_Layout.setWidget(1, QFormLayout.LabelRole, self.parametersGradient1Penalty_label)

        self.parametersGradient2Penalty_label = QLabel(self.parameters_groupBox)
        self.parametersGradient2Penalty_label.setObjectName(u"parametersGradient2Penalty_label")

        self.groupSettings_Layout.setWidget(2, QFormLayout.LabelRole, self.parametersGradient2Penalty_label)


        self.verticalLayout_2.addWidget(self.parameters_groupBox)

        self.controls_frame = QFrame(self.fitFields_groupBox)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setFrameShape(QFrame.StyledPanel)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.controls_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.controlsFit_pushButton = QPushButton(self.controls_frame)
        self.controlsFit_pushButton.setObjectName(u"controlsFit_pushButton")

        self.horizontalLayout_7.addWidget(self.controlsFit_pushButton)


        self.verticalLayout_2.addWidget(self.controls_frame)


        self.verticalLayout.addWidget(self.fitFields_groupBox)

        self.display_groupBox = QGroupBox(self.dockWidgetContents)
        self.display_groupBox.setObjectName(u"display_groupBox")
        sizePolicy.setHeightForWidth(self.display_groupBox.sizePolicy().hasHeightForWidth())
        self.display_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.display_groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayMisc_frame = QFrame(self.display_groupBox)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.displayAxes_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.horizontalLayout_8.addWidget(self.displayAxes_checkBox)

        self.displaytMisc_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.displaytMisc_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayMisc_frame)

        self.displayData_frame = QFrame(self.display_groupBox)
        self.displayData_frame.setObjectName(u"displayData_frame")
        self.displayData_frame.setFrameShape(QFrame.StyledPanel)
        self.displayData_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.displayData_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.displayDataPoints_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataPoints_checkBox.setObjectName(u"displayDataPoints_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataPoints_checkBox)

        self.displayDataProjections_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataProjections_checkBox.setObjectName(u"displayDataProjections_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataProjections_checkBox)

        self.displayDataProjectionPoints_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataProjectionPoints_checkBox.setObjectName(u"displayDataProjectionPoints_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataProjectionPoints_checkBox)

        self.displayData_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.displayData_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayData_frame)

        self.displayDataField_frame = QFrame(self.display_groupBox)
        self.displayDataField_frame.setObjectName(u"displayDataField_frame")
        self.displayDataField_frame.setFrameShape(QFrame.StyledPanel)
        self.displayDataField_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.displayDataField_frame)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.displayDataFieldLabels_label = QLabel(self.displayDataField_frame)
        self.displayDataFieldLabels_label.setObjectName(u"displayDataFieldLabels_label")

        self.horizontalLayout_12.addWidget(self.displayDataFieldLabels_label)

        self.displayDataFieldLabelsNone_radioButton = QRadioButton(self.displayDataField_frame)
        self.displayDataFieldLabelsNone_radioButton.setObjectName(u"displayDataFieldLabelsNone_radioButton")

        self.horizontalLayout_12.addWidget(self.displayDataFieldLabelsNone_radioButton)

        self.displayDataFieldLabelsValue_radioButton = QRadioButton(self.displayDataField_frame)
        self.displayDataFieldLabelsValue_radioButton.setObjectName(u"displayDataFieldLabelsValue_radioButton")

        self.horizontalLayout_12.addWidget(self.displayDataFieldLabelsValue_radioButton)

        self.displayDataFieldLabelsDelta_radioButton = QRadioButton(self.displayDataField_frame)
        self.displayDataFieldLabelsDelta_radioButton.setObjectName(u"displayDataFieldLabelsDelta_radioButton")

        self.horizontalLayout_12.addWidget(self.displayDataFieldLabelsDelta_radioButton)


        self.verticalLayout_7.addWidget(self.displayDataField_frame)

        self.displayNodes_frame = QFrame(self.display_groupBox)
        self.displayNodes_frame.setObjectName(u"displayNodes_frame")
        self.displayNodes_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNodes_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNodes_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.displayNodePoints_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodePoints_checkBox.setObjectName(u"displayNodePoints_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNodePoints_checkBox)

        self.displayNodeNumbers_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeNumbers_checkBox.setObjectName(u"displayNodeNumbers_checkBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.displayNodeNumbers_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeNumbers_checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_6.addWidget(self.displayNodeNumbers_checkBox)

        self.displayNodes_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.displayNodes_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayNodes_frame)

        self.displayElements_frame = QFrame(self.display_groupBox)
        self.displayElements_frame.setObjectName(u"displayElements_frame")
        self.displayElements_frame.setFrameShape(QFrame.StyledPanel)
        self.displayElements_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.displayElements_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.displayElementNumbers_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementNumbers_checkBox.setObjectName(u"displayElementNumbers_checkBox")

        self.horizontalLayout_4.addWidget(self.displayElementNumbers_checkBox)

        self.displayElementAxes_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementAxes_checkBox.setObjectName(u"displayElementAxes_checkBox")
        sizePolicy4.setHeightForWidth(self.displayElementAxes_checkBox.sizePolicy().hasHeightForWidth())
        self.displayElementAxes_checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.displayElementAxes_checkBox)

        self.displayElements_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.displayElements_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayElements_frame)

        self.displayLines_frame = QFrame(self.display_groupBox)
        self.displayLines_frame.setObjectName(u"displayLines_frame")
        self.displayLines_frame.setFrameShape(QFrame.StyledPanel)
        self.displayLines_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.displayLines_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.displayLines_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLines_checkBox.setObjectName(u"displayLines_checkBox")

        self.horizontalLayout_5.addWidget(self.displayLines_checkBox)

        self.displayLinesExterior_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLinesExterior_checkBox.setObjectName(u"displayLinesExterior_checkBox")
        sizePolicy4.setHeightForWidth(self.displayLinesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLinesExterior_checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.displayLinesExterior_checkBox)

        self.displayLines_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.displayLines_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayLines_frame)

        self.displaySurfaces_frame = QFrame(self.display_groupBox)
        self.displaySurfaces_frame.setObjectName(u"displaySurfaces_frame")
        self.displaySurfaces_frame.setFrameShape(QFrame.StyledPanel)
        self.displaySurfaces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.displaySurfaces_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName(u"displaySurfaces_checkBox")

        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)

        self.displaySurfacesExterior_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName(u"displaySurfacesExterior_checkBox")
        sizePolicy4.setHeightForWidth(self.displaySurfacesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesExterior_checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)

        self.displaySurfacesTranslucent_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName(u"displaySurfacesTranslucent_checkBox")
        sizePolicy4.setHeightForWidth(self.displaySurfacesTranslucent_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesTranslucent_checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)

        self.displaySurfacesWireframe_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName(u"displaySurfacesWireframe_checkBox")
        sizePolicy4.setHeightForWidth(self.displaySurfacesWireframe_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesWireframe_checkBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)

        self.displaySurfaces_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.displaySurfaces_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displaySurfaces_frame)

        self.displayField_frame = QFrame(self.display_groupBox)
        self.displayField_frame.setObjectName(u"displayField_frame")
        self.displayField_frame.setFrameShape(QFrame.StyledPanel)
        self.displayField_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.displayField_frame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.displayFieldColourBar_checkBox = QCheckBox(self.displayField_frame)
        self.displayFieldColourBar_checkBox.setObjectName(u"displayFieldColourBar_checkBox")

        self.horizontalLayout_11.addWidget(self.displayFieldColourBar_checkBox)

        self.displayFieldContours_checkBox = QCheckBox(self.displayField_frame)
        self.displayFieldContours_checkBox.setObjectName(u"displayFieldContours_checkBox")

        self.horizontalLayout_11.addWidget(self.displayFieldContours_checkBox)

        self.displayFieldContoursCount_spinBox = QSpinBox(self.displayField_frame)
        self.displayFieldContoursCount_spinBox.setObjectName(u"displayFieldContoursCount_spinBox")
        self.displayFieldContoursCount_spinBox.setMinimum(1)
        self.displayFieldContoursCount_spinBox.setMaximum(100)

        self.horizontalLayout_11.addWidget(self.displayFieldContoursCount_spinBox)


        self.verticalLayout_7.addWidget(self.displayField_frame)


        self.verticalLayout.addWidget(self.display_groupBox)

        self.bottom_frame = QFrame(self.dockWidgetContents)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.viewAll_pushButton = QPushButton(self.bottom_frame)
        self.viewAll_pushButton.setObjectName(u"viewAll_pushButton")

        self.horizontalLayout_2.addWidget(self.viewAll_pushButton)

        self.stdViews_pushButton = QPushButton(self.bottom_frame)
        self.stdViews_pushButton.setObjectName(u"stdViews_pushButton")

        self.horizontalLayout_2.addWidget(self.stdViews_pushButton)

        self.done_pushButton = QPushButton(self.bottom_frame)
        self.done_pushButton.setObjectName(u"done_pushButton")
        sizePolicy4.setHeightForWidth(self.done_pushButton.sizePolicy().hasHeightForWidth())
        self.done_pushButton.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.done_pushButton)


        self.verticalLayout.addWidget(self.bottom_frame)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.sceneviewerwidget = SceneviewerWidget(FieldFitterWidget)
        self.sceneviewerwidget.setObjectName(u"sceneviewerwidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.sceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerwidget.setSizePolicy(sizePolicy5)
        self.sceneviewerwidget.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.sceneviewerwidget)


        self.retranslateUi(FieldFitterWidget)

        QMetaObject.connectSlotsByName(FieldFitterWidget)
    # setupUi

    def retranslateUi(self, FieldFitterWidget):
        FieldFitterWidget.setWindowTitle(QCoreApplication.translate("FieldFitterWidget", u"Field Fitter", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("FieldFitterWidget", u"Control Panel", None))
        self.identifier_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Identifier", None))
        self.configInitial_groupBox.setTitle(QCoreApplication.translate("FieldFitterWidget", u"Configuration", None))
        self.configModelCoordinates_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Model coordinates:", None))
        self.configFibreOrientation_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Fibre orientation:", None))
#if QT_CONFIG(tooltip)
        self.configFibreOrientation_fieldChooser.setToolTip(QCoreApplication.translate("FieldFitterWidget", u"<html><head/><body><p>Field supplying Euler angles to rotate local 'fibre' axes on which strain and curvature penalties are applied. Clear to apply on global x, y, z axes. Required for fitting 2D meshes with 3 coordinate components.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configDiagnosticLevel_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Diagnostic level:", None))
        self.configModelFitGroup_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Model fit group:", None))
        self.configDataCoordinates_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Data coordinates:", None))
        self.fitFields_groupBox.setTitle(QCoreApplication.translate("FieldFitterWidget", u"Fit fields:", None))
        self.fitFieldsCheckAll_pushButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Check All", None))
        self.fitFieldsCheckNone_pushButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Check None", None))
#if QT_CONFIG(tooltip)
        self.fitFields_listView.setToolTip(QCoreApplication.translate("FieldFitterWidget", u"<html><head/><body><p>Check fields for fitting.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.parameters_groupBox.setTitle(QCoreApplication.translate("FieldFitterWidget", u"Parameters", None))
        self.parametersGradient1Penalty_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Gradient 1 penalty:", None))
        self.parametersGradient2Penalty_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Gradient 2 penalty:", None))
#if QT_CONFIG(tooltip)
        self.controlsFit_pushButton.setToolTip(QCoreApplication.translate("FieldFitterWidget", u"<html><head/><body><p>Fit currently highlighted field.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.controlsFit_pushButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Fit", None))
        self.display_groupBox.setTitle(QCoreApplication.translate("FieldFitterWidget", u"Display:", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Axes", None))
        self.displayDataPoints_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Data points", None))
        self.displayDataProjections_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Data projections", None))
        self.displayDataProjectionPoints_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Data projection points", None))
        self.displayDataFieldLabels_label.setText(QCoreApplication.translate("FieldFitterWidget", u"Data field label:", None))
        self.displayDataFieldLabelsNone_radioButton.setText(QCoreApplication.translate("FieldFitterWidget", u"None", None))
        self.displayDataFieldLabelsValue_radioButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Value", None))
        self.displayDataFieldLabelsDelta_radioButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Delta", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Node numbers", None))
        self.displayElementNumbers_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Element numbers", None))
        self.displayElementAxes_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Element axes", None))
        self.displayLines_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Lines", None))
        self.displayLinesExterior_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Exterior", None))
        self.displaySurfaces_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Surfaces", None))
        self.displaySurfacesExterior_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Exterior", None))
        self.displaySurfacesTranslucent_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Transluc.", None))
        self.displaySurfacesWireframe_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Wireframe", None))
        self.displayFieldColourBar_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Field colour bar", None))
        self.displayFieldContours_checkBox.setText(QCoreApplication.translate("FieldFitterWidget", u"Field contours:", None))
        self.viewAll_pushButton.setText(QCoreApplication.translate("FieldFitterWidget", u"View All", None))
        self.stdViews_pushButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Std. Views", None))
#if QT_CONFIG(tooltip)
        self.done_pushButton.setToolTip(QCoreApplication.translate("FieldFitterWidget", u"<html><head/><body><p>Fit all checked fields and end step.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.done_pushButton.setText(QCoreApplication.translate("FieldFitterWidget", u"Done", None))
    # retranslateUi

