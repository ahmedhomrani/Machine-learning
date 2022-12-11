# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:48:25 2018

@author: Asma

"""
import math

##################################

a=int(input("saisir a :" ))
b=int(input("saisir b :" ))
c=int(input("saisir c :"))

if (a==0):
	if (b==0):
		if(c==0):
			print("La solution est R")
		else:
			print("Pas de solution")
	else:
		print("La solution est :",str(-c/b))
else:
    delta=(b*b)-(4*a*c)
    print("Delta=",delta)
    if(delta<0):
        print("Pas de solution dans R")
    elif (delta==0):
        print("solution unique dans R: ",str(-b/(2*a)))
    else:
        s1=(-b+math.sqrt(delta))/2/a
        s2=(-b-math.sqrt(delta))/2/a
        print("Deux solution dans R",str(s1),"et",str(s2))
        
###########################################
x="0"
nbre=0
somme=0
while(x!="="):
   somme=somme+int(x)
   x=input("saisir un entier :")
   nbre=nbre+1

print("Las somme est : ",somme,"la moyenne est : ",float(somme/(nbre-1)))


################################################
def nombreOcurrences(caractere, mot) :
    nbr=0
    for i in range(len(mot)):
        if (caractere==mot[i]):
            nbr=nbr+1

    print(caractere," existe ",nbr," fois dans ",mot )
    

nombreOcurrences("a", "java")
nombreOcurrences("b", "skz,ccldsllsxvbkapab")