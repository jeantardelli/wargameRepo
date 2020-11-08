"""traditional_knight

This is one of the different GameUnits that are used in the desing patterns examples.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from traditional_abstractgameunit import AbstractGameUnit

class Knight(AbstractGameUnit):
    """Create a DwarfFighter object instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("Hello, I'm the Knight!")
