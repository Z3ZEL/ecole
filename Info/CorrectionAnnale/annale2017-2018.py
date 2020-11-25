#question 1.1
from PIL import Image

def DarkPurpleFilter(img):
    (w,h) = img.size
    for x in range(w):
        for y in range(h):
            (r,g,b) = img.getpixel((x,y))
            r//=2
            g=0
            b//=2
            img.putpixel((x,y),(r,g,b))

#question 1.2
testImg = Image.open("teapot.png")
DarkPurpleFilter(testImg)
testImg.show()

#question 2.1
print("Mystere1")
def mystere1(L,x,b):
    cpt=0
    for i in L:
        if i==x:
            cpt+=1
            if cpt==b:
                return True
        print(i,cpt)
    return False
print(mystere1([1,0,2,1,1,0,0,0,2,2],0,4))
#True

print("Mystere2")
def mystere2(L,x,b):
    cpt = 0
    for i in L:
        if i == x:
            cpt+=1
            if cpt==b:
                return True
        else:
            cpt=0
        print(i,cpt)
    return False
print(mystere2([1,0,2,1,1,0,0,0,2,2],0,4))
#False

print("Mystere3")
def mystere3(L,x,b):
    cpt = 0
    for i in L:
        if i==x:
            cpt+=1
            if cpt==b:
                return True
            else:
                cpt=0
        print(i,cpt)
    return False
print(mystere3([1,0,2,1,1,0,0,0,2,2],0,4))
#False

'''
La première fonction retourne True si il y a b élément x dans la
liste L rentré en paramètre. Sinon elle retourne False
La deuxième fonction retourne True si la Liste contient l'élement x
, b fois de suite sinon elle retourne False.
La dernière fonction ne fait rien car "else: cpt=0" a été identé une fois de 
plus que dans la deuxième fonction ce qui provoque une réinitialisation du compteur
à chaque passage dans la boucle elle ne pourra donc jamais retourner vraie
sauf pour b = 1 ou elle retourne True si l'élément x apparait 1 fois.
'''

#question 3.1
def DarkFrame(img):
    (w,h)=img.size
    blackPx = (0,0,0)
    for i in range(2):
        for x in range(w):
            px1=img.getpixel((x,i))
            px2=img.getpixel(((w-1)-x,(h-1)-i))
            if (px1 or px2) != blackPx :
                return False
        for y in range(h):
            px1 = img.getpixel((i,y))
            px2 = img.getpixel(((w-1)-i,(h-1)-y))
            if(px1 or px2) != blackPx:
                return False
    return True

#question 3.2
'''
On va parcourir 2 fois (premiere boucle for) toute la largeur (w) et ensuite toute la hauteur(h)
mais pas l'une * l'autre car les deux ne sont pas imbriqués.
Ensuite dans chacune d'elle il y a 2 instructions, deux opérations en somme, que nous
allons considérer comme élémentaire. Il y a donc 2*w + 2*h instructions or nous allons répéter cela
2 fois donc 2*(2*w + 2*h). La complexité de ma fonction est donc de 4w+4h.
'''

#question 3.3
def FindWhitePx(img):
    (w,h)=img.size
    whitePx = (255,255,255)
    for y in range(h-1,-1,-1):
        for x in range(w):
            px = img.getpixel((x,y))
            if px == whitePx:
                return (x,y)
    return None


'''test= Image.new("RGB",(100,100))
test.putpixel((50,50),(255,255,255))
test.putpixel((43,50),(255,255,255))
print(FindWhitePx(test))'''
