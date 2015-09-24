"""This is an application that generate a random number"""
print "Welcome\n"
import sys
import os
from random import randrange

COUNT = 0
while COUNT < 4:
    print "This is your "+str(COUNT +1) + " turn"
    RAN_NUM = randrange(1, 21)
    try:
        NUMBER = int(raw_input("Insert a number from 1 to 20\n"))
        if NUMBER > RAN_NUM:
            print "You guess to high, please try again\n"
        elif NUMBER < RAN_NUM:
            print "you guess too low, please try again\n"
        elif (NUMBER == RAN_NUM) and (ANSWER.isalpha() == True):
            print "YOU WIN\n"
            ANSWER = raw_input("Do you want to play again y/n?\n")
            ANSWER.lower()
            if ANSWER == "y" or ANSWER == "yes":
                COUNT = 0
                os.system("cls")
            elif ANSWER == "n" or ANSWER == "no":
                ANSWER.isalpha()
                sys.exit()
        COUNT += 1
        try:
            if (COUNT == 4) and (ANSWER.isalpha() == True):
                print "GAME OVER"
                ANSWER = raw_input("Do you want to play again y/n?\n")
                ANSWER.lower()
                if ANSWER == "y" or ANSWER == "yes":
                    COUNT = 0
                    os.system("cls")
                elif ANSWER == "n" or ANSWER == "no":    
                    sys.exit()
        except ValueError:
            print "Insert only y or n\n"
    except ValueError:
        print "Insert only integer numbers"
