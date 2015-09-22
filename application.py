print "Welcome\n"
from random import randrange #importa "randrange" de random

number = input("Insert a number\n") #pide al usuario que ingrese un numero 
ran_num = randrange(1,20) #genera un numero aleatorio del 1 al 20
	
	#verifica si el numero ingresado es mayor o menor que el generado
if  number > ran_num : 
	print "You guess to high please try again"
elif number < ran_num:
	print "you guess too low, please try again"



	
	
