"""pythonic_woodelf

This is one of the different GameUnits that are used in the desing patterns 
examples. But, differently than the others, this unit represents a
third-party class that has an incompatible interface.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""

class WoodElf:
    """Create a WoodRider instance"""
    def info(self):
        """Print info about this unit, overrides superclass method."""
        print("I am an Elf from the woods! Nice to meet you!")

    def leap(self):
        """leap method is equivalent to the 'jump' method client expects.

        The adapter should have a jump method which in turn calls this
        method.
        """
        print("Inside WoodElf.leap")

    def climb(self):
        """Some other (dummy) method of the class.

        Adapter shouldn't do anything with this method. It should just
        delegate the call from the client to thid method.
        """
        print("Inside WoodElf.climb")
