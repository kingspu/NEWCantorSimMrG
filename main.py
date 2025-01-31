import math
import random

import winsound

primesand99 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 99]
e = math.e
pi = math.pi
tau = 2*math.pi
phi = (1 + (5) ** (1 / 2)) / 2

constants = {"tau":math.pi*2,
             "pi":math.pi,
             "phi":(1 + (5) ** (1 / 2)) / 2,
             "e":math.e}
cantorlen = 10

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

def promptint(demand: str, range : list[int]):
    chosenint = input(f"{demand} : ")
    if chosenint.isdigit() and int(chosenint) >= range[0] and int(chosenint) <= range[1]:
        return int(chosenint)
    else:
        print("Please choose and accepted value.")
        return promptint(demand,range)

def makenum():
        print("CANTOR'S DIAGONAL PROOF SIMULATION")
        numlst = primesand99 + list(constants.keys())
        chosenlist = []
        chosenlist = random.sample(numlst, k=cantorlen)
        proccessedlist = []

        item = 0
        cantornum = ""
        for i in chosenlist:
            item += 1
            if i in list(constants.keys()):
                proccessedlist.append(constants[i]/10)
                proccessedlist[-1] = f"{proccessedlist[-1]:.{cantorlen+1}f}"[:-1]
                cantornum = cantornum + proccessedlist[-1][item + 1:item + 2]
                print(f"{item:>2}.{i:>12}/10    : {proccessedlist[-1][:item+1]}[{proccessedlist[-1][item+1:item+2]}]{proccessedlist[-1][item+2:]}")
            else:
                if len(str(i)) <= 2:
                    primedivisor = 10
                else:
                    primedivisor = 100

                proccessedlist.append((i**(1/2)/primedivisor))
                proccessedlist[-1] = f"{proccessedlist[-1]:.{cantorlen+1}f}"[:-1]
                cantornum = cantornum + proccessedlist[-1][item + 1:item + 2]
                print(f"{item:>2}.SQ.RT of {i:<3}/{primedivisor:<5} : {proccessedlist[-1][:item+1]}[{proccessedlist[-1][item+1:item+2]}]{proccessedlist[-1][item+2:]}")
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

def settings():
    prompt("SETTINGS\n--------------------",["Change prime finding range","Change cantor number length","beep...","Main Menu"],[changeprimerange,changenumlen,playnoise,start])

def start():
    print("WELCOME TO THE CANTOR'S DIAGONAL PROOF SIMULATOR")
    prompt("MAIN MENU\n--------------------",["Run Simulation","Settings","Quit"],[makenum,settings,exit])

def getprimes(untill: int):
    possiblenums = []
    for i in range(2,untill+1):
        possiblenums.append(i)
    for divisor in possiblenums:
        for dividend in possiblenums:
            if dividend%divisor == 0 and divisor/dividend != 1 and dividend in possiblenums:
                possiblenums.remove(dividend)
    return possiblenums

def changeprimerange():
    global primesand99
    primesand99 = getprimes(promptint("Choose an integer between 13 and 1000 to find primes",[13,1000]))
    print(f"Your primes are now {primesand99}")
    settings()

beepmeter = 0
def playnoise():
    global beepmeter
    if beepmeter < 10:
        x = random.randint(1000,5000)
        winsound.Beep(x,20)
        beepmeter = beepmeter + 1
        print("beware of the omega beep")
        settings()
    else :
        winsound.Beep(300,10000)
        beepmeter = 0
        settings()

def changenumlen():
    global cantorlen
    cantorlen = promptint("Change Cantor's Number Length(Anywhere from 1 to 16, default is 10)", [1,16])
    print("Changed")
    settings()

start()
