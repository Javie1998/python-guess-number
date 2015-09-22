print "Welcome\n"
from random import randrange 

number = input("Insert a number\n") #asks the user to enter a number 
ran_num = randrange(1,20) #here we create a random number
	
	#here we verified if the number is lower or is higher than the random number
if  number > ran_num : 
	print "You guess to high please try again"
elif number < ran_num:
	print "you guess too low, please try again"



	
	
