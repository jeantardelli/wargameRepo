"""pythonic_mountainelf

This is one of the different GameUnits that are used in the desing patterns 
examples. But, differently than the others, this unit represents a
third-party class that has an incompatible interface.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""

class MountainElf:
    """Create a MountaiElf instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am an Elf from the mountains. Nice to meet you!")

    def spring(self):
        """sping method is equivalent to the 'jump' method client expects.

        The adapter should have a jump method which in turn calls this
        method.
        """
        print("Inside MountainElf.spring")
