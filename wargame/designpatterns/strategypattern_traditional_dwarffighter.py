"""strategypattern_traditional_dwarffighter

Example to show one way of implementing strategy design pattern in Python.

The example shown here resembles a 'traditional' implementation of trategy
pattern in Python (traditional = the one you may implement in languages like
C++). For a more Pythonic approach, see the file strategy_pythonic.py.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from strategypattern_traditional_abstractgameunit import AbstractGameUnit

class DwarfFighter(AbstractGameUnit):
    """Create a DwarfFighter object instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am a great dwarf of the eastern foo mountain!")
