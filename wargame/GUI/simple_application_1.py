"""simple_application_1

A 'Hello World' GUI application script using Tkinter module.
"""
import sys

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Button, LEFT, RIGHT
else:
    from tkinter import Tk, Label, Button, LEFT, RIGHT


if __name__ == '__main__':

    # Create the main window or Tk instance
    mainwin = Tk()
    mainwin.geometry("140x40")

    # Create a label widget and 'pack' it in a row (or column)
    lbl = Label(mainwin, text="Hello World!", bg='yellow')
    lbl.pack(side=LEFT)

    # 'Exit' button that calls mainwin.destroy when clicked
    exit_button = Button(mainwin, text='Exit', command=mainwin.destroy)
    exit_button.pack(side=RIGHT)

    # Mainloop
    mainwin.mainloop()
