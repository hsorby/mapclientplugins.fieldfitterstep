"""
User interface for github.com/ABI-Software/fieldfitter
"""
import webbrowser

from PySide6 import QtCore, QtGui, QtWidgets

from cmlibs.maths.vectorops import dot, magnitude, mult, normalize, sub
from cmlibs.utils.zinc.field import field_is_managed_coordinates, field_is_managed_group, \
    field_is_managed_real_1_to_3_components
from cmlibs.widgets.collapsibleboxwidget import CollapsibleBox
from cmlibs.widgets.helpers.widgetvisibility import setting_visibility
from cmlibs.widgets.ui.ui_buttonswidget import Ui_Buttons
from cmlibs.widgets.ui.ui_displaysettingswidget import Ui_DisplaySettings
from cmlibs.widgets.utils import parse_vector, parse_real

from mapclientplugins.fieldfitterstep.view.ui_fieldfitterwidget import Ui_FieldFitterWidget
from mapclientplugins.fieldfitterstep.view.ui_initialconfigwidget import Ui_InitialConfig
from mapclientplugins.fieldfitterstep.view.ui_fitfieldswidget import Ui_FitFields


realFormat = "{:.4g}"


class FieldFitterWidget(QtWidgets.QMainWindow):
    """
    User interface for github.com/ABI-Software/fieldfitter
    """

    def __init__(self, model, parent=None):
        super(FieldFitterWidget, self).__init__(parent)
        self._model = model
        self._ui = Ui_FieldFitterWidget()
        self._ui.setupUi(self)
        self._setup_dock_widget()
        self._ui.sceneviewerwidget.setContext(model.getContext())
        self._fitter = self._model.getFitter()
        self._region = self._fitter.getRegion()
        self._scene = self._region.getScene()
        self._ui.sceneviewerwidget.graphicsInitialized.connect(self._graphicsInitialized)
        self._callback = None
        self._setupFitWidgets()
        self._updateFitWidgets()
        self._makeConnectionsFit()
        self._updateDisplayWidgets()
        self._makeConnectionsDisplay()

    def _setup_dock_widget(self):
        """
        Set up the dock widget for the field fitter.
        """
        parent_widget = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(parent_widget)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        self._identifier_label = QtWidgets.QLabel("Field Fitter Identifier: " + self._model.getIdentifier())
        layout.addWidget(self._identifier_label)

        self._initial_config_ui = Ui_InitialConfig()
        self._fit_fields_ui = Ui_FitFields()
        self._display_settings_ui = Ui_DisplaySettings()
        self._buttons_ui = Ui_Buttons()

        for ui in [self._initial_config_ui, self._fit_fields_ui, self._display_settings_ui]:
            form_container = QtWidgets.QWidget()
            ui.setupUi(form_container)
            tools_box = CollapsibleBox(form_container.windowTitle(), checked=True if ui is self._initial_config_ui else False)
            tools_box.add_widget(form_container)
            layout.addWidget(tools_box, stretch=1)

        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        layout.addSpacerItem(spacer)

        form_container = QtWidgets.QWidget()
        self._buttons_ui.setupUi(form_container)
        layout.addWidget(form_container)

        setting_visibility(self._display_settings_ui, 'fieldfitter')

        self._dock_widget = QtWidgets.QDockWidget("Controls", self)
        self._dock_widget.setObjectName("ControlsDock")
        self._dock_widget.setWidget(parent_widget)

        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, self._dock_widget)

    def _graphicsInitialized(self):
        """
        Callback for when SceneviewerWidget is initialised
        """
        self._sceneChanged()
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            self._autoPerturbLines()
            sceneviewer.viewAll()

    def _sceneChanged(self):
        """
        Set custom scene from model.
        """
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setScene(self._model.getScene())

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _autoPerturbLines(self):
        """
        Enable scene viewer perturb lines iff solid surfaces are drawn with lines.
        Call whenever lines, surfaces or translucency changes
        """
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setPerturbLinesFlag(self._model.needPerturbLines())

    # === fit widgets ===

    def _setupFitWidgets(self):
        """
        Set up config widgets and display values from fitter object.
        """
        self._initial_config_ui.configDataCoordinates_fieldChooser.setRegion(self._region)
        self._initial_config_ui.configDataCoordinates_fieldChooser.setNullObjectName("-")
        self._initial_config_ui.configDataCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._initial_config_ui.configModelCoordinates_fieldChooser.setRegion(self._region)
        self._initial_config_ui.configModelCoordinates_fieldChooser.setNullObjectName("-")
        self._initial_config_ui.configModelCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._initial_config_ui.configModelFitGroup_fieldChooser.setRegion(self._region)
        self._initial_config_ui.configModelFitGroup_fieldChooser.setNullObjectName("-")
        self._initial_config_ui.configModelFitGroup_fieldChooser.setConditional(field_is_managed_group)
        self._initial_config_ui.configFibreOrientation_fieldChooser.setRegion(self._region)
        self._initial_config_ui.configFibreOrientation_fieldChooser.setNullObjectName("-")
        self._initial_config_ui.configFibreOrientation_fieldChooser.setConditional(field_is_managed_real_1_to_3_components)
        self._buildFitFieldsListView()

    def _makeConnectionsFit(self):
        self._initial_config_ui.configDataCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configDataCoordinatesFieldChanged)
        self._initial_config_ui.configModelCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configModelCoordinatesFieldChanged)
        self._initial_config_ui.configModelFitGroup_fieldChooser.currentIndexChanged.connect(self._configModelFitGroupChanged)
        self._initial_config_ui.configFibreOrientation_fieldChooser.currentIndexChanged.connect(
            self._configFibreOrientationFieldChanged)
        self._initial_config_ui.configDiagnosticLevel_spinBox.valueChanged.connect(self._configDiagnosticLevelValueChanged)
        self._fit_fields_ui.fitFieldsCheckAll_pushButton.clicked.connect(self._fitFieldCheckAllButtonClicked)
        self._fit_fields_ui.fitFieldsCheckNone_pushButton.clicked.connect(self._fitFieldCheckNoneButtonClicked)
        self._fit_fields_ui.fitFields_listView.clicked[QtCore.QModelIndex].connect(self._fitFieldListItemClicked)
        self._fit_fields_ui.parametersGradient1Penalty_lineEdit.editingFinished.connect(
            self._parametersGradient1PenaltyEntered)
        self._fit_fields_ui.parametersGradient2Penalty_lineEdit.editingFinished.connect(
            self._parametersGradient2PenaltyEntered)
        self._fit_fields_ui.controlsFit_pushButton.clicked.connect(self._fitButtonClicked)
        self._buttons_ui.pushButtonDocumentation.clicked.connect(self._documentationButtonClicked)
        self._buttons_ui.done_pushButton.clicked.connect(self._doneButtonClicked)

    def _updateFitWidgets(self):
        """
        Update fit widgets to display settings for Fitter.
        """
        self._identifier_label.setText("Field Fitter Identifier:  " + self._model.getIdentifier())
        self._initial_config_ui.configDataCoordinates_fieldChooser.setField(self._fitter.getDataCoordinatesField())
        self._initial_config_ui.configModelCoordinates_fieldChooser.setField(self._fitter.getModelCoordinatesField())
        self._initial_config_ui.configModelFitGroup_fieldChooser.setField(self._fitter.getModelFitGroup())
        self._initial_config_ui.configFibreOrientation_fieldChooser.setField(self._fitter.getFibreField())
        self._initial_config_ui.configDiagnosticLevel_spinBox.setValue(self._fitter.getDiagnosticLevel())
        self._updateFitFieldsListView()
        self._updateParametersGradient1Penalty()
        self._updateParametersGradient2Penalty()

    def _configDataCoordinatesFieldChanged(self, index):
        """
        Callback for change in data coordinates field chooser widget.
        """
        field = self._initial_config_ui.configDataCoordinates_fieldChooser.getField()
        if field:
            self._model.setDataCoordinatesField(field)
            self._updateFitFieldsListView()

    def _configModelCoordinatesFieldChanged(self, index):
        """
        Callback for change in model coordinates field chooser widget.
        """
        field = self._initial_config_ui.configModelCoordinates_fieldChooser.getField()
        if field:
            self._model.setModelCoordinatesField(field)
            self._updateFitFieldsListView()

    def _configModelFitGroupChanged(self, index):
        """
        Callback for change in fit group field chooser widget.
        """
        group = self._initial_config_ui.configModelFitGroup_fieldChooser.getField()
        if group:
            group = group.castGroup()
            if not group.isValid():
                group = None
        self._model.setModelFitGroup(group)

    def _configFibreOrientationFieldChanged(self, index):
        """
        Callback for change in model coordinates field chooser widget.
        """
        self._model.setFibreField(self._initial_config_ui.configFibreOrientation_fieldChooser.getField())

    def _configDiagnosticLevelValueChanged(self, value):
        self._fitter.setDiagnosticLevel(value)

    def _fitFieldCheckAllButtonClicked(self):
        for name in self._fitter.getFitFieldNames():
            self._fitter.setFitField(name, True)
        self._updateFitFieldsListView()

    def _fitFieldCheckNoneButtonClicked(self):
        for name in self._fitter.getFitFieldNames():
            self._fitter.setFitField(name, False)
        self._updateFitFieldsListView()

    def _buildFitFieldsListView(self):
        """
        Add a checkable item for each fit field.
        """
        fitFieldModel = QtGui.QStandardItemModel(self._fit_fields_ui.fitFields_listView)
        fitFieldNames = self._fitter.getFitFieldNames()
        for fitFieldName in fitFieldNames:
            displayName = fitFieldName
            timeCount = self._fitter.getFieldTimeCount(fitFieldName)
            if timeCount:
                displayName += " (" + str(timeCount) + " times)"
            item = QtGui.QStandardItem(displayName)
            item.setData(fitFieldName)
            item.setEditable(False)
            item.setCheckable(True)
            fitFieldModel.appendRow(item)
        self._fit_fields_ui.fitFields_listView.setModel(fitFieldModel)
        self._fit_fields_ui.fitFields_listView.show()

    def _updateFitFieldsListView(self):
        """
        Select current fitField. Ensure coordinate fields are unchecked and disabled.
        """
        dataCoordinatesField = self._fitter.getDataCoordinatesField()
        dataCoordinatesFieldName = dataCoordinatesField.getName() if dataCoordinatesField else None
        modelCoordinatesField = self._fitter.getModelCoordinatesField()
        modelCoordinatesFieldName = modelCoordinatesField.getName() if modelCoordinatesField else None
        currentFitFieldName = self._model.getCurrentFitFieldName()
        fitFieldModel = self._fit_fields_ui.fitFields_listView.model()
        for row in range(fitFieldModel.rowCount()):
            index = fitFieldModel.index(row, 0)
            item = fitFieldModel.itemFromIndex(index)
            name = item.data()
            if name in (dataCoordinatesFieldName, modelCoordinatesFieldName):
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item.setEnabled(False)
            else:
                item.setCheckState(QtCore.Qt.CheckState.Checked if self._fitter.isFitField(name) else QtCore.Qt.CheckState.Unchecked)
                item.setEnabled(True)
            if name == currentFitFieldName:
                self._fit_fields_ui.fitFields_listView.setCurrentIndex(index)

    def _fitFieldListItemClicked(self, modelIndex):
        """
        Changes current fit field.
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        fitFieldName = item.data()
        if not self._model.setCurrentFitFieldName(fitFieldName, item.checkState() == QtCore.Qt.CheckState.Checked):
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self._updateTimeWidgets()

    def _updateParametersGradient1Penalty(self):
        s = ", ".join(realFormat.format(e) for e in self._fitter.getGradient1Penalty())
        self._fit_fields_ui.parametersGradient1Penalty_lineEdit.setText(s)

    def _parametersGradient1PenaltyEntered(self):
        value = parse_vector(self._fit_fields_ui.parametersGradient1Penalty_lineEdit)
        self._model.setGradient1Penalty(value)
        self._updateParametersGradient1Penalty()

    def _updateParametersGradient2Penalty(self):
        s = ", ".join(realFormat.format(e) for e in self._fitter.getGradient2Penalty())
        self._fit_fields_ui.parametersGradient2Penalty_lineEdit.setText(s)

    def _parametersGradient2PenaltyEntered(self):
        value = parse_vector(self._fit_fields_ui.parametersGradient2Penalty_lineEdit)
        self._model.setGradient2Penalty(value)
        self._updateParametersGradient2Penalty()

    def _fitButtonClicked(self):
        # following will tick the field if not already
        update = not self._fitter.isFitField(self._model.getCurrentFitFieldName())
        self._model.fitCurrentField()
        if update:
            self._updateFitFieldsListView()
        self._updateTimeWidgets()

    def _documentationButtonClicked(self):
        webbrowser.open("https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.fieldfitterstep/docs/index.html")

    def _doneButtonClicked(self):
        self._model.done()
        self._dock_widget.setFloating(False)
        self._callback()

    # === display widgets ===

    def _makeConnectionsDisplay(self):
        self._display_settings_ui.displayAxes_checkBox.clicked.connect(self._displayAxesClicked)
        self._display_settings_ui.displayDataPoints_checkBox.clicked.connect(self._displayDataPointsClicked)
        self._display_settings_ui.displayDataProjections_checkBox.clicked.connect(self._displayDataProjectionsClicked)
        self._display_settings_ui.displayDataProjectionPoints_checkBox.clicked.connect(self._displayDataProjectionPointsClicked)
        self._display_settings_ui.displayDataFieldLabelsNone_radioButton.toggled.connect(self._displayDataFieldLabelsNoneToggled)
        self._display_settings_ui.displayDataFieldLabelsValue_radioButton.toggled.connect(self._displayDataFieldLabelsValueToggled)
        self._display_settings_ui.displayDataFieldLabelsDelta_radioButton.toggled.connect(self._displayDataFieldLabelsDeltaToggled)
        self._display_settings_ui.displayNodePoints_checkBox.clicked.connect(self._displayNodePointsClicked)
        self._display_settings_ui.displayNodeNumbers_checkBox.clicked.connect(self._displayNodeNumbersClicked)
        self._display_settings_ui.displayElementAxes_checkBox.clicked.connect(self._displayElementAxesClicked)
        self._display_settings_ui.displayElementFieldPoints_checkBox.clicked.connect(self._displayElementFieldPointsClicked)
        self._display_settings_ui.displayElementNumbers_checkBox.clicked.connect(self._displayElementNumbersClicked)
        self._display_settings_ui.displayLines_checkBox.clicked.connect(self._displayLinesClicked)
        self._display_settings_ui.displayLinesExterior_checkBox.clicked.connect(self._displayLinesExteriorClicked)
        self._display_settings_ui.displaySurfaces_checkBox.clicked.connect(self._displaySurfacesClicked)
        self._display_settings_ui.displaySurfacesExterior_checkBox.clicked.connect(self._displaySurfacesExteriorClicked)
        self._display_settings_ui.displaySurfacesTranslucent_checkBox.clicked.connect(self._displaySurfacesTranslucentClicked)
        self._display_settings_ui.displaySurfacesWireframe_checkBox.clicked.connect(self._displaySurfacesWireframeClicked)
        self._display_settings_ui.displayFieldColourBar_checkBox.clicked.connect(self._displayFieldColourBarClicked)
        self._display_settings_ui.displayFieldContours_checkBox.clicked.connect(self._displayFieldContoursClicked)
        self._display_settings_ui.displayFieldContoursCount_spinBox.valueChanged.connect(self._displayFieldContoursCountValueChanged)
        self._buttons_ui.stdViews_pushButton.clicked.connect(self._stdViewsButtonClicked)
        self._buttons_ui.viewAll_pushButton.clicked.connect(self._viewAllButtonClicked)
        self._display_settings_ui.displayTime_lineEdit.editingFinished.connect(self._displayTimeEntered)
        self._display_settings_ui.displayTime_horizontalSlider.valueChanged.connect(self._displayTimeSliderValueChanged)

    def _updateDisplayWidgets(self):
        """
        Update display widgets to display settings for model graphics display.
        """
        self._display_settings_ui.displayAxes_checkBox.setChecked(self._model.isDisplayAxes())
        self._display_settings_ui.displayDataPoints_checkBox.setChecked(self._model.isDisplayDataPoints())
        self._display_settings_ui.displayDataProjections_checkBox.setChecked(self._model.isDisplayDataProjections())
        self._display_settings_ui.displayDataProjectionPoints_checkBox.setChecked(self._model.isDisplayDataProjectionPoints())
        if self._model.isDisplayDataFieldLabelsNone():
            self._display_settings_ui.displayDataFieldLabelsNone_radioButton.setChecked(True)
        if self._model.isDisplayDataFieldLabelsValue():
            self._display_settings_ui.displayDataFieldLabelsValue_radioButton.setChecked(True)
        if self._model.isDisplayDataFieldLabelsDelta():
            self._display_settings_ui.displayDataFieldLabelsDelta_radioButton.setChecked(True)
        self._display_settings_ui.displayNodePoints_checkBox.setChecked(self._model.isDisplayNodePoints())
        self._display_settings_ui.displayNodeNumbers_checkBox.setChecked(self._model.isDisplayNodeNumbers())
        self._display_settings_ui.displayElementAxes_checkBox.setChecked(self._model.isDisplayElementAxes())
        self._display_settings_ui.displayElementFieldPoints_checkBox.setChecked(self._model.isDisplayElementFieldPoints())
        self._display_settings_ui.displayElementNumbers_checkBox.setChecked(self._model.isDisplayElementNumbers())
        self._display_settings_ui.displayLines_checkBox.setChecked(self._model.isDisplayLines())
        self._display_settings_ui.displayLinesExterior_checkBox.setChecked(self._model.isDisplayLinesExterior())
        self._display_settings_ui.displaySurfaces_checkBox.setChecked(self._model.isDisplaySurfaces())
        self._display_settings_ui.displaySurfacesExterior_checkBox.setChecked(self._model.isDisplaySurfacesExterior())
        self._display_settings_ui.displaySurfacesTranslucent_checkBox.setChecked(self._model.isDisplaySurfacesTranslucent())
        self._display_settings_ui.displaySurfacesWireframe_checkBox.setChecked(self._model.isDisplaySurfacesWireframe())
        self._display_settings_ui.displayFieldColourBar_checkBox.setChecked(self._model.isDisplayFieldColourBar())
        self._display_settings_ui.displayFieldContours_checkBox.setChecked(self._model.isDisplayFieldContours())
        self._display_settings_ui.displayFieldContoursCount_spinBox.setValue(self._model.getDisplayFieldContoursCount())
        self._updateTimeWidgets()

    def _displayAxesClicked(self):
        self._model.setDisplayAxes(self._display_settings_ui.displayAxes_checkBox.isChecked())

    def _displayDataPointsClicked(self):
        self._model.setDisplayDataPoints(self._display_settings_ui.displayDataPoints_checkBox.isChecked())

    def _displayDataProjectionsClicked(self):
        self._model.setDisplayDataProjections(self._display_settings_ui.displayDataProjections_checkBox.isChecked())

    def _displayDataProjectionPointsClicked(self):
        self._model.setDisplayDataProjectionPoints(self._display_settings_ui.displayDataProjectionPoints_checkBox.isChecked())

    def _displayDataFieldLabelsNoneToggled(self):
        if self._display_settings_ui.displayDataFieldLabelsNone_radioButton.isChecked():
            self._model.setDisplayDataFieldLabelsNone()

    def _displayDataFieldLabelsValueToggled(self):
        if self._display_settings_ui.displayDataFieldLabelsValue_radioButton.isChecked():
            self._model.setDisplayDataFieldLabelsValue()

    def _displayDataFieldLabelsDeltaToggled(self):
        if self._display_settings_ui.displayDataFieldLabelsDelta_radioButton.isChecked():
            self._model.setDisplayDataFieldLabelsDelta()

    def _displayNodePointsClicked(self):
        self._model.setDisplayNodePoints(self._display_settings_ui.displayNodePoints_checkBox.isChecked())

    def _displayNodeNumbersClicked(self):
        self._model.setDisplayNodeNumbers(self._display_settings_ui.displayNodeNumbers_checkBox.isChecked())

    def _displayElementAxesClicked(self):
        self._model.setDisplayElementAxes(self._display_settings_ui.displayElementAxes_checkBox.isChecked())

    def _displayElementFieldPointsClicked(self):
        self._model.setDisplayElementFieldPoints(self._display_settings_ui.displayElementFieldPoints_checkBox.isChecked())

    def _displayElementNumbersClicked(self):
        self._model.setDisplayElementNumbers(self._display_settings_ui.displayElementNumbers_checkBox.isChecked())

    def _displayLinesClicked(self):
        self._model.setDisplayLines(self._display_settings_ui.displayLines_checkBox.isChecked())
        self._autoPerturbLines()

    def _displayLinesExteriorClicked(self):
        self._model.setDisplayLinesExterior(self._display_settings_ui.displayLinesExterior_checkBox.isChecked())

    def _displaySurfacesClicked(self):
        self._model.setDisplaySurfaces(self._display_settings_ui.displaySurfaces_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesExteriorClicked(self):
        self._model.setDisplaySurfacesExterior(self._display_settings_ui.displaySurfacesExterior_checkBox.isChecked())

    def _displaySurfacesTranslucentClicked(self):
        self._model.setDisplaySurfacesTranslucent(self._display_settings_ui.displaySurfacesTranslucent_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesWireframeClicked(self):
        self._model.setDisplaySurfacesWireframe(self._display_settings_ui.displaySurfacesWireframe_checkBox.isChecked())

    def _displayFieldColourBarClicked(self):
        self._model.setDisplayFieldColourBar(self._display_settings_ui.displayFieldColourBar_checkBox.isChecked())

    def _displayFieldContoursClicked(self):
        self._model.setDisplayFieldContours(self._display_settings_ui.displayFieldContours_checkBox.isChecked())

    def _displayFieldContoursCountValueChanged(self, value):
        self._model.setDisplayFieldContoursCount(value)

    def _updateTimeWidgets(self):
        """
        Update time slider widgets.
        """
        self._display_settings_ui.displayTime_frame.setEnabled(bool(self._model.getCurrentFitFieldTimeCount()))
        time = self._model.getTime()
        self._display_settings_ui.displayTime_lineEdit.setText(realFormat.format(time))
        minValue = self._display_settings_ui.displayTime_horizontalSlider.minimum()
        self._display_settings_ui.displayTime_horizontalSlider.setValue(minValue)

    def _displayTimeEntered(self):
        oldTime = self._model.getTime()
        time = parse_real(self._display_settings_ui.displayTime_lineEdit)
        if time:
            time = self._model.setTime(time)
        else:
            time = oldTime
        self._display_settings_ui.displayTime_lineEdit.setText(realFormat.format(time))
        minValue = self._display_settings_ui.displayTime_horizontalSlider.minimum()
        maxValue = self._display_settings_ui.displayTime_horizontalSlider.maximum()
        minTime, maxTime = self._model.getTimeRange()
        value = minValue
        if maxTime > minTime:
            xi = (time - minTime) / (maxTime - minTime)
            value = int((1.0 - xi) * minValue + xi * maxValue)
        self._display_settings_ui.displayTime_horizontalSlider.setValue(value)

    def _displayTimeSliderValueChanged(self):
        """
        Time slider value has changed.
        """
        value = self._display_settings_ui.displayTime_horizontalSlider.value()
        minTime, maxTime = self._model.getTimeRange()
        minValue = self._display_settings_ui.displayTime_horizontalSlider.minimum()
        maxValue = self._display_settings_ui.displayTime_horizontalSlider.maximum()
        xi = (value - minValue) / (maxValue - minValue)
        time = (1.0 - xi) * minTime + xi * maxTime
        self._display_settings_ui.displayTime_lineEdit.setText(realFormat.format(time))
        self._model.setTime(time)

    def _stdViewsButtonClicked(self):
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            result, eyePosition, lookatPosition, upVector = sceneviewer.getLookatParameters()
            upVector = normalize(upVector)
            viewVector = sub(lookatPosition, eyePosition)
            viewDistance = magnitude(viewVector)
            viewVector = normalize(viewVector)
            # viewX = dot(viewVector, [1.0, 0.0, 0.0])
            viewY = dot(viewVector, [0.0, 1.0, 0.0])
            viewZ = dot(viewVector, [0.0, 0.0, 1.0])
            # upX = dot(upVector, [1.0, 0.0, 0.0])
            upY = dot(upVector, [0.0, 1.0, 0.0])
            upZ = dot(upVector, [0.0, 0.0, 1.0])
            if (viewZ < -0.999) and (upY > 0.999):
                # XY -> XZ
                viewVector = [0.0, 1.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            elif (viewY > 0.999) and (upZ > 0.999):
                # XZ -> YZ
                viewVector = [-1.0, 0.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            else:
                # XY
                viewVector = [0.0, 0.0, -1.0]
                upVector = [0.0, 1.0, 0.0]
            eyePosition = sub(lookatPosition, mult(viewVector, viewDistance))
            sceneviewer.setLookatParametersNonSkew(eyePosition, lookatPosition, upVector)

    def _viewAllButtonClicked(self):
        self._ui.sceneviewerwidget.viewAll()
