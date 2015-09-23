"""This is an application that generate a random number"""
print "Welcome\n"

from random import randrange
RAN_NUM = randrange(1, 21)
COUNT = 0
while COUNT < 4:
    NUMBER = int(raw_input("Insert a number\n"))
    if NUMBER > RAN_NUM:#
        print "You guess to high, please try again\n"
    elif NUMBER < RAN_NUM:
        print "you guess too low, please try again\n"
    elif NUMBER == RAN_NUM:
        print "YOU WIN\n"
    COUNT += 1
    if COUNT == 4:
        print "GAME OVER"
       