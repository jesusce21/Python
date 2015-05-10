#!/usr/bin/env python
import sys
import math

cprimos=[]
numCprimos=[]

def casi(n):# Sirven para comprobar si es primo, y en caso contrario decir cual es el primo divisor
	if n % 2 == 0 and n > 2:
		primdiv =2
		return (False, primdiv)

	for element in range(3, int(math.sqrt(n)) + 1, 2):
		if ((n%int(element)) == 0):
			return False, element

	return True, 0


def casiPrimos(ini,fin):
	for num in range(int(ini),int(fin)+1):
		bprime, prime = casi(int(num)) #Comprobamos si es primo, en caso contrario cual es el divisor
		
		if(bprime==False):
			boprim, numprim = casi(int(num)/prime) #Comprobamos si es primo, en caso contrario cual es el divisor

			if(boprim==True): # Si el segundo es primo resulta una multiplicación.
				cprimos.append(int(num))


entrada = input()

for num in range(int(entrada)):
	inp = input()
	par = inp.split() #Parseamos la primera línea

	casiPrimos(int(par[0]),int(par[1])) #Analizamos cada uno de los rangos comprobando
	numCprimos.append(len(cprimos))
	cprimos=[]

for num2 in range(int(entrada)):
	print(numCprimos[num2])