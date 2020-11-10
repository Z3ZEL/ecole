#22002573
#Rodriguez Esteban
#sujet1

from PIL import Image

#Exercice 1
def Mystery(myList):
    for i in range(len(myList)-2,-1,-1):
        if myList[i]>myList[i+1]:
            return False
    return True

print(Mystery([1,10,25,100]))
print(Mystery([1,-10,25,100]))
print(Mystery([1,10,25,5]))

"""
1. True , False, False
2.La fonction va retourner True si la liste est rangé dans l'ordre croissant
et False si elle ne l'est pas. Elle parcours la liste en partant de la fin et test
si la valeur à l'index i et supérieur à la valeur suivante de la liste (i+1) si oui
cela traduit donc que la liste n'est pas rangée dans l'ordre croissant.
3. On aura une erreur car car i = la longueur de la liste - 1 existe : c'est le dernier index or i+1 
est exactement égal à la longueur de la liste, qui commence à i=0 donc cet index n'existe pas :
Index out of range.

4
"""
def MysteryV2(myList):
    for i in range(len(myList-1)):
        if myList[i]>myList[i+1]:
            return False
    return True

"""
les deux sont similaires, on change juste le sens de parcours de la liste, 
cela dépendra donc juste de la liste rentrée en argument. Par exemple si toute la liste est rangée dans l'ordre croissant 
sauf la fin, alors la premiere version seras plus efficace et vice-versa.
"""
#Exercice 2
def MaxMultiple3(myList):
    max=-1
    for i in range(len(myList)):
        if(not(myList[i]%3) and myList[i]>max):
            max = myList[i]
    return max

print(MaxMultiple3([3,1,9,5,6]))
print(MaxMultiple3([2,5,7,1]))

#Exercice 3
def PixelRedInRectangle(img,x1,x2,y1,y2):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            (r,g,b) = img.getpixel((x,y))
            if(not(g) and not(b) and r):
                return True
    return False

'''
to test
testimg=Image.new("RGB",(500,500))
testimg.putpixel((300,300),(25,0,0))
print(PixelRedInRectangle(testimg,0,250,0,250))
print(PixelRedInRectangle(testimg,250,499,250,499))
'''
