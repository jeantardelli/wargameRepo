import random
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from gameutils import print_bold


class AttackOfTheOrcs(object):
    """Main class to play Attack of The Orcs game"""
    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):
        """Return a list of occupant types for all huts."""
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")

    def _process_user_choice(self):
        """Process the user input for choice of hut to enter"""
        verifying_choice = True
        idx = 0
        print("Current occupants: {0:s}".format(', '.join(self.get_occupants())))
        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-5): ")
            
            # Handling Exceptions block
            try:
                idx = int(user_choice)
                assert idx >  0

            except ValueError as e:
                print("Invalid input, args: {0:s}".format(', '.join(e.args)))
                continue
            except AssertionError as e:
                print("Number should be in the range 1-5. Try again")
                
            try:
                if self.huts[idx-1].is_acquired:
                    print("You have already acquired this hut. Try another one.\n"
                          "<INFO: You can NOT get healed in already acquired hut.>")
                else:
                    verifying_choice = False
            except IndexError as e:
                print("Number should be in the range 1-5. Try again")
        return idx

    def _occupy_huts(self):
        """Randomly occupy the huts with one of the options (friend, enemy or 'None')"""
        choice_lst = ['friend', 'enemy', None]
        for i in range(5):
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    def play(self):
        """
        Workhorse method to play the game.

        Controls the high level logic to play the game. this is called from
        the main program to begin the game execution.
        """
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print_bold("YOU LOSE :( Better luck next time")
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold("Congratulations! YOU WIN!!!")

if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()
