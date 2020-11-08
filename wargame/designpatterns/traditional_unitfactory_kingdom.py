"""traditional_unitfactory_kingdom

Example to show one way of implementing a 'simple factory' in Python.

The example shown here resembles a 'traditional' implementation of a
simple factory in Python (traditional = the one you may implement in languages
like C++). For a more Pythonic approach, see the file simplefactory_pythonic.py.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""

class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character.

    :arg UnitFactory factory: A factory instance used to create new units.
    :ivar UnitFactory factory: Represents a factory instance used to create a
        new game unit.

    .. seealso:: class `UnitFactory`
    """
    def __init__(self, factory):
        self.factory = factory

    def recruit(self, unit_type):
        """Recruit a new game unit, creating it first using a factory.

        This method recruits a new unit for the 'kingdom'. First it 'orders' a
        unit from the factory instance, then pays the price and updates some
        record. The pay_gold and update_record methods are dummy, they just print
        some information.

        :arg string unit_type: The type (name) of unit requested.
        :return: A game unit instance returned by the factory.
        """
        unit = self.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self, something):
        """Pay gold for the recruited unit (dummy method)."""
        print("GOLD PAID")

    def update_records(self, something):
        """Update some record to reflect new recruit (dummy method)."""
        print("Some logic (not shown) to update database of units")
