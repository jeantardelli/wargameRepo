"""simplefactory_pythonic_unitfactory

Example to show a Pythonic way of implementing a simple factory

The example shows how to use Python's language features,(classes are first-class
objects) to implement a simple factory. It also shows how to use a factory
WITHOUT instantiating it (using class method and class variables).

This module is compatible with Python 3.6.x

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from pythonic_dwarffighter import DwarfFighter
from pythonic_orcfighter import OrcFighter
from pythonic_orcrider import OrcRider
from pythonic_wizard import Wizard
from pythonic_fairy import Fairy
from pythonic_knight import Knight
from pythonic_elfrider import ElfRider
from pythonic_elflord import ElfLord

class UnitFactory:
    """A factory class to create game units.

    This is an exaple that shows how we can use Python classes (which are
    first-class objects) and a class method to represent a simple factory. In
    this example, the client does not instantiate factory.

    :cvar units_dict: Python dictionary created as a class variable. This
            dictionary holds names (types) of the game units as its keys and
            the corresponding values are the concrete classes representing the
            game character.

    .. seealso:: `Kingdom` class and various classes like `ElfRider`, `Knight`.
    """
    units_dict = {
            'elfrider': ElfRider,
            'elflord': ElfLord,
            'orcrider': OrcRider,
            'orcfighter': OrcFighter,
            'knight': Knight,
            'wizard': Wizard,
            'fairy': Fairy,
            'dwarffighter': DwarfFighter,
    }

    @classmethod
    def create_unit(cls, unit_type):
        """Return an instance of a game unit.

        This is a class method and it used the class variable units_dict to
        create and return an instance of a game unit class (e.g. ElfRider(),
        Knight(), etc)

        :arg unit_type: A string representing the unit type (e.g. 'elfrider')
        :return: Instance of a game unit.
        """
        key = unit_type.lower()
        return cls.units_dict.get(key)()
