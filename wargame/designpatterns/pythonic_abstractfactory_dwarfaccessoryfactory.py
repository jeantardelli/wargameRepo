"""pythonic_abstractfactory_dwarfaccessory

This module represents a dwarf accessory factory object.
"""
from pythonic_abstractfactory_accessoryfactory import AccessoryFactory
from pythonic_dwarfironjacket import DwarfIronJacket
from pythonic_dwarfpowersuit import DwarfPowerSuit
from pythonic_dwarfmithrilarmor import DwarfMithrilArmor
from pythonic_dwarfgoldenlocket import DwarfGoldenLocket
from pythonic_dwarfsuperlocket import DwarfSuperLocket
from pythonic_dwarfmagiclocket import DwarfMagicLocket

class DwarfAccessoryFactory(AccessoryFactory):
    """A factory for creating accessories customized for Dwarf game character.

    Redefines the class variables, armor_dict and locket_dict.

    .. seealso:: the superclass `AccessoryFactory`
    """
    # Subclasses specify their own version of these dictionaries.
    armor_dict = {
        'ironjacket': DwarfIronJacket,
        'powersuit': DwarfPowerSuit,
        'mithril': DwarfMithrilArmor
    }
    locket_dict = {
        'goldenlocket': DwarfGoldenLocket,
        'superlocket': DwarfSuperLocket,
        'magiclocket': DwarfMagicLocket
    }
