from math import *
#question 1.1

l1 = [1,4,7,5,8]
print(l1)
l2 = ["a","b","d"]
print(l1)
l3 = ['a',5,"toto",2.4]
print(l3)
l1.append(2)
print(l1)
l4 = l1+l2
print(l4)

#question 1.2
print(list(range(1, 10)))
print(list(range(2, 20, 3)))
print(list(range(2, 21, 3)))
print(list(range(2, 22, 3)))
l = list(range(17, 3, -2))
print(l)

#question 1.3

evenIncreasingNumbers = range(0,102,2)
evenDecreasingNumbers = range(100,0,-2)

#question 1.4

l = [1, 4, 7, 3, 8]
l[3] = 12
print(l)

#question 1.5
#Index out of range ?

#question 2.1
#erreur d'indentation
def test1():
    #affiche 3 pairs de valeur la premiere est une valeur de la liste ,l'autre
    #est son carre
    for i in [2, 8, 5]:
        print(i, i * i)
        
#question 2.2
        
def test2():
    #si l'on change l'ordre des for nous aurion a,1 b,1 c,1 / a,2 b,2 etc...
    for c in ['a','b','c']:
        for i in [1, 2, 3, 4]:
            print(c, i)
            
def Test2Bis():
    for c in ['a','b','c']:
        for i in range(1,5):
            print(c,i)
            
#question 2.3
def mystery(n):
    s=0
    for i in range(n+1):
        s+=i
    return s
# mystery(3) -> 6 mystery(5) -> 15 mystery(n) -> somme de n terme

#question 2.5
def Factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

allFactorials = "Factorial  : "
for i in range (17):
    allFactorials += ", " +str(Factorial(i))
print(allFactorials)

#question 2.7
def SumOdds(k):
    s=0
    for i in range(1,k,2):
        s+=i
    return s

#question 2.8
def WeirdSum(n):
    s = 0
    for i in range(1,n+1):
        s += pow(3*i+1,2)
    return s
#question 2.9
def SumPower2(k):
    s = 0
    for i in range(k):
        s += 2**k
    return s
print(SumPower2(3))
#return float
        
#question3.1
def Mean(l):
    s = 0
    for i in l:
        s+=i
    return s/len(l)
#question 3.2
def NbOccurence(x,l):
    n=0
    for i in l:
        if x == i:
            n+=1
    return n

def ContainsDuplicates(l):
    if(len(l)==0):
        return

    for x in l:
        n = 0
        for y in l:
            if x == y:
               n+=1
        if n>=2:
            return True
    return False

print(ContainsDuplicates([1,5,5,2,3,4,5]))

def MaxOfOdds(l):
    if(len(l)==0):
       return
    
    odds=[]
    for i in l:
        if i%2==1:
            odds.append(i)
    
    if(len(odds) == 0):
        return 0
    
    maxOdd = odds[0]
    for j in odds:
        if(j>maxOdd):
            maxOdd = j
    return maxOdd

#question 3.5
def LastGreaterThanMean(l):
    if(len(l)==0):
        return
    
    mean = Mean(l)
    for i in range(len(l)-1,-1,-1):
        if l[i]>mean:
            return i

#question 3.6
def ClosestToMean(l):
    if(len(l)==0):
        return
    
    mean = Mean(l)
    closest = abs(mean-l[0])
    closestNumber=l[0]
    
    for i in range (0,l):
        if(abs(mean-l[i])< closest):
            closestNumber=l[i]
    return closestNumber
    
#question 4.1
            