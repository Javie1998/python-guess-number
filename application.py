"""This is an application that generate a random number"""
print """                                                                                                                                                                  
                                                                                                   ,--.                                                           
  ,----..                                                             ,---,                      ,--.'|                       ____                                
 /   /   \                                                           '  .' \                 ,--,:  : |                     ,'  , `.  ,---,                       
|   :     :          ,--,                                           /  ;    '.            ,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-. 
.   |  ;. /        ,'_ /|             .--.--.    .--.--.           :  :       \           |   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /| 
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '          :  |   /\   \          :   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' | 
;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./          |  :  ' ;.   :         |   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,' 
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_            |  |  ;/  \   \        '   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /   
.   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `.         '  :  | \  \ ,'        |   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '    
'   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \        |  |  '  '--'          '   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |    
'   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /        |  :  :                |   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;    
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     /         |  | ,'                '   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'     
 \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'          `--''                  ;   |.'       `--`----'   '---'           /    \  /  \   \  /           
  `---`                     `----'                                                        '---'                                     `-'----'    `----'            
                                                                                                                                                                  """

print """
                            =====================================================
                            |--------------------Welcome------------------------|
                            |                                                   |
                            |----- Hi, in this game we gonna challenge you------|
                            |--------to Guess a number. Do you accept?----------|
                            |------ You have to use only Integer Numbers--------|
                            |-------------You only have 4 turns-----------------|
                            |-----------------Enjoy it!! n.n--------------------|
                            =====================================================        
                                     \n"""
import sys
import os
from random import randrange
COUNT = 0


while COUNT < 4:
    if COUNT == 0:
        RAN_NUM = randrange(1, 21)

    print "This is your turn number: "+str(COUNT +1)
    try:
        NUMBER = int(raw_input("Insert a number from 1 to 20\n"))
        if NUMBER > RAN_NUM:
            print """***You guess to high, please try again***\n"""
        elif NUMBER < RAN_NUM:
            print """***you guess too low, please try again***\n"""
        elif NUMBER == RAN_NUM:
            print "YOU WIN $.$\n"
            COUNT = 3
        elif NUMBER < RAN_NUM or NUMBER > RAN_NUM and COUNT == 4:
            print """Game OVER :[ """
        COUNT += 1
        try:
            if COUNT == 4:
                print "GAME OVER "
                QUEST = True
                while QUEST == True:
                    ANSWER = raw_input("Do you want to play again y/n?\n")
                    ANSWER = ANSWER.lower()
                    if ANSWER == "y" or ANSWER == "yes":
                        COUNT = 0
                        QUEST = False
                        os.system("cls")
                        os.system("clear")
                        print """
                        =============================================================
                        |------------------Hi, Welcome again n.n--------------------|
                        |------In this time we give to you a second chance----------|
                        |-----to win!, Do you think you can do it this time??-------|
                        =============================================================
                        """
                    elif ANSWER == "n" or ANSWER == "no":
                        QUEST = False
                        print "Thanks for play, come back soon, We hope to see you again!! *--*\n"
                        raw_input("Press enter")
                        sys.exit()

                    else:
                        print "Insert only y/n\n"
        except ValueError:
            print "Insert only y or n\n"
    except ValueError:
        print "Insert only integer numbers\n"
