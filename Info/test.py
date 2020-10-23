from math import *
from turtle import *

test = int(input("Please enter a number\n"))

chaine = str(input("Demande prénom \n"))

print(chaine)


def squareroot(x):
    x-=1
    return round(x**0.5,3) 

print("Square root :"+str(squareroot(test)))



class Couleur:
    r=0
    g=0
    b=0 
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def test(self):
        print(self.r,self.g,self.b)


    def testoverload(self):
        print("Method with 0 argument")

    def testoverload(self,onevar):
        print("Method with 1 argument")



red = Couleur(1,0,0)
red.test()
red.testoverload(1)