"""wargame.knight

This modue is compatible with Python 3.5.x and later. It contains supporting
code for the book, Learning Python Application Development Packt Publishing.

This is my version of the code, it is pretty much similar to the original
author version.

:copyright: 2020, Jean Tardelli
:license: The MIT License (MIT). See LICENSE file for further details.
"""

from abstractgameunit import AbstractGameUnit
from gameutils import print_bold

class Knight(AbstractGameUnit):
    """
    Class that represents the game character 'Knight'

    The player instance in the game is a Knight instance. Other Knight
    instances are considered as 'friends' of the player and is indicated
    by the attribute `self.unit_type`.

    :arg str name: Name of this game character (optional)

    :ivar int max_hp: Maximum number of hit points (health points)
    :ivar int health_meter: The actual number of hit points or health points
    :ivar str unit_type: Stores id this character (unit) a friend or an enemy
    :ivar AbstractGameUnit enemy: Stores who is the enemy (not implemented)
    """
    def __init__(self, name='Sir Foo'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        """Print basic information about this character

        Overrides AbstractGameUnit.info
        """
        print("I am a Knight!")

    def acquire_hut(self, hut):
        """Fight the combat (command line) to acquire the hut

        :arg Hut hut: The hut that needs to be acquired.
        """
        print_bold("Entering hut {0:d}...".format(hut.number), end=' ')
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit) and
                    hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'

        if is_enemy:
            self.enemy = hut.occupant
            self.show_health(bold=True, end=' ')
            self.enemy.show_health(bold=True, end=' ')
            while continue_attack:
                try:
                    continue_attack = input(".......continue attack? (y/n): ")
                    assert continue_attack in ('y', 'n')
                except AssertionError:
                    print("Please, select either 'y' for attack or 'n' to run away")
                    continue

                if continue_attack == 'n':
                    self.run_away()
                    break

                self.attack(self.enemy)

                if self.enemy.health_meter <= 0:
                    print("")
                    hut.acquired(self)
                    break
                if self.health_meter <=0:
                    print("")
                    break
        else:
            if hut.get_occupant_type() =='unnocupied':
                print_bold("Hut is unoccupied")
            else:
                print_bold("Friend sighted!")
            hut.acquired(self)
            self.heal()

    def run_away(self):
        """Abandon the combat and run away from the hut

        If the player is losing the combat, there is an option to leave the
        hut. A strategy to rejuvenate and restart the combat for a better
        change of winning.

        .. seealso:: :py:meth:`self.acquire_hut`
        """
        print_bold("RUNNING AWAY...")
        self.enemy = None
