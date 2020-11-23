"""mainloop_example

This module shows the simplest GUI application you could create with Tkinter
"""
import sys

if sys.version_info < (3, 0):
    from Tkinter import Tk
else:
    from tkinter import Tk

if __name__ == '__main__':
    print("Python version: {0}".format(sys.version_info))

    # Create a Tk instance
    mainwin = Tk()

    # Start the main event loop
    mainwin.mainloop()
