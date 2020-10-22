import random
from abc import ABC, abstractmethod
from gameuniterror import GameUnitError
from gameutils import print_bold, weighted_random_selection

class AbstractGameUnit(ABC):
    """An abstract base class for creating various game characters"""
    def __init__(self, name=''):
        self.name = name
        self.max_hp = 0
        self.health_meter = 0
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """Information on the unit (MUST be overridden in subclasses)"""
        pass

    def attack(self, enemy):
        """The main logic to determine injured unit and amount of injury"""
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
        """Heal the unit replenishing all the hit points"""
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
        """Show the remaining hit points of the player and the enemy"""
        msg = "Health: {0:s} {1:d}".format(self.name, self.health_meter)
            
        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)

