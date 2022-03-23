"""
Created on Jul 23, 2015

@author: Richard Christie
"""
from opencmiss.maths.vectorops import add, matrix_vector_mult
from opencmiss.utils.zinc.general import ChangeManager
from opencmiss.zinc.node import Node, Nodeset
from opencmiss.zinc.field import Field, FieldGroup
from opencmiss.zinc.scene import Scene
from opencmiss.zinc.status import OK as ZINC_OK


def copyNodalParameters(sourceField, targetField, time = 0.0):
    """
    Copy nodal parameters from sourceField to identically defined targetField.
    Assumes they are in the same field module.
    :param sourceField: the field to copy from
    :param targetField: the field to copy to
    :param optional time
    :return: True on success, otherwise false
    """
    ncomp = sourceField.getNumberOfComponents()
    if targetField.getNumberOfComponents() != ncomp:
        print('zinc.copyNodalParameters: fields must have same number of components')
        return False
    sourceFeField = sourceField.castFiniteElement()
    targetFeField = targetField.castFiniteElement()
    if not (sourceFeField.isValid() and targetFeField.isValid()):
        print('zinc.copyNodalParameters: fields must be finite element type')
        return False
    success = True
    fm = sourceFeField.getFieldmodule()
    fm.beginChange()
    cache = fm.createFieldcache()
    cache.setTime(time)
    nodes = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
    nodetemplate = nodes.createNodetemplate()
    nodeIter = nodes.createNodeiterator()
    node = nodeIter.next()
    while node.isValid():
        nodetemplate.defineFieldFromNode(sourceFeField, node)
        cache.setNode(node)
        for derivative in [Node.VALUE_LABEL_VALUE, Node.VALUE_LABEL_D_DS1, Node.VALUE_LABEL_D_DS2, Node.VALUE_LABEL_D2_DS1DS2,
                           Node.VALUE_LABEL_D_DS3, Node.VALUE_LABEL_D2_DS1DS3, Node.VALUE_LABEL_D2_DS2DS3, Node.VALUE_LABEL_D3_DS1DS2DS3]:
            versions = nodetemplate.getValueNumberOfVersions(sourceFeField, -1, derivative)
            for v in range(1, versions + 1):
                result, values = sourceFeField.getNodeParameters(cache, -1, derivative, v, ncomp)
                if result != ZINC_OK:
                    success = False
                else:
                    result = targetFeField.setNodeParameters(cache, -1, derivative, v, values)
                    if result != ZINC_OK:
                        success = False
        node = nodeIter.next()
    fm.endChange()
    if not success:
        print('zinc.copyNodalParameters: failed to get/set some values')
    return success

def transformCoordinates(field, rotationScale, offset, time = 0.0):
    """
    Transform finite element field coordinates by matrix and offset, handling nodal derivatives and versions.
    Limited to nodal parameters, rectangular cartesian coordinates
    :param field: the coordinate field to transform
    :param rotationScale: square transformation matrix 2-D array with as many rows and columns as field components.
    :param offset: coordinates offset
    :return: True on success, otherwise false
    """
    ncomp = field.getNumberOfComponents()
    if ((ncomp != 2) and (ncomp != 3)):
        print('zinc.transformCoordinates: field has invalid number of components')
        return False
    if (len(rotationScale) != ncomp) or (len(offset) != ncomp):
        print('zinc.transformCoordinates: invalid matrix number of columns or offset size')
        return False
    for matRow in rotationScale:
        if len(matRow) != ncomp:
            print('zinc.transformCoordinates: invalid matrix number of columns')
            return False
    if (field.getCoordinateSystemType() != Field.COORDINATE_SYSTEM_TYPE_RECTANGULAR_CARTESIAN):
        print('zinc.transformCoordinates: field is not rectangular cartesian')
        return False
    feField = field.castFiniteElement()
    if not feField.isValid():
        print('zinc.transformCoordinates: field is not finite element field type')
        return False
    success = True
    fm = field.getFieldmodule()
    fm.beginChange()
    cache = fm.createFieldcache()
    cache.setTime(time)
    nodes = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
    nodetemplate = nodes.createNodetemplate()
    nodeIter = nodes.createNodeiterator()
    node = nodeIter.next()
    while node.isValid():
        nodetemplate.defineFieldFromNode(feField, node)
        cache.setNode(node)
        for derivative in [Node.VALUE_LABEL_VALUE, Node.VALUE_LABEL_D_DS1, Node.VALUE_LABEL_D_DS2, Node.VALUE_LABEL_D2_DS1DS2,
                           Node.VALUE_LABEL_D_DS3, Node.VALUE_LABEL_D2_DS1DS3, Node.VALUE_LABEL_D2_DS2DS3, Node.VALUE_LABEL_D3_DS1DS2DS3]:
            versions = nodetemplate.getValueNumberOfVersions(feField, -1, derivative)
            for v in range(1, versions + 1):
                result, values = feField.getNodeParameters(cache, -1, derivative, v, ncomp)
                if result != ZINC_OK:
                    success = False
                else:
                    newValues = matrix_vector_mult(rotationScale, values)
                    if derivative == Node.VALUE_LABEL_VALUE:
                        newValues = add(newValues, offset)
                    result = feField.setNodeParameters(cache, -1, derivative, v, newValues)
                    if result != ZINC_OK:
                        success = False
        node = nodeIter.next()
    fm.endChange()
    if not success:
        print('zinc.transformCoordinates: failed to get/set some values')
    return success

def get_scene_selection_group(scene : Scene, subelementHandlingMode = FieldGroup.SUBELEMENT_HANDLING_MODE_FULL):
    """
    Get existing scene selection group of standard name.
    :param subelementHandlingMode: Mode controlling how faces, lines and nodes are
    automatically added or removed with higher dimensional elements.
    :return: Existing selection group, or None.
    """
    selection_group = scene.getSelectionField().castGroup()
    if selection_group.isValid():
        selection_group.setSubelementHandlingMode(subelementHandlingMode)
        return selection_group
    return None

selection_group_name = 'cmiss_selection'

def create_scene_selection_group(scene : Scene, subelementHandlingMode = FieldGroup.SUBELEMENT_HANDLING_MODE_FULL):
    """
    Create empty, unmanaged scene selection group of standard name.
    Should have already called get_selection_group with None returned.
    Can discover orphaned group of that name.
    :param scene: Zinc Scene to create selection for.
    :param subelementHandlingMode: Mode controlling how faces, lines and nodes are
    automatically added or removed with higher dimensional elements. Defaults to on/full.
    :return: Selection group for scene.
    """
    region = scene.getRegion()
    fieldmodule = region.getFieldmodule()
    with ChangeManager(fieldmodule):
        selection_group = fieldmodule.findFieldByName(selection_group_name)
        if selection_group.isValid():
            selection_group = selection_group.castGroup()
            if selection_group.isValid():
                selection_group.clear()
                selection_group.setManaged(False)
        if not selection_group.isValid():
            selection_group = fieldmodule.createFieldGroup()
            selection_group.setName(selection_group_name)
        selection_group.setSubelementHandlingMode(subelementHandlingMode)
    scene.setSelectionField(selection_group)
    return selection_group

def group_add_group_elements(group : FieldGroup, other_group : FieldGroup, highest_dimension_only=True):
    """
    Add to group elements from other_group.
    :param highest_dimension_only: If set (default), only add elements of
    highest dimension present in other_group, otherwise add all dimensions.
    """
    fieldmodule = group.getFieldmodule()
    with ChangeManager(fieldmodule):
        for dimension in range(3, 0, -1):
            mesh = fieldmodule.findMeshByDimension(dimension)
            other_element_group = other_group.getFieldElementGroup(mesh)
            if other_element_group.isValid() and (other_element_group.getMeshGroup().getSize() > 0):
                element_group = group.getFieldElementGroup(mesh)
                if not element_group.isValid():
                    element_group = group.createFieldElementGroup(mesh)
                mesh_group = element_group.getMeshGroup()
                mesh_group.addElementsConditional(other_element_group)
                if highest_dimension_only:
                    break

def group_add_group_nodes(group : FieldGroup, other_group : FieldGroup, nodeset : Nodeset):
    """
    Add to group elements and/or nodes from other_group.
    :param nodeset: Nodeset to add nodes from.
    """
    other_node_group = other_group.getFieldNodeGroup(nodeset)
    if other_node_group.isValid() and (other_node_group.getNodesetGroup().getSize() > 0):
        node_group = group.getFieldNodeGroup(nodeset)
        if not node_group.isValid():
            node_group = group.createFieldNodeGroup(nodeset)
        nodeset_group = node_group.getNodesetGroup()
        nodeset_group.addNodesConditional(other_group.getFieldNodeGroup(nodeset))

def field_is_managed_real_1_to_3_components(field_in: Field):
    """
    Conditional function returning True if the field is real-valued
    with up to 3 components, and is managed.
    """
    return (field_in.getValueType() == Field.VALUE_TYPE_REAL) and \
        (field_in.getNumberOfComponents() <= 3) and field_in.isManaged()
