"""This is an application that generate a random number"""
print "Welcome\n"
import sys
import os
from random import randrange
COUNT = 0


while COUNT < 4: #we used the while loop for check the quantity of turns that played the user
    if COUNT == 0: #the if condition equals the quantity of turns to 0
        RAN_NUM = randrange(1, 21) #the variable RAN_NUM is equals to the random number between one to twenty one
    print "This is your turn number: "+str(COUNT +1) #here shows how many turns the user has played
    try:#try serves to make excepts in the errors of the program
        NUMBER = int(raw_input("Insert a number from 1 to 20\n"))#the variable NUMBER server to enter the user's number
        if NUMBER > RAN_NUM:#the if condition will chek if the number entered for the user is higer than the random number 
            print "You guess to high, please try again\n"
        elif NUMBER < RAN_NUM:#the if condition will chek if the number entered for the user is lower than the random number
            print "you guess too low, please try again\n"
        elif NUMBER == RAN_NUM:#it chekcs if the number entered for the user is equals to the random number
            print "YOU WIN\n"#if the last part is true it will show "you win"
            COUNT = 3
        elif NUMBER < RAN_NUM or NUMBER > RAN_NUM and COUNT == 4:#in this part if all conditions are true will show "Game Over"
            print "Game OVER "
        COUNT += 1#turns of the user will increase one turn
        try:#try serves to make excepts in the errors of the program
            if COUNT == 4:#it checks if the turns are equals to 4 and if you couldn't win will show "Game Over"
                print "GAME OVER"
                QUEST = True
                while QUEST == True:#if the variable QUEST is Ture will continue with the program
                    ANSWER = raw_input("Do you want to play again y/n?\n")#the variable ANSWER save if the user wants to play again or not
                    ANSWER = ANSWER.lower()#it serves to make lowercase letters
                    if ANSWER == "y" or ANSWER == "yes":#it checks the two possibles answers of the user
                        COUNT = 0
                        QUEST = False
                        os.system("cls")#it serves to clean the window
                    elif ANSWER == "n" or ANSWER == "no":#it checks the two possibles answers of the user
                        QUEST = False
                        print "Thanks for play, come back soon\n"
                        raw_input("Press enter")#if the user press enter the game will exit 
                        sys.exit()#with this the application ends

                    else:
                        print "Insert only y/n\n"#if the user enter any other letter or a number on 
        except ValueError:
            print "Insert only y or n\n"#if the user enter any other letter or a number on
    except ValueError:
        print "Insert only integer numbers\n"
