"""pythonic_abstractfactory_accessoryfactory

This module represents an accessory factory object.
"""
from pythonic_ironjacket import IronJacket
from pythonic_powersuit import PowerSuit
from pythonic_mithrilarmor import MithrilArmor
from pythonic_goldenlocket import GoldenLocket
from pythonic_superlocket import SuperLocket
from pythonic_magiclocket import MagicLocket

class AccessoryFactory:
    """A factory base class to create various game accessories.

    This is an example that shows how we can use Python classes (which are
    first-class objects) and a class method to represent an abstract factory.
    In this example, the client does not instantiates factory.

    :cvar armor_dict: Python dictionary created as a class variable. This
            dictionary holds names of the armor accessories as its keys and
            the corresponding values are the concrete classes representing the
            armor accessory for the game units. This class variable may be
            overriden is subclasses.
    :cvar armor_dict: Similar to `armor_dict`, a dictionary created as a class
            variable to hold concrete classes representing the 'locket'
            accessory. This class variable may be overriden in subclasses.

    .. seealso:: `Kingdom.buy_accessories`, `DwarfKingdom`
                  Also review the code in `pythonic_simplefactory.py`
    """
    # Subclasses specify their own version of these dictionaries.
    armor_dict = {
        'ironjacket': IronJacket,
        'powersuit': PowerSuit,
        'mithril': MithrilArmor
    }
    locket_dict = {
        'goldenlocket': GoldenLocket,
        'superlocket': SuperLocket,
        'magiclocket': MagicLocket
    }

    @classmethod
    def create_armor(cls, armor_type):
        """Return an instance of an armor accessory

        This is a class method and it uses the class variable armor_dict to
        create and return an instance of an armor accessory (e.g. IronJacket(),
        PowerSuit(), etc.)

        :arg string armor_type: A string representing the armor type
        :return: Instance of an armor accessory such as IronJacket().
        """
        return cls.armor_dict.get(armor_type)()

    @classmethod
    def create_locket(cls, locket_type):
        """Return an instance of a locket accessory

        This is a class method and it uses the class variable locket_dict to
        create and return an instance of an armor accessory (e.g.
        GoldenLocket(), etc).
        """
        return cls.locket_dict.get(locket_type)()
