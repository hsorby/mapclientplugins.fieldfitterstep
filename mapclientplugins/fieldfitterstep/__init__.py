
"""
MAP Client Plugin
"""

__version__ = '0.2.1'
__author__ = 'Auckland Bioengineering Institute'
__stepname__ = 'Field Fitter'
__location__ = 'https://github.com/ABI-Software/mapclientplugins.fieldfitterstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.fieldfitterstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
