from math import *

print("Hello all")
#this is a python comment
print("Welcome to python")

def f(x):
    return x*x+x+1

def UselessF(x):
    print(x*x+x+1)

y = f(2)
print(y)

t = 4
z = f(t)
print(z)

x = (3*t+1)/2
t = f(t)

def Average(a,b):
    """return the average btw 2 numbers a,b
    
    >>>
    Average(0,20)
    20
    
    """
    return (a+b)/2

def WeightedAverage(a,coefA,b,coefB):
    """return the weighted average btw 2 numbers and their coef"""
    return (a*coefA+b*coefB)/(coefA+coefB)

def BetteredAverage(a,b):
    return WeightedAverage(a,1,b,1)




print("Basic Average : \n ",Average(int(input("First number : \n")),int(input("Second number : \n"))))
print("Weighted Average : \n",WeightedAverage(20,3,10,1))
print("Weighted Average w/ normalized coef : \n",BetteredAverage(12,20))


def Swap(x,y):
    return [y,x]

print("Swap : ",Swap(1,2))

def Even(n):
    return n%2==0

print("Even : ",Even(34))


def Compare(a,b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

print("Compare 6 and 7 : ",Compare(6,7))

def Max2(x,y):
    if x<y:
        return y
    else:
        return x

print("Max value btw 10 and 60 : ",Max2(10,60))

#max 3 same

def CostPhotocopies(n):
    if(n<=10):
        return n*20
    elif(n<=30):
        return (n-10)*15+200
    else:
        return (n-30)*10+500


print("340 photocopies cost : ", CostPhotocopies(340))
def OneMoreMinute(h,m):
    m+=1
    if(m>=60):
        h+=1
        m=0
    if(h>=24):
        h=0

    print(h,m)

print("Next Minutes : ", OneMoreMinute(14,59),OneMoreMinute(23,59))

def Solve(a,b,c):
    delta = pow(b,2)-4*a*c
    if(delta < 0 ):
        print("No solution")
        return

    if(delta == 0):
        print("One solution : \n", (-b)/(2*a))
        return

    if(delta > 0):
        print ("Two solutions : \n",(-b-sqrt(delta))/(2*a),"\n",(-b+sqrt(delta))/(2*a))

Solve(4,-4,1)
Solve(1,5,5)



    


