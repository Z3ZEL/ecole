from math import *

#cours intégré sur la boucle while

#question 1.1
def EuclidianDivision(a,b):
    """
    return a couple integer variables (q,r)
    
    >>> EuclidianDivision(13,3)
    (4,1)


    """
    q=0
    while(a>=b):
        a-=b
        q+=1
    return(q,a)

''' or
def quotient(a,b):
    q=0
    while(a>b):
        a-=b
        q+=1
    return q

def reste(a,b):
    q=0
    while(a>b):
        a-=b
        q+=1
    return a 
'''
print(EuclidianDivision(13,3)) #q = 4 r=1
print(EuclidianDivision(2,7)) #q=0 r=2

#question 2.1

def Mystery(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

#print(Mystery(11))

#question 2.2
def Mystery2(n):
    i = 2
    while(i<n):
        if(n%i == 0):
            return False
    i+=1
    return True

"""
def Mystery2(n):
    i = 2
    while(i<n and n%i)   car var != 0 est considéré comme True
    i+=1
    return i==n
"""

#print(Mystery2(11))

#question 3.2
def IsPrime(n):
    if not(n%2):
        return False
    i = 3
    while(i*i<=n and n%i):
        i+=2
    return i*i>n

print(IsPrime(13))