"""wargame.orcrider

This module contains the OrcRider class implementation.

This modue is compatible with Python 3.5.x and later. It contains supporting
code for the book, Learning Python Application Development Packt Publishing.

This is my version of the code, it is pretty much similar to the original
author version.

:copyright: 2020, Jean Tardelli
:license: The MIT License (MIT). See LICENSE file for further details.
"""
from abstractgameunit import AbstractGameUnit

class OrcRider(AbstractGameUnit):
    """Class that represents the game character Orc Rider

    .. seealso:: The class `Knight` and the superclass `AbstractGameUnit`
    """
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Grrr..I am an Orc Wolf Rider. Don't mess with me.")
