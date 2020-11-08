"""pythonic_fairy

This is one of the different GameUnits that are used in the desing patterns examples.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from pythonic_abstractgameunit import AbstractGameUnit

class Fairy(AbstractGameUnit):
    """Create a Fairy instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("Hi, like the stars I am :)")
