# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:11:55 2017

@author: tisonad
"""

import random

#Initialyze points of players
human = 0
machine = 0

toHuman = False
stop = 0

while human < 100 and machine < 100 :
    toHuman = not toHuman
    dice = -1
    score = 0

    if toHuman:
        stop = '0'
        print("\nIt's your turn")
        while stop == '0' and dice != 1:
            dice = random.randint(1, 6)
            print("Dice : " + str(dice))
            if dice != 1:
                score += dice
                print("Score :" + str(human + score))
                stop = input("Stop now ? (0 : no ; 1 : yes) ? ")
                if stop == '1':
                    print("You stop")
                    human += score
            else:
                print("Your score : " + str(human))

    else:
        stop = 0
        print("\nMachine play")
        while stop == 0 and dice != 1:
            dice = random.randint(1, 6)
            print("Dice : " + str(dice))
            if dice != 1:
                score += dice
                print("Machine score :" + str(machine + score))
                stop = random.randint(0, 1)
                if stop == 1:
                    print("Machine stop")
                    machine += score
                else:
                    print("Machine continue")
            else:
                print("Machine score : " + str(machine))


print(str(human) + " at " + str(machine))
if toHuman:
    print("You win")
else :
    print("Machine win")