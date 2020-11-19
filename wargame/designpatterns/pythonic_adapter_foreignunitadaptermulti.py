"""python_adapter_foreignunitadaptermulti

This method represents an adapter class that will make other game units
compatible between themselves.
"""

class ForeignUnitAdapterMulti:
    """Generalized adapter class for 'fixing' incompatible interfaces.

    :arg adaptee: An instance of the 'adaptee' class. For example, WoodElf
                 is an adaptee as it has a method 'leap' when we expect
                 'jump'.

    :ivar foreign_unit: The instance of the adaptee class
    """
    def __init__(self, adaptee):
        self.foreign_unit = adaptee

    def __getattr__(self, item):
        """Handle all the undefined attributes the client code expects.

        :param item: name of the attribute.
        :return: Returns the corresponding attribute of the adaptee instance
                (self.foreign_unit).
        """
        return getattr(self.foreign_unit, item)

    def set_adapter(self, name, adaptee_method):
        """Convenience method to set a new attribute to this class

        :arg name: Name of the new attribute.
        :arg adaptee_method: The 'value' of the new attribute.
             Example: setattr(self, 'jump', 'foo_elf.leap') is equivalent to
                      sayng self.jump = foo_elf.leap
        """
        setattr(self, name, adaptee_method)
