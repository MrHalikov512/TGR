#pip install tabulate
from tabulate import tabulate
import random
import os

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

def generator():

    HeadClass = random_wepon('head.txt')
    BodyClass = random_wepon('body.txt')
    PistolCaliber = random_wepon('pistol.txt')
    Weapon = random_wepon('weapon.txt')

    data = [[" ", "Name"],
        ["Head Armor", rvv1_3(HeadClass)],
        ["Body Armor", rvv1_3(BodyClass)],
        ["Pisto", rvv1_2(PistolCaliber)],
        ["Wepon", rvv1_3(Weapon)]
    ]

    print(tabulate(data, headers='firstrow', tablefmt='grid'))

def work():
    while True:
        user_input = input("Wpisz 'next', aby wyświetlić wynik ponownie lub 'exit', aby zakończyć program: ")
        if user_input == "exit":
            print("Do zobaczenia!")
            break
        elif user_input == "next":
            print(generator())
        else:
            print("Nieprawidłowe polecenie. Wpisz 'next', aby wyświetlić wynik ponownie lub 'exit', aby zakończyć program.")


work()
