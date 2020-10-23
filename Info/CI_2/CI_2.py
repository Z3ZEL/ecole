from math import *
from PIL import Image

path = "test.jpg"

def Save(img):
    img.save(path)


img = Image.open(path)

#question 2.1
def LineHColorMiddle(img,c):
    (w,h)=img.size
    for x in range(w):
        img.putpixel((x,h//2),c)
# assign a vector3 variable to the color variable.


LineHColorMiddle(img,(255,255,255))






#question 2.2
def LineH(img,color,height):
    (w,h)=img.size

    if(height >= h):
        print("Error : Height out of range.")
        return img

    for x in range(w):
        img.putpixel((x,height),color)
    return img

img = LineH(img,(0,255,0),25)

#New version : lineH(img,c, height//2)

#question 2.3
def GridH(img,color,gap):
    (w,h)=img.size
    for x in range(0,h,gap):
        LineH(img,color,x)
    return img

#complexité double boucle for qui balayent l'une en x l'autre en y de l'image.

img = GridH(img,(0,0,255),3)


#question 2.5
#double boucle for qui parcours l'image entiere chaque pixel de l'image est traités

def FullRectangle(img,startPoint,endPoint):
    (w,h) = img.size
    (x1,y1) = startPoint
    (x2,y2) = endPoint
    #faire check si les vector2 sont out of range de l'array img

    for x in range(x1,x2+1):
        for y in range (y1,y2+1):
            img.putpixel((x,y),(255,255,255))
    return img

img = FullRectangle(img,(2,2),(15,20))


Save(img)


