import random

def Die():
    return int(random.uniform(1,7))

#question 1.1
def NbRolls():
    n = 0
    while Die() != 6:
        n+=1
    return n

#print(NbRolls())

#question 1.2
def Double():
    n=0
    while Die() != Die():
        n+=1
    return n
#print (Double())


#question 1.3
def MeanNumberOfTriesDouble(n):
    total=0
    for i in range(n):
        total += Double()
    return total//n
#print(MeanNumberOfTriesDouble(10000))

#question 1.4
def Uniform(n):
    rollCount = [0,0,0,0,0,0]
    for i in range(n):
        roll = Die()
        rollCount[roll-1]+=1
    return rollCount
#print(Uniform(6000))

#question 2.1
def Mystery(n):
    s = 0
    while n>0:
        s+=n%10
        n//=10
    return s
#print(Mystery(2705))
'''elle fait la somme des chiffres des nombres ici 2705 affichera 14 car 2+7+0+5 = 14'''

#question 2.3
def DigitsNumber(n):
    s=0
    while n>0:
        s+=1
        n//=10
    return s
#print(DigitsNumber(2705))

#question 2.4
def GreatestDigit(n):
    max = 0
    while n>0:
        if(max<n%10):
            max = n%10
        n//=10
    return max
#print(GreatestDigit(2705))

#question 3.1
def SquareRoot(n):
    i=0
    while i<n:
        if(i*i == n):
            return i
        i+=1
    return -1

'''pas la bonne méthode voir CI While'''

#print(SquareRoot(9))

#question 3.2
def Logarithm (a,n):
    k=0
    while(Power(a,k)<n):
        k+=1
    return k


def Power(a,k):
    m=1
    for i in range(k):
        m*=a
    return m


print(Logarithm(5,85))
