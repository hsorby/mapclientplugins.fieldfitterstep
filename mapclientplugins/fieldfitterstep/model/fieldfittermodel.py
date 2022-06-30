"""
Field Fitter model adding visualisations to github.com/ABI-Software/fieldfitter
"""
import os
import json

from opencmiss.utils.zinc.finiteelement import evaluateFieldNodesetRange
from opencmiss.utils.zinc.general import ChangeManager
from opencmiss.zinc.element import Element
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.material import Material
from opencmiss.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT
from opencmiss.zinc.scenefilter import Scenefilter
from opencmiss.zinc.spectrum import Spectrum
from fieldfitter.fitter import Fitter


class FieldFitterModel(object):
    """
    Field Fitter model adding visualisations to github.com/ABI-Software/fieldfitter
    """

    def __init__(self, inputZincModelFile, inputZincDataFile, location, identifier):
        """
        :param location: Path to folder for mapclient step name.
        """
        self._fitter = Fitter(inputZincModelFile, inputZincDataFile)
        # self._fitter.setDiagnosticLevel(1)
        self._location = os.path.join(location, identifier)
        self._identifier = identifier
        self._glyphColourBar = None
        self._initGraphicsModules()
        self._settings = {
            "displayAxes": True,
            "displayDataPoints": True,
            "displayDataProjections": False,
            "displayDataProjectionPoints": False,
            "displayDataFieldLabels": "NONE",  # or "VALUE" or "DELTA"
            "displayFieldColourBar": True,
            "displayFieldContours": False,
            "displayFieldContoursCount": 10,
            "displayNodePoints": False,
            "displayNodeNumbers": False,
            "displayElementNumbers": False,
            "displayElementFieldPoints": False,
            "displayElementAxes": False,
            "displayLines": True,
            "displayLinesExterior": False,
            "displaySurfaces": True,
            "displaySurfacesExterior": True,
            "displaySurfacesTranslucent": True,
            "displaySurfacesWireframe": False
        }
        self._loadSettings()
        self._fitter.load()
        self._currentFitFieldName = None
        self._discoverCurrentFitField()
        self._createGraphics()

    def _initGraphicsModules(self):
        context = self._fitter.getContext()
        self._materialmodule = context.getMaterialmodule()
        with ChangeManager(self._materialmodule):
            self._materialmodule.defineStandardMaterials()
            solid_blue = self._materialmodule.createMaterial()
            solid_blue.setName("solid_blue")
            solid_blue.setManaged(True)
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            solid_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
            trans_blue = self._materialmodule.createMaterial()
            trans_blue.setName("trans_blue")
            trans_blue.setManaged(True)
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            trans_blue.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.3)
            trans_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)

        spectrummodule = context.getSpectrummodule()
        defaultSpectrum = spectrummodule.getDefaultSpectrum()
        defaultSpectrum.setMaterialOverwrite(False)
        glyphmodule = context.getGlyphmodule()
        with ChangeManager(glyphmodule):
            glyphmodule.defineStandardGlyphs()
            spectrummodule = context.getSpectrummodule()
            self._glyphColourBar = glyphmodule.createGlyphColourBar(defaultSpectrum)
            self._glyphColourBar.setName("colourbar")
        tessellationmodule = context.getTessellationmodule()
        defaultTessellation = tessellationmodule.getDefaultTessellation()
        defaultTessellation.setRefinementFactors([12])

    def setDataCoordinatesField(self, field):
        self._fitter.setDataCoordinatesField(field)
        self._createGraphics()

    def setModelCoordinatesField(self, field):
        if field != self._fitter.getModelCoordinatesField():
            self._fitter.setModelCoordinatesField(field)
            self._createGraphics()

    def setFibreField(self, fibreField: Field):
        self._fitter.setFibreField(fibreField)
        self._updateGraphicsField()

    def setModelFitGroup(self, group):
        if group != self._fitter.getModelFitGroup():
            self._fitter.setModelFitGroup(group)
            self._createGraphics()

    def setGradient1Penalty(self, value):
        self._fitter.setGradient1Penalty(value)
        self._updateGraphicsField()

    def setGradient2Penalty(self, value):
        self._fitter.setGradient2Penalty(value)
        self._updateGraphicsField()

    def _discoverCurrentFitField(self):
        dataCoordinatesField = self._fitter.getDataCoordinatesField()
        dataCoordinatesFieldName = dataCoordinatesField.getName() if dataCoordinatesField else None
        modelCoordinatesField = self._fitter.getModelCoordinatesField()
        modelCoordinatesFieldName = modelCoordinatesField.getName() if modelCoordinatesField else None
        for name in self._fitter.getFitFieldNames():
            if name not in (dataCoordinatesFieldName, modelCoordinatesFieldName):
                self._currentFitFieldName = name
                self._updateGraphicsField()
                break

    def getCurrentFitFieldName(self):
        return self._currentFitFieldName

    def setCurrentFitFieldName(self, fitFieldName, isFit: bool):
        """
        :isFit: True if set to fit, otherwise False.
        :return: True on success, False if failed to set isFit flag.
        """
        result = True
        oldIsFit = self._fitter.isFitField(fitFieldName)
        result = self._fitter.setFitField(fitFieldName, isFit)
        if (fitFieldName != self._currentFitFieldName) or (oldIsFit and not isFit):
            self._currentFitFieldName = fitFieldName
            self._updateGraphicsField()
        return result

    def getCurrentFitFieldTimeCount(self):
        """
        :return: Number of times held for field parameters, or 0 if not time-varying.
        """
        if self._currentFitFieldName:
            return self._fitter.getFieldTimeCount(self._currentFitFieldName)
        return 0

    def getCurrentFitFieldTimes(self):
        """
        :return: List of times in current field time sequence, or [] if none.
        """
        if self._currentFitFieldName:
            return self._fitter.getFieldTimes(self._currentFitFieldName)
        return []

    def fitCurrentField(self):
        if self._currentFitFieldName:
            if not self._fitter.isFieldFitted(self._currentFitFieldName):
                if self._fitter.fitField(self._currentFitFieldName):
                    self._updateGraphicsField()

    def _getFitSettingsFileName(self):
        return self._location + "-settings.json"

    def _getDisplaySettingsFileName(self):
        return self._location + "-display-settings.json"

    def _loadSettings(self):
        # try:
        fitSettingsFileName = self._getFitSettingsFileName()
        if os.path.isfile(fitSettingsFileName):
            with open(fitSettingsFileName, "r") as f:
                self._fitter.decodeSettingsJSON(f.read())
        # except:
        #    print('_loadSettings FitSettings EXCEPTION')
        #    raise()
        # try:
        displaySettingsFileName = self._getDisplaySettingsFileName()
        if os.path.isfile(displaySettingsFileName):
            with open(displaySettingsFileName, "r") as f:
                savedSettings = json.loads(f.read())
                self._settings.update(savedSettings)
        # except:
        #    print('_loadSettings DisplaySettings EXCEPTION')
        #    pass

    def _saveSettings(self):
        with open(self._getFitSettingsFileName(), "w") as f:
            f.write(self._fitter.encodeSettingsJSON())
        with open(self._getDisplaySettingsFileName(), "w") as f:
            f.write(json.dumps(self._settings, sort_keys=False, indent=4))

    def getOutputModelFileNameStem(self):
        return self._location

    def getOutputModelFileName(self):
        return self._location + ".exf"

    def done(self):
        self._saveSettings()
        self._fitter.fitAllFields()
        self._fitter.writeFittedFields(self.getOutputModelFileName())

    def getIdentifier(self):
        return self._identifier

    def getContext(self):
        return self._fitter.getContext()

    def getFitter(self):
        return self._fitter

    def getRegion(self):
        return self._fitter.getRegion()

    def getFieldmodule(self):
        return self._fitter.getFieldmodule()

    def getScene(self):
        return self._fitter.getRegion().getScene()

    def _getVisibility(self, graphicsName):
        return self._settings[graphicsName]

    def _setVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        graphics = self.getScene().findGraphicsByName(graphicsName)
        graphics.setVisibilityFlag(show)

    def isDisplayAxes(self):
        return self._getVisibility("displayAxes")

    def setDisplayAxes(self, show):
        self._setVisibility("displayAxes", show)

    def isDisplayElementNumbers(self):
        return self._getVisibility("displayElementNumbers")

    def setDisplayElementNumbers(self, show):
        self._setVisibility("displayElementNumbers", show)

    def isDisplayElementFieldPoints(self):
        return self._getVisibility("displayElementFieldPoints")

    def setDisplayElementFieldPoints(self, show):
        self._setVisibility("displayElementFieldPoints", show)

    def isDisplayLines(self):
        return self._getVisibility("displayLines")

    def setDisplayLines(self, show):
        self._setVisibility("displayLines", show)

    def isDisplayLinesExterior(self):
        return self._settings["displayLinesExterior"]

    def setDisplayLinesExterior(self, isExterior):
        self._settings["displayLinesExterior"] = isExterior
        lines = self.getScene().findGraphicsByName("displayLines")
        lines.setExterior(self.isDisplayLinesExterior())

    def isDisplayDataPoints(self):
        return self._getVisibility("displayDataPoints")

    def setDisplayDataPoints(self, show):
        self._setVisibility("displayDataPoints", show)

    def isDisplayDataProjections(self):
        return self._getVisibility("displayDataProjections")

    def setDisplayDataProjections(self, show):
        self._setVisibility("displayDataProjections", show)

    def isDisplayDataProjectionPoints(self):
        return self._getVisibility("displayDataProjectionPoints")

    def setDisplayDataProjectionPoints(self, show):
        self._setVisibility("displayDataProjectionPoints", show)

    def isDisplayDataFieldLabelsNone(self):
        return self._settings["displayDataFieldLabels"] == "NONE"

    def setDisplayDataFieldLabelsNone(self):
        if self._settings["displayDataFieldLabels"] != "NONE":
            self._settings["displayDataFieldLabels"] = "NONE"
            self._updateDataFieldLabels()

    def isDisplayDataFieldLabelsValue(self):
        return self._settings["displayDataFieldLabels"] == "VALUE"

    def setDisplayDataFieldLabelsValue(self):
        if self._settings["displayDataFieldLabels"] != "VALUE":
            self._settings["displayDataFieldLabels"] = "VALUE"
            self._updateDataFieldLabels()

    def isDisplayDataFieldLabelsDelta(self):
        return self._settings["displayDataFieldLabels"] == "DELTA"

    def setDisplayDataFieldLabelsDelta(self):
        if self._settings["displayDataFieldLabels"] != "DELTA":
            self._settings["displayDataFieldLabels"] = "DELTA"
            self._updateDataFieldLabels()

    def isDisplayNodeNumbers(self):
        return self._getVisibility("displayNodeNumbers")

    def setDisplayNodeNumbers(self, show):
        self._setVisibility("displayNodeNumbers", show)

    def isDisplayNodePoints(self):
        return self._getVisibility("displayNodePoints")

    def setDisplayNodePoints(self, show):
        self._setVisibility("displayNodePoints", show)

    def isDisplaySurfaces(self):
        return self._getVisibility("displaySurfaces")

    def setDisplaySurfaces(self, show):
        self._setVisibility("displaySurfaces", show)

    def isDisplaySurfacesExterior(self):
        return self._settings["displaySurfacesExterior"]

    def setDisplaySurfacesExterior(self, isExterior):
        self._settings["displaySurfacesExterior"] = isExterior
        surfaces = self.getScene().findGraphicsByName("displaySurfaces")
        meshDimension = self._fitter.getMeshHighestDimension().getDimension()
        surfaces.setExterior(self.isDisplaySurfacesExterior() if (meshDimension == 3) else False)

    def isDisplaySurfacesTranslucent(self):
        return self._settings["displaySurfacesTranslucent"]

    def setDisplaySurfacesTranslucent(self, isTranslucent):
        self._settings["displaySurfacesTranslucent"] = isTranslucent
        surfaces = self.getScene().findGraphicsByName("displaySurfaces")
        surfacesMaterial = self._materialmodule.findMaterialByName("trans_blue" if isTranslucent else "solid_blue")
        surfaces.setMaterial(surfacesMaterial)

    def isDisplaySurfacesWireframe(self):
        return self._settings["displaySurfacesWireframe"]

    def setDisplaySurfacesWireframe(self, isWireframe):
        self._settings["displaySurfacesWireframe"] = isWireframe
        surfaces = self.getScene().findGraphicsByName("displaySurfaces")
        surfaces.setRenderPolygonMode(
            Graphics.RENDER_POLYGON_MODE_WIREFRAME if isWireframe else Graphics.RENDER_POLYGON_MODE_SHADED)

    def isDisplayFieldColourBar(self):
        return self._getVisibility("displayFieldColourBar")

    def setDisplayFieldColourBar(self, show):
        self._setVisibility("displayFieldColourBar", show)

    def isDisplayFieldContours(self):
        return self._getVisibility("displayFieldContours")

    def setDisplayFieldContours(self, show):
        self._setVisibility("displayFieldContours", show)

    def getDisplayFieldContoursCount(self) -> int:
        return self._settings["displayFieldContoursCount"]

    def setDisplayFieldContoursCount(self, count: int):
        assert count > 0
        self._settings["displayFieldContoursCount"] = count
        self._updateGraphicsFieldContours()

    def isDisplayElementAxes(self):
        return self._getVisibility("displayElementAxes")

    def setDisplayElementAxes(self, show):
        self._setVisibility("displayElementAxes", show)

    def needPerturbLines(self):
        """
        Return if solid surfaces are drawn with lines, requiring perturb lines to be activated.
        """
        region = self.getRegion()
        if region is None:
            return False
        mesh2d = region.getFieldmodule().findMeshByDimension(2)
        if mesh2d.getSize() == 0:
            return False
        return self.isDisplayLines() and self.isDisplaySurfaces() and not self.isDisplaySurfacesTranslucent()

    def getTimekeeper(self):
        return self.getContext().getTimekeepermodule().getDefaultTimekeeper()

    def _setTimes(self, times):
        """
        Set the range of times in the timekeeper.
        """
        timekeeper = self.getTimekeeper()
        minTime = 0.0
        maxTime = 0.0
        if times:
            minTime = times[0]
            maxTime = times[-1]
        timekeeper.setMinimumTime(minTime)
        timekeeper.setMaximumTime(maxTime)
        timekeeper.setTime(minTime)

    def getTime(self):
        """
        Get the current time in the timekeeper.
        """
        timekeeper = self.getTimekeeper()
        return timekeeper.getTime()

    def getTimeRange(self):
        """
        Get the range of times in the timekeeper, set for the current field.
        :return: minTime, maxTime
        """
        timekeeper = self.getTimekeeper()
        return timekeeper.getMinimumTime(), timekeeper.getMaximumTime()

    def setTime(self, time):
        """
        Set time in the timekeeper; time is restricted to be within the minimum-maximum time range.
        :return: Time actually set
        """
        timekeeper = self.getTimekeeper()
        minTime = timekeeper.getMinimumTime()
        maxTime = timekeeper.getMaximumTime()
        useTime = time
        if useTime < minTime:
            useTime = minTime
        elif useTime > maxTime:
            useTime = maxTime
        timekeeper.setTime(useTime)
        return useTime

    def _createGraphics(self):
        fieldmodule = self.getFieldmodule()
        mesh = self._fitter.getMeshHighestDimension()
        meshDimension = mesh.getDimension()
        modelCoordinates = self._fitter.getModelCoordinatesField()
        componentsCount = modelCoordinates.getNumberOfComponents()

        # prepare fields and calculate axis and glyph scaling
        with ChangeManager(fieldmodule):
            elementDerivativesField = fieldmodule.createFieldConcatenate(
                [fieldmodule.createFieldDerivative(modelCoordinates, d + 1) for d in range(meshDimension)])
            cmiss_number = fieldmodule.findFieldByName("cmiss_number")

            # get sizing for axes
            axesScale = 1.0
            nodes = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
            try:
                minX, maxX = evaluateFieldNodesetRange(modelCoordinates, nodes)
                if componentsCount == 1:
                    maxRange = maxX - minX
                else:
                    maxRange = maxX[0] - minX[0]
                    for c in range(1, componentsCount):
                        maxRange = max(maxRange, maxX[c] - minX[c])
                if maxRange > 0.0:
                    while axesScale * 10.0 < maxRange:
                        axesScale *= 10.0
                    while axesScale * 0.1 > maxRange:
                        axesScale *= 0.1
            except AssertionError:
                maxX = minX = [0.0] * componentsCount

            # fixed width glyph size is based on average element size in all dimensions
            mesh1d = fieldmodule.findMeshByDimension(1)
            lineCount = mesh1d.getSize()
            if lineCount > 0:
                one = fieldmodule.createFieldConstant(1.0)
                sumLineLength = fieldmodule.createFieldMeshIntegral(one, modelCoordinates, mesh1d)
                cache = fieldmodule.createFieldcache()
                result, totalLineLength = sumLineLength.evaluateReal(cache, 1)
                glyphWidth = 0.1 * totalLineLength / lineCount
                del cache
                del sumLineLength
                del one
            if (lineCount == 0) or (glyphWidth == 0.0):
                # use function of coordinate range if no elements
                if componentsCount == 1:
                    maxScale = maxX - minX
                else:
                    first = True
                    for c in range(componentsCount):
                        scale = maxX[c] - minX[c]
                        if first or (scale > maxScale):
                            maxScale = scale
                            first = False
                if maxScale == 0.0:
                    maxScale = 1.0
                glyphWidth = 0.01 * maxScale

        # make graphics
        scene = self.getScene()
        with ChangeManager(scene):
            scene.removeAllGraphics()

            axes = scene.createGraphicsPoints()
            pointattr = axes.getGraphicspointattributes()
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_XYZ)
            pointattr.setBaseSize([axesScale, axesScale, axesScale])
            pointattr.setLabelText(1, "  " + str(axesScale))
            axes.setMaterial(self._materialmodule.findMaterialByName("grey50"))
            axes.setName("displayAxes")
            axes.setVisibilityFlag(self.isDisplayAxes())

            # data points, projections and projection points

            dataCoordinates = self._fitter.getDataCoordinatesField()
            dataPoints = scene.createGraphicsPoints()
            dataPoints.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            if dataCoordinates:
                dataPoints.setCoordinateField(dataCoordinates)
            pointattr = dataPoints.getGraphicspointattributes()
            # pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_DIAMOND)
            # pointattr.setBaseSize([glyphWidthSmall, glyphWidthSmall, glyphWidthSmall])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_POINT)
            dataPoints.setRenderPointSize(3.0)
            dataPoints.setMaterial(self._materialmodule.findMaterialByName("grey50"))
            dataPoints.setName("displayDataPoints")
            dataPoints.setVisibilityFlag(self.isDisplayDataPoints())

            dataProjectionCoordinates = self._fitter.getDataHostCoordinatesField()
            dataProjectionDelta = self._fitter.getDataHostDeltaCoordinatesField()
            dataProjections = scene.createGraphicsPoints()
            dataProjections.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            if dataCoordinates:
                dataProjections.setCoordinateField(dataCoordinates)
            pointAttr = dataProjections.getGraphicspointattributes()
            pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_LINE)
            pointAttr.setBaseSize([0.0, 1.0, 1.0])
            pointAttr.setScaleFactors([1.0, 0.0, 0.0])
            if dataProjectionDelta:
                pointAttr.setOrientationScaleField(dataProjectionDelta)
            dataProjections.setName("displayDataProjections")
            dataProjections.setVisibilityFlag(self.isDisplayDataProjections())

            dataProjectionPoints = scene.createGraphicsPoints()
            dataProjectionPoints.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            if dataProjectionCoordinates:
                dataProjectionPoints.setCoordinateField(dataProjectionCoordinates)
            pointattr = dataProjectionPoints.getGraphicspointattributes()
            # pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_DIAMOND)
            # pointattr.setBaseSize([glyphWidthSmall, glyphWidthSmall, glyphWidthSmall])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_POINT)
            dataProjectionPoints.setRenderPointSize(3.0)
            dataProjectionPoints.setMaterial(self._materialmodule.findMaterialByName("grey50"))
            dataProjectionPoints.setName("displayDataProjectionPoints")
            dataProjectionPoints.setVisibilityFlag(self.isDisplayDataProjectionPoints())

            nodePoints = scene.createGraphicsPoints()
            nodePoints.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            nodePoints.setCoordinateField(modelCoordinates)
            pointattr = nodePoints.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidth, glyphWidth, glyphWidth])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
            nodePoints.setMaterial(self._materialmodule.findMaterialByName("white"))
            nodePoints.setName("displayNodePoints")
            nodePoints.setVisibilityFlag(self.isDisplayNodePoints())

            nodeNumbers = scene.createGraphicsPoints()
            nodeNumbers.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            nodeNumbers.setCoordinateField(modelCoordinates)
            pointattr = nodeNumbers.getGraphicspointattributes()
            pointattr.setLabelField(cmiss_number)
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
            nodeNumbers.setMaterial(self._materialmodule.findMaterialByName("green"))
            nodeNumbers.setName("displayNodeNumbers")
            nodeNumbers.setVisibilityFlag(self.isDisplayNodeNumbers())

            elementNumbers = scene.createGraphicsPoints()
            elementNumbers.setFieldDomainType(Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION)
            elementNumbers.setCoordinateField(modelCoordinates)
            pointattr = elementNumbers.getGraphicspointattributes()
            pointattr.setLabelField(cmiss_number)
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
            elementNumbers.setMaterial(self._materialmodule.findMaterialByName("cyan"))
            elementNumbers.setName("displayElementNumbers")
            elementNumbers.setVisibilityFlag(self.isDisplayElementNumbers())

            elementFieldPoints = scene.createGraphicsPoints()
            elementFieldPoints.setFieldDomainType(Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION)
            elementFieldPoints.setCoordinateField(modelCoordinates)
            pointattr = elementFieldPoints.getGraphicspointattributes()
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_POINT)
            sampleattr = elementFieldPoints.getGraphicssamplingattributes()
            sampleattr.setElementPointSamplingMode(Element.POINT_SAMPLING_MODE_CELL_CORNERS)
            elementFieldPoints.setRenderPointSize(2.0)
            elementFieldPoints.setMaterial(self._materialmodule.findMaterialByName("grey50"))
            tessellationmodule = self.getContext().getTessellationmodule()
            defaultTessellation = tessellationmodule.getDefaultTessellation()
            elementFieldPoints.setTessellation(defaultTessellation)
            elementFieldPoints.setName("displayElementFieldPoints")
            elementFieldPoints.setVisibilityFlag(self.isDisplayElementFieldPoints())

            elementAxes = scene.createGraphicsPoints()
            elementAxes.setFieldDomainType(Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION)
            elementAxes.setCoordinateField(modelCoordinates)
            pointattr = elementAxes.getGraphicspointattributes()
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_123)
            pointattr.setOrientationScaleField(elementDerivativesField)
            if meshDimension == 1:
                pointattr.setBaseSize([0.0, 2 * glyphWidth, 2 * glyphWidth])
                pointattr.setScaleFactors([0.25, 0.0, 0.0])
            elif meshDimension == 2:
                pointattr.setBaseSize([0.0, 0.0, 2 * glyphWidth])
                pointattr.setScaleFactors([0.25, 0.25, 0.0])
            else:
                pointattr.setBaseSize([0.0, 0.0, 0.0])
                pointattr.setScaleFactors([0.25, 0.25, 0.25])
            elementAxes.setMaterial(self._materialmodule.findMaterialByName("yellow"))
            elementAxes.setName("displayElementAxes")
            elementAxes.setVisibilityFlag(self.isDisplayElementAxes())

            lines = scene.createGraphicsLines()
            lines.setCoordinateField(modelCoordinates)
            lines.setExterior(self.isDisplayLinesExterior())
            lines.setName("displayLines")
            lines.setVisibilityFlag(self.isDisplayLines())

            surfaces = scene.createGraphicsSurfaces()
            surfaces.setCoordinateField(modelCoordinates)
            surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_WIREFRAME if self.isDisplaySurfacesWireframe()
                                          else Graphics.RENDER_POLYGON_MODE_SHADED)
            surfaces.setExterior(self.isDisplaySurfacesExterior() if (meshDimension == 3) else False)
            surfacesMaterial = self._materialmodule.findMaterialByName(
                "trans_blue" if self.isDisplaySurfacesTranslucent() else "solid_blue")
            surfaces.setMaterial(surfacesMaterial)
            surfaces.setName("displaySurfaces")
            surfaces.setVisibilityFlag(self.isDisplaySurfaces())

            colourBar = scene.createGraphicsPoints()
            colourBar.setScenecoordinatesystem(SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT)
            pointattr = colourBar.getGraphicspointattributes()
            pointattr.setGlyph(self._glyphColourBar)
            pointattr.setBaseSize([1.0, 1.0, 1.0])
            pointattr.setGlyphOffset([-0.9, 0.0, 0.0])
            colourBar.setName("displayFieldColourBar")
            colourBar.setVisibilityFlag(self.isDisplayFieldColourBar())

            self._updateGraphicsField()

    def _updateGraphicsField(self):
        """
        Enable data colouring if there is a current field, and autorange spectrum for it.
        """
        isFieldFitted = False
        field = Field()
        scene = self.getScene()
        spectrummodule = scene.getSpectrummodule()
        defaultSpectrum = spectrummodule.getDefaultSpectrum()
        times = []
        if self._currentFitFieldName:
            isFieldFitted = self._fitter.isFieldFitted(self._currentFitFieldName)
            field = self.getFieldmodule().findFieldByName(self._currentFitFieldName)
            times = self._fitter.getFieldTimes(self._currentFitFieldName)
            self._setTimes(times)

        modelFitGroup = self._fitter.getModelFitGroup()
        if not modelFitGroup:
            modelFitGroup = Field()

        # make graphics
        with ChangeManager(scene):
            dataPoints = scene.findGraphicsByName("displayDataPoints")
            dataPoints.setDataField(field)
            dataPoints.setSpectrum(defaultSpectrum if field.isValid() else Spectrum())

            elementFieldPoints = scene.findGraphicsByName("displayElementFieldPoints")
            elementFieldPoints.setSubgroupField(modelFitGroup)
            elementFieldPoints.setDataField(field if isFieldFitted else Field())
            elementFieldPoints.setSpectrum(defaultSpectrum if isFieldFitted else Spectrum())

            surfaces = scene.findGraphicsByName("displaySurfaces")
            surfaces.setSubgroupField(modelFitGroup)
            surfaces.setDataField(field if isFieldFitted else Field())
            surfaces.setSpectrum(defaultSpectrum if isFieldFitted else Spectrum())

            contours = scene.findGraphicsByName("displayFieldContours")
            if contours.isValid():
                scene.removeGraphics(contours)
                del contours

        # workaround: getSpectrumDataRange() is not correct for timekeeper time during with ChangeManager(scene):
        with ChangeManager(spectrummodule):
            if times:
                minFieldValue = None
                maxFieldValue = None
                componentCount = field.getNumberOfComponents()
                for time in reversed(times):  # so we end at lowest time
                    self.setTime(time)
                    result, vMin, vMax = scene.getSpectrumDataRange(Scenefilter(), defaultSpectrum, componentCount)
                    if componentCount > 1:
                        vMin = vMin[0]
                        vMax = vMax[0]
                    if minFieldValue is None:
                        minFieldValue = vMin
                        maxFieldValue = vMax
                    else:
                        if vMin < minFieldValue:
                            minFieldValue = vMin
                        if vMax > maxFieldValue:
                            maxFieldValue = vMax
                spectrumcomponent = defaultSpectrum.getFirstSpectrumcomponent()
                spectrumcomponent.setRangeMinimum(minFieldValue)
                spectrumcomponent.setRangeMaximum(maxFieldValue)
            else:
                defaultSpectrum.autorange(scene, Scenefilter())

        with ChangeManager(scene):
            if field.isValid():
                self._updateDataFieldLabels()

            if isFieldFitted:
                self._updateGraphicsFieldContours()

    def _updateDataFieldLabels(self):
        """
        Show current DataFieldLabels state.
        """
        isFieldFitted = self._fitter.isFieldFitted(self._currentFitFieldName) if self._currentFitFieldName else False
        field = self.getFieldmodule().findFieldByName(self._currentFitFieldName) if self._currentFitFieldName else None
        scene = self.getScene()
        with ChangeManager(scene):
            dataPoints = scene.findGraphicsByName("displayDataPoints")
            pointattr = dataPoints.getGraphicspointattributes()
            if self.isDisplayDataFieldLabelsValue():
                pointattr.setLabelField(field)
            elif isFieldFitted and self.isDisplayDataFieldLabelsDelta():
                fieldmodule = self.getFieldmodule()
                with ChangeManager(fieldmodule):
                    hostField = fieldmodule.createFieldEmbedded(field, self._fitter.getDataHostLocationField())
                    delta = field - hostField
                    pointattr.setLabelField(delta)
            else:
                pointattr.setLabelField(Field())  # none

    def _updateGraphicsFieldContours(self):
        """
        Assume spectrum has correct range.
        """
        field = self.getFieldmodule().findFieldByName(self._currentFitFieldName) if self._currentFitFieldName else None
        if (not field) or (field.getNumberOfComponents() > 1) or (not self._fitter.isFieldFitted(field.getName())):
            return
        modelFitGroup = self._fitter.getModelFitGroup()
        if not modelFitGroup:
            modelFitGroup = Field()
        scene = self.getScene()
        spectrummodule = scene.getSpectrummodule()
        defaultSpectrum = spectrummodule.getDefaultSpectrum()
        spectrumcomponent = defaultSpectrum.getFirstSpectrumcomponent()
        minValue = spectrumcomponent.getRangeMinimum()
        maxValue = spectrumcomponent.getRangeMaximum()
        count = self.getDisplayFieldContoursCount()
        delta = (maxValue - minValue) / (2.0 * count)
        with ChangeManager(scene):
            contours = scene.findGraphicsByName("displayFieldContours").castContours()
            if not contours.isValid():
                contours = scene.createGraphicsContours()
                contours.setCoordinateField(self._fitter.getModelCoordinatesField())
                contours.setIsoscalarField(field)
                contours.setDataField(field)
                contours.setSpectrum(defaultSpectrum)
                contours.setName("displayFieldContours")
                contours.setVisibilityFlag(self.isDisplayFieldContours())
            contours.setSubgroupField(modelFitGroup)
            contours.setRangeIsovalues(count, minValue + delta, maxValue - delta)
