import random
from abc import ABC, abstractmethod
from gameuniterror import GameUnitError
from gameutils import print_bold, weighted_random_selection

class AbstractGameUnit(ABC):
    """Abstract class to represent a game character (or a 'unit')

    :ivar name: Name of the character (set by subclassess)
    :ivar max_hp: Maximum 'hit points' or 'health points' for the unit.
                      This is set by the subclasses.
    :ivar health_meter: Keeps track of the current health of the unit
    :ivar enemy: Present enemy of this unit. At any time, it can have only one enemy.
    :ivar unit_type: Tells if this is a 'friend' or an 'enemy'

    :param name: Accept the name of this game character

    .. seealso:: Classes :py:class:`Knight` and :py:class:`OrcRider`
    """
    def __init__(self, name=''):
        self.name = name
        self.max_hp = 0
        self.health_meter = 0
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """Print information about this game unit.

        Abstract method. See subclasses for implementation.
        """
        pass

    def attack(self, enemy):
        """The main logic to 'attack' the enemy unit.

        This method handles combat between the player (Knight instance) and the
        given enemy (at the moment OrcRider instance). In the combat, one of the 
        units could get injured or both will scape unhurt. The method reduces the
        'health' oh the injured unit by a randomly selected amount.

        :param enemy: The enemy to be attacked (instance of subclass of AbstractGameUnit)

        .. seealso:: :py:meth:`Knight.acquire_hut`
        """
        if not enemy:
            print("No enemy to attack")
        else:
            injured_unit = weighted_random_selection(self, enemy)
            injury = random.randint(10, 15)
            injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
            print("ATTACK! ", end='')
            self.show_health(end='  ')
            enemy.show_health(end='  ')
 
    def heal(self, heal_by=2, full_healing=True):
        """Heal the unit replenishing all the hit points

        This method is called when you (the player) enters a friendly hut.

        :param heal_by: `health_meter`will be updated by this amount if full
                        healing is not requested.
        :param full_healing: Fully heal this unit by resetting the `heal_meter`to
                        the maximum limit.

        .. seealso:: :py:meth:`Knigth.acquire_hut`
        """
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
 
        if self.health_meter > self.max_hp:
            raise GameUnitErrors("health_meter > max_hp!")
 
        print_bold("You are HEALED!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assing default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """Print info on the current health reading of this game unit

        The arguments to this method are mainly to customize the message display style.

        :param bold: Flag to indicate whether information should be printed in bold
                     style or normal style.
        :param end: Specify how the message should end i.e wheter a new line character
                     should be appended in the end or you want to add a space or a tab
                     (for message continuation)

       """
        msg = "Health: {0:s} {1:d}".format(self.name, self.health_meter)
 
        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)

