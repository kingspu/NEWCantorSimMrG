import math
import random
from random import sample
from typing import Callable

primesand99 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 99]
e = math.e
pi = math.pi
tau = 2*math.pi
phi = (1 + (5) ** (1 / 2)) / 2

constants = {"tau":math.pi*2,"pi":math.pi,"phi":(1 + (5) ** (1 / 2)) / 2, "e":math.e}

def prompt(demand: str, choices: list[str], funcs: list[callable]):
    print(demand)
    for i in range(len(choices)):
        print(f"[{i+1}] : {choices[i]}")

    choice = input("What would you like to do? : ")
    if choice.isdigit():
        if int(choice) in range(1,len(choices)+1):
            funcs[int(choice) - 1]()
        else:
            print("Please enter an accepted value.")
            prompt(demand, choices, funcs)
    else:
        print("Please enter an accepted value.")
        prompt(demand,choices,funcs)

def makenum():
        print("CANTOR'S DIAGONAL PROOF SIMULATION")
        numlst = primesand99 + list(constants.keys())
        chosenlist = []
        chosenlist = sample(numlst,k=10)
        proccessedlist = []

        item = 0
        cantornum = ""
        print(f" 0.Zero           : [0].0000000000")
        for i in chosenlist:
            item += 1
            if i in list(constants.keys()):
                proccessedlist.append(constants[i]/10)
                printed = f"{proccessedlist[-1]:.11f}"
                printed = printed[:-1]
                cantornum = cantornum + printed[item + 1:item + 2]
                print(f"{item:>2}.{i:>11}/10 : {printed[:item+1]}[{printed[item+1:item+2]}]{printed[item+2:]}")
            else:
                proccessedlist.append((i**(1/2)/10))
                printed = f"{proccessedlist[-1]:.11f}"
                printed = printed[:-1]
                cantornum = cantornum + printed[item + 1:item + 2]
                print(f"{item:>2}.SQ.RT of {i:<2}/10 : {printed[:item+1]}[{printed[item+1:item+2]}]{printed[item+2:]}")
        print(f"NEW NUMBER GENERATED FROM DIAGONAL: 0.{cantornum}")
        print("THE NEW NUMBER GENERATED FROM THE DIAGONAL OF THE LIST OF IRRATIONAL NUMBERS ABOVE, DOES NOT MATCH ANY OF THE NUMBERS IN SUCH LIST.")
        if int(cantornum) in primesand99 + list(constants.values()):
            print("PROOF RESULT: All infinities are the same size")
        else:
            print("PROOF RESULT: There are different sized infinities")
        prompt("Would you like to run another simulation?",['Yes','No'],[makenum,start])

def exit():
    print("Exited")
    quit(0)

def start():
    print("WELCOME TO THE CANTOR'S DIAGONAL PROOF SIMULATOR")
    prompt("MAIN MENU\n---------------------\n",["Run Simulation","Quit"],[makenum,exit])

start()
