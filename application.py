"""This is an application that generate a random number"""
print "Welcome\n"

from random import randrange
NUMBER = int(raw_input("Insert a number\n"))
RAN_NUM = randrange(1, 20)
if NUMBER > RAN_NUM:
    print "You guess to high please try again"
elif NUMBER < RAN_NUM:
    print "you guess too low, please try again"
