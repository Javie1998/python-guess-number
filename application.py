"""This is an application that generate a random number"""
print "Welcome\n"
import sys
import os
from random import randrange
COUNT = 0
RAN_NUM = randrange(1, 21)
while COUNT < 4:
    print "This is your turn number: "+str(COUNT +1)
    try:
        NUMBER = int(raw_input("Insert a number from 1 to 20\n"))
        if NUMBER > RAN_NUM:
            print "You guess to high, please try again\n"
        elif NUMBER < RAN_NUM:
            print "you guess too low, please try again\n"
        elif NUMBER == RAN_NUM:
            print "YOU WIN\n"
            COUNT = 3
        elif NUMBER < RAN_NUM or NUMBER > RAN_NUM and COUNT == 4:
            print "Game OVER "
        COUNT += 1
        try:
            if COUNT == 4:
                print "GAME OVER"
                QUEST = True
                while QUEST == True:
                    ANSWER = raw_input("Do you want to play again y/n?\n")
                    ANSWER.lower()
                    ANSWER.isalpha()
                    if ANSWER == "y" or ANSWER == "yes":
                        COUNT = 0
                        QUEST = False
                        os.system("cls")
                    elif ANSWER == "n" or ANSWER == "no":
                        QUEST = False
                        sys.exit()
                    else:
                        print "Insert only y/n\n"
        except ValueError:
            print "Insert only y or n\n"
    except ValueError:
        print "Insert only integer numbers"
