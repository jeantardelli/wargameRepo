"""pythonic_dwarffighter

This is one of the different GameUnits that are used in the desing patterns examples.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from pythonic_abstractgameunit import AbstractGameUnit

class DwarfFighter(AbstractGameUnit):
    """Create a DwarfFighter instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am a great dwarf of the eastern foo mountain!")
