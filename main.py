from tabulate import tabulate
import random
import os
from tkinter import *
def random_wepon(filename):
    with open(filename) as f:
        data = f.read().split(',')
        return random.choice(data)


def rvv1_3(variable): #random variable valiu 66%
    if random.randint(0, 2) == 1 or 2:
        return variable
    else:
        return 0

def rvv1_2(variable): #random variable valiu 50%
    if random.randint(0,1) == 0:
        return variable
    else:
        return 0

class GeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Weapon Generator")

        # create labels and buttons
        self.label = Label(master, text="Click the button to generate a weapon:")
        self.label.pack()

        self.generate_button = Button(master, text="Generate", command=self.generate_weapon)
        self.generate_button.pack()

        self.exit_button = Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

        # create a text box to display the generated weapon
        self.text = Text(self.master)
        self.text.pack()

    def generate_weapon(self):
        # clear the previous result
        self.text.delete(1.0, END)

        HeadClass = random_wepon('head.txt')
        BodyClass = random_wepon('body.txt')
        PistolCaliber = random_wepon('pistol.txt')
        Weapon = random_wepon('weapon.txt')

        data = [[" ", "Name"],
                ["Head Armor", rvv1_3(HeadClass)],
                ["Body Armor", rvv1_3(BodyClass)],
                ["Pistol", rvv1_2(PistolCaliber)],
                ["Weapon", rvv1_3(Weapon)]
        ]

        # display the generated weapon in the text box
        self.text.insert(END, tabulate(data, headers='firstrow', tablefmt='grid'))

# create the GUI
root = Tk()
gui = GeneratorGUI(root)
root.mainloop()