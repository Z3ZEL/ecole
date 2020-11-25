#exercice 2
from PIL import Image

testImg = Image.new("RGB",(128,128))

def VerticalRemplissage(img,c):
    (w,h) = img.size

    for x in range(w//2):
        for y in range(h):
            img.putpixel((x,y),c)

#VerticalRemplissage(testImg,(180,180,180))
#testImg.show()

def HorizontalRemplissage(img,c):
    (w,h) = img.size

    for x in range(w):
        for y in range(h//2):
            img.putpixel((x,y),c)

#HorizontalRemplissage(testImg,(180,180,180))
#testImg.show()

def DiagonalRemplissage(img,c):
    (w,h) = img.size
    for x in range(w):
        img.putpixel((x,(x*h)//w),c)

#DiagonalRemplissage(testImg,(180,180,180))
#testImg.show()

#exercice 3
def isBright(img):
    (w,h)=img.size
    numberHalfPx=(w*h)//2
    luminosity=[0,0]
    for x in range(w):
        for y in range(h):
            (r,g,b) = img.getpixel((x,y))
            mean = (r+b+g)//3
            if mean > 127:
                luminosity[1]+=1
            else: 
                luminosity[0]+=1
            if luminosity[1] > numberHalfPx:
                return True
            elif luminosity[0] > numberHalfPx:
                return False
    return False

#HorizontalRemplissage(testImg,(255,255,255))
#VerticalRemplissage(testImg,(255,255,255))
#print(isBright(testImg))

#exercice 4
def mystery(L,b):
    p=0
    for i in range(0,8):
        p=p*b+L[i]
    return p
#print(mystery([0,0,1,0,0,1,0,1],10))

def calculPolynome(L,x):
    value=L[0]
    for a in range(1,5):
        value*=x+L[a]
    return value