"""hutgame

A simple game where the player has to select a hut where Sir Foo can rest.

This is a trivial application where the player has to select a radiobutton
to 'enter a hut'. Depending on the occupant, the player either wins or loses!
"""
import sys
import random

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    import tkMessageBox as messagebox
else:
    from tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    from tkinter import messagebox

class HutGame:
    def __init__(self, parent):
        """A game where the player selects a hut to rest.

        The program initially puts 'enemy' or a 'friend' inside each hut. Some
        huts could also be left 'unoccupied'. You are asked to select a hut.
        You win if the hut occupant is either a 'friend' or if the hut is not
        occupied.

        :param parent: the parent tkinter widget
        :ivar list huts: list to store occupant types (as strings)
        :ivar int hut_width: the width of the application window in pixels
        :ivar int hut_height: the height of the application window in pixels
        :ivar PhotoImage village_image: background image for the app
        :ivar PhotoImage hut_image: the hut image for the radio buttons
        :ivar Tk container: the main widget serving as a parent for others. In
            this example it is just the main Tk instance.
        :ivar str result: the string to declare the result via a messagebox.
        """
        self.village_image = PhotoImage(file="jungle_small.gif")
        self.hut_image = PhotoImage(file="hut_small.gif")
        self.hut_width = 40
        self.hut_height = 56
        self.container = parent
        self.huts = []
        self.result = ""
        self.occupy_huts()
        self.setup()

    def occupy_huts(self):
        """Randomly occupy the huts: enemy or friend or keep unoccupied"""
        occupants = ['enemy', 'friend', 'unoccupied']
        while len(self.huts) < 5:
            self.huts = [random.choice(occupants) for _ in range(5)]
        print("Hut occupants are: {0}".format(', '.join(self.huts)))

    def enter_hut(self, hut_number):
        """Enter the selected hut and determine the winner

        This method checks the hut occupant stored in self.huts for the
        given hut_number. Depending on the occupant the winner is 'announced'.

        :param hut_number: the number assigned to the selected hut

        .. seealso:: :py:meth: `occupy_huts`
        .. seealso:: the equivalent method in fiel hutgame_mvc.py
        """
        print("Entering hut #: {0}".format(hut_number))
        hut_occupant = self.huts[hut_number-1]
        print("Hut occupant is: {0}".format(hut_occupant))

        if hut_occupant == 'enemy':
            self.result = "Enemy sighted in Hut # {0}\n\n".format(hut_number)
            self.result += "YOU LOSE :( Luck next time!"
        elif hut_occupant == 'unoccupied':
            self.result = "Hut # {0} is unoccupied!\n\n".format(hut_number)
            self.result += "Congratulations! YOU WIN!!!"
        else:
            self.result = "Friend sighted in Hut # {0}\n\n".format(hut_number)
            self.result += "Congratulations! YOU WIN!!!"

        # Announce the winner!
        self.announce_winner(self.result)

    def create_widgets(self):
        """Create various widges in the tkinter main window."""
        self.var = IntVar()
        self.background_label = Label(self.container, image=self.village_image)
        txt = "Select a hut to enter. You win if:\n"
        txt += "The hut is unoccupie or the occupant is a friend!"
        self.info_label = Label(self.container, text=txt, bg='yellow')

        # Create a dictionary for radio button config options.
        r_btn_config = {'variable': self.var,
                        'bg': '#A8884C',
                        'activebackground': 'yellow',
                        'image': self.hut_image,
                        'height': self.hut_height,
                        'width': self.hut_width,
                        'command': self.radio_btn_pressed}

        self.r1 = Radiobutton(self.container, r_btn_config, value=1)
        self.r2 = Radiobutton(self.container, r_btn_config, value=2)
        self.r3 = Radiobutton(self.container, r_btn_config, value=3)
        self.r4 = Radiobutton(self.container, r_btn_config, value=4)
        self.r5 = Radiobutton(self.container, r_btn_config, value=5)

    def setup(self):
        """Calls methods to setup the user interface."""
        self.create_widgets()
        self.setup_layout()

    def setup_layout(self):
        """Use the grid geometry manager to place widgets."""
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(4, weight=1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.info_label.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.r1.grid(row=1, column=0)
        self.r2.grid(row=1, column=4)
        self.r3.grid(row=2, column=3)
        self.r4.grid(row=3, column=0)
        self.r5.grid(row=4, column=4)

    def announce_winner(self, data):
        """Declare the winner by displaying a tkinter messagebox.

        :param data: the data to be 'published'. This could be any object.
        """
        messagebox.showinfo("Winner Announcement", message=data)

    # Handle Events
    def radio_btn_pressed(self):
        """Command callback when radio button is pressed.

        .. seealso:: :py:meth: `create_widgets`
        """
        self.enter_hut(self.var.get())

if __name__ == '__main__':

    # Create Tk instance. This is popularly called 'root'. But let's
    # call it mainwin (the 'main window' of the application.)
    mainwin = Tk()
    WIDTH = 494
    HEIGHT = 307
    mainwin.geometry("{0}x{1}".format(WIDTH, HEIGHT))
    mainwin.resizable(0, 0)
    mainwin.title("Attack of the Orcs Game")
    game_app = HutGame(mainwin)
    mainwin.mainloop()
