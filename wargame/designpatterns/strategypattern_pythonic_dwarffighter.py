"""strategypattern_pythonic_dwarffighter

Example to show a Pythonic way of implementing strategy desing pattern.

The example shows how to use Python's first class functions to implement
strategy pattern.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:copyright: The MIT License (MIT). See LICENSE file for further details.
"""
from strategypattern_pythonic_abstractgameunit import AbstractGameUnit

class DwarfFighter(AbstractGameUnit):
    """Create a DwarfFighter instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am a great dwarf of the eastern foo mountain!")
