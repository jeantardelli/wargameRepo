"""wargame.hut

This module contains the Hut class implementation.

This modue is compatible with Python 3.5.x and later. It contains supporting
code for the book, Learning Python Application Development Packt Publishing.

This is my version of the code, it is pretty much similar to the original
author version.

:copyright: 2020, Jean Tardelli
:license: The MIT License (MIT). See LICENSE file for further details.
"""

from gameutils import print_bold

class Hut():
    """Class to create hut object(s) in the game Attack of the Orcs

    :arg int number: Hut number to be assigned
    :arg AbstractGameUnit occupant: The new occupant of the Hut

    :ivar int number: A number assigned to this hut
    :ivar AbstractGameUnit occupant: The occupant of this hut.
                  Needs to be an instance of the subclass of
                  `AbstractGameUnit`.
    :ivar boolean is_acquired: A boolean flag to indicate if the
                  hut is acquired. In the current implementation
                  this is viewed from the player's perspective.

    .. seealso:: where it is used --
            :py:meth: `attackoftheorcs.AttackOfTheOrcs.setup_game_scenario`
    """
    def __init__(self, number, occupant):
        self.number = number
        self.occupant = occupant
        self.is_acquired = False

    def acquired(self, new_occupant):
        """Update the occupant of this hut and set is_acquired flag.

        Update the occupant instance variable with the parameter new_occupant
        and set the is_acquired flag to True.

        :arg new_occupant: self.occupant will be updated with this parameter

        .. todo:: In the current implementation this is supposed to be called
                  only bt the `Knight` instance (everything from the player
                  context). A generalization is to allow anyone to 'acquire'
                  the hut! In that case, the client code should properly
                  interpret meaning of `is_acquired` flag!
                  Otherwise it will be a bug! As an exercise, write a unit
                  test to catch this and/or make the calling code robust.
        """
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("GOOD JOB! Hut {0:d} acquired".format(self.number))

    def get_occupant_type(self):
        """Return a string giving info on the hut occupant type.

        Used only for the printing information on who is present in the
        hut. The information it will return depends on the occupant and
        can be one of these strings: 'enemy', 'friend', 'ACQUIRED',
        'unoccupied'

        The logic is as follows: If the hut.occupant is one of the game
        characters, it will simply retrieve this info from that instance.
        Otherwise determine whether it is acquired or unoccupied.

        :return: A string representing the occupant type

        .. seealso: :py:meth: `attackoftheorcs.AttackOfTheOrcs.get_occupants`
        """
        if self.is_acquired:
            occupant_type = 'ACQUIRED'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type
