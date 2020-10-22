from abstractgameunit import AbstractGameUnit
from gameutils import print_bold

class Knight(AbstractGameUnit):
    """
    Class that represents the game character 'Knight'

    The player instance in the game is aKnight instance. Other Knight
    instances are considered as 'friends' of the player and is indicated
    by the attribute `self.unit_type`.
    """
    def __init__(self, name='Sir Foo'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        """Print basic information about this character"""
        print("I am a Knight!")

    def acquire_hut(self, hut):
        """Fight the combat (command line) to acquire the hut"""
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
                    assert continue_attack == 'y' or continue_attack == 'n'
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
        """Abandon the battle"""
        print_bold("RUNNING AWAY...")
        self.enemy = None
