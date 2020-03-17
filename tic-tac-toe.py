#TIC-TAC-TOE - 3 in a row! or more?

import random
import tkinter as tk

## TIC-TAC-TOE game class: emulates a tic-tac-toe game with nxn rather than 3x3
class ttcGame:

    def __init__(self, size):
        self.size = size

    # the computer makes a move
    def opponentMove(self):
        #opponent randomly selects a square, continue until empty one found
        spot = random.randint(0, self.size*self.size-1) 

# called by GUI to make new game - assumes proper input of dimension
def newGame():
    ttcGame(ent_dimension.get())

## GRAPHICAL USER INTERFAE

window = tk.Tk()

label = tk.Label(text = "Enter a positive integer number for dimension of game.")
label.pack()
ent_dimension = tk.Entry()
ent_dimension.pack() # pack widgets so they're visible
but_submit = tk.Button(text = "Submit", command = newGame)
but_submit.pack()

window.mainloop() #listens for events like button clicks, etc.
