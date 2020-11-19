"""pythonic_abstractfactory_kingdom

This module represents a kindom object.
"""
from pythonic_abstractfactory_accessoryfactory import AccessoryFactory

class Kingdom:
    """Class that uses a 'factory' to create the desired accesory.

    :cvar factory: This is a class variable that represents AccessoryFactory
                   class or its subclass.

    .. seealso:: class `AccessoryFactory`
    """
    # Define which factory class you want to use. (Redefined in subclasses)
    factory = AccessoryFactory

    def buy_accessories(self, armor_type, locket_type):
        """Create accessories using factories, pay gold and update record.

        Demonstrates how to use concrete factory classes to create accesory
        objects (without instantiating the factories)

        The pay_gold and update_records are just dummy methods.

        :arg string armor_type: Armor type to be created.
        :arg string locket_type: Locket type to be created.

        .. seealso:: pythonic_simplefactory.py
        """
        armor = self.__class__.factory.create_armor(armor_type)
        locket = self.__class__.factory.create_locket(locket_type)
        accessories = [armor, locket]
        self.pay_gold(accessories)
        self.update_records(accessories)
        self.print_info(armor, locket)

    def pay_gold(self, accessories):
        """Pay gold for the new accessories (dummy method)."""
        print("GOLD PAID!")

    def update_records(self, accessories):
        """Update some record to reflect new accessories (dummy method)."""
        print("Updated database of accessories")

    def print_info(self, armor, locket):
        """Print some information on the newly created accessories

        :arg armor: Should be an instance of an armor class e.g. IronJacket()
        :arg locket: Should be an instance of an armor class e.g. GoldLocket()
        """
        print("Done with shopping in       : {}".format(self.__class__.__name__))
        print("  concrete class for armor  : {}".format(armor.__class__.__name__))
        print("  concrete class for locket : {}".format(locket.__class__.__name__))
