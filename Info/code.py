from math import *
#infinity representation : inf


if(-10000>-inf):
    print("true")



def MaxList(l):
    max = l[0]

    for j in range(1,len(l)):
        if l[j]>max:
            max = l[j]
    
    return max

def NbEvenList(l):
    n=0
    for i in l:
        if i%2==0:
            n+=1
    return n