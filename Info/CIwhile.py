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

#question 3.3
def IsPrime(n):
    if not(n%2):
        return False
    i = 3
    while(i*i<=n and n%i):
        i+=2
    return i*i>n

#print(IsPrime(13))

#question 3.4
def NextPrime(n):
    p = n+1
    if not(p%2):
        p+=1
    while not(IsPrime(p)):
        p+=2
    return p

print(NextPrime(13))



def SquareRoot(n):
    s=0
    nb=1
    resp=0
    while s<n:
        s+=nb
        nb+=2
        resp+=1
    if s!=n:
        resp-=1
    return resp

print(SquareRoot(12))

def LogarithmA(a,n):
    k=1
    p=a
    while(p<=n):
        p*=a
        k+=1
    return k-1 

print(LogarithmA(10,1))