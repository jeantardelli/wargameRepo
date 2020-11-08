"""pythonic_unitfactory_kingdom

Example to show one way of implementing a 'simple factory' in Python.

The example shows how to use Python's language features,(classes are first-class
objects) to implement a simple factory. It also shows how to use a
factory WITHOUT instantiating it (using class method and class variables)

.. seealso: For a somewhat 'traditional' approach, see the file

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from pythonic_unitfactory import UnitFactory

class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character.

    :cvar: UnitFactory factory: This is a class variable that represents
               UnitFactory class.

    .. seealso:: class `pythonic_unitfactory.UnitFactory`
    """
    factory = UnitFactory

    def recruit(self, unit_type):
        """Recruit a new game unit, creating it first using a factory.

        This is an example that shows how we can use Python classes (which are
        first-class objects) and a class method to represent a simple factory. In
        this example, the client does not instantiates factory.

        :arg string unit_type: The type (name) of unit requested.
        :return: A game unit instance returned by the factory.
        """
        unit = self.__class__.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self, something):
        """Pay gold for the recruited unit (dummy method)."""
        print("GOLD PAID!")

    def update_records(self, something):
        """Update some record to reflect new recruit (dummy method)."""
        print("Some logic (not shown) to update database of units")
