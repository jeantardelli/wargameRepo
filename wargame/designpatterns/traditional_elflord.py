"""traditional_elflord

This is one of the different GameUnits that are used in the desing patterns examples.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from traditional_abstractgameunit import AbstractGameUnit

class ElfLord(AbstractGameUnit):
    """Create a ElfLord object instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am a Elf Lord from far away!")
