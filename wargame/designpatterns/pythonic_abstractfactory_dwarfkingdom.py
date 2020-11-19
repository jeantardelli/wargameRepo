"""pythonic_abstractfactory_dwarfkingdom

This module represents a dwarf kingdom object.
"""
from pythonic_abstractfactory_kingdom import Kingdom
from pythonic_abstractfactory_dwarfaccessoryfactory import DwarfAccessoryFactory

class DwarfKingdom(Kingdom):
    """Class that represents imaginary Kingdom of the Great Dwarfs."""
    # Define which factory you want to use for this kingdom.
    factory = DwarfAccessoryFactory
