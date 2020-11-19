"""python_adapter_foreignunitadapter

This method represents an adapter class that will make other game units
compatible between themselves.
"""

class ForeignUnitAdapter:
    """Generalized adapter class for 'fixing' incompatible interfaces.

    :arg adaptee: An instance of the 'adaptee' class. For example, WoodElf
                 is an adaptee as it has a method 'leap' when we expect
                 'jump'.
    :arg adaptee_method: The method you want the to adapt. Example, when
                 client calls 'jump' method on the adapter instance, it is
                 delegated to 'leap' method of the adaptee.

    :ivar foreign_unit: The instance of the adaptee class
    :ivar jump: Instance variable jump is assigned as the adaptee_method
               (e.g. 'leap')
    """
    def __init__(self, adaptee, adaptee_method):
        self.foreign_unit = adaptee
        self.jump = adaptee_method

    def __getattr__(self, item):
        """Handle all the undefined attributes the client code expects.

        :param item: name of the attribute.
        :return: Returns the corresponding attribute of the adaptee instance
                (self.foreign_unit).
        """
        return getattr(self.foreign_unit, item)
