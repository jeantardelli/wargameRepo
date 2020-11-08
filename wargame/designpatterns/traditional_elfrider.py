"""traditional_elfrider

This is one of the different GameUnits that are used in the desing patterns examples.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from traditional_abstractgameunit import AbstractGameUnit

class ElfRider(AbstractGameUnit):
    """Create a ElfRider object instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am a Elf Rider. Nice to meet you!")
