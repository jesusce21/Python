#!/usr/bin/env python
import sys


conmax = input() # Number of cases
for i in range(int(conmax)):
	cont = input()
	if(int(cont)%2==0): #Never used 1/2 wall-mounted urinals
		var = int(cont)/2
		print(int(var))
	else:
		var = (int(cont)+1)/2 
		print(int(var))
	