from math import *
from PIL import Image
#question 1.1


image1 = Image.new("RGB",(300,200))
image1.putpixel((50,100),(255,255,255))

img2 = Image.open("teapot.png")
#img2.show()

#question 1.2

imgFullRectangle = Image.new("RGB",(200,200))

def FullRectangle(img,startPoint,endPoint):
    (w,h) = img.size
    (x1,y1) = startPoint
    (x2,y2) = endPoint
    #faire check si les vector2 sont out of range de l'array img

    for x in range(x1,x2+1):
        for y in range (y1,y2+1):
            img.putpixel((x,y),(255,255,255))


FullRectangle(imgFullRectangle,(50,50),(100,100))
FullRectangle(imgFullRectangle,(110,110),(190,190))

#imgFullRectangle.show()

#question 1.3

def LineH(img,color,height):
    (w,h)=img.size
    
    if(height<0 or height>=h):
        return img

    
    for x in range(w):
        img.putpixel((x,height),color)
        
imgLine = Image.new("RGB",(100,100))
LineH(imgLine,(255,0,0),50)
#imgLine.show()

#question 1.4
def Rectangle(img,startPoint,endPoint,c):
    (w,h) = img.size
    (x1,y1)=startPoint
    (x2,y2)=endPoint
    
    
    
    
    for c1 in range(abs(x1-x2)+1):
        img.putpixel((x1+c1,y1),c)
        img.putpixel((x2-c1,y2),c)
        
    for c2 in range(abs(y1-y2)+1):
        img.putpixel((x1,y1+c2),c)
        img.putpixel((x2,y2-c2),c)
        

imgRectangle = Image.new("RGB",(100,100))
Rectangle(imgRectangle,(10,10),(80,80),(0,0,255))
#imgRectangle.show()



def Diagonal(img,c):
    #ratio
    (w,h) = img.size
    ratio = 0
    
    if(w>h):
        ratio = w//h        
        n=0
        y=0
        for x in range(w):          
            img.putpixel((x,y),c)
            
            n+=1           
            if(n==ratio):
                n=0
                y+=1      
            if(y>=h):
                return
        
    else:
        ratio = h//w
        n=0
        x=0
        for y in range(h):  
            img.putpixel((x,y),c)
                      
            n+=1    
            if(n==ratio):
                n=0
                x+=1          
            if(x>=w):
                return


        
imgDiago = Image.new("RGB",(50,400))
Diagonal(imgDiago,(0,255,0))
#imgDiago.show()


#question 2.1
def filter(img,color):

    (w,h) = img.size
    (r,g,b) = color
    
    for x in range(w):
        for y in range(h):
            (pxR,pxG,pxB) = img.getpixel((x,y))
            pxR= int(pxR*(1-r/255))
            pxG= int(pxG*(1-g/255))
            pxB= int(pxB*(1-b/255))
            img.putpixel((x,y),(pxR,pxG,pxB))
            

imgFilter = Image.open("teapot.png")
filter(imgFilter,(0,255,0))
#imgFilter.show()

#question 2.2
def Luminosity(img,factor):
    (w,h) = img.size
    
    for x in range(w):
        for y in range(h):
            (r,g,b) = img.getpixel((x,y))
            r = int(r*factor)
            g = int(g*factor)
            b = int(b*factor)
            img.putpixel((x,y),(r,g,b))

imgLumi = Image.open("teapot.png")
Luminosity(imgLumi,0.5)
#imgLumi.show()
    

def Blur(img):
    (w,h) = img.size
    newImg = Image.new("RGB",(w,h))

    for x in range(w):
        for y in range(h):
            pixelsAround = PixelAround((x,y),img)
            (meanR,meanG,meanB) = (0,0,0)
            length = len(pixelsAround)
            for color in pixelsAround:
                (r,g,b)=color
                meanR+=r
                meanG+=g
                meanB+=b
            meanR = int(meanR/length)
            meanG=int(meanG/length)
            meanB=int(meanB/length)

            newImg.putpixel((x,y),(meanR,meanG,meanB))

    img = newImg

    img.show()



def PixelAround(coord,img):
    (x,y)=coord
    (w,h)=img.size

    l = []

    if(x>1):
        l.append(img.getpixel((x-1,y)))
    if(y>1):
        l.append(img.getpixel((x,y-1)))
    if(y>1 and x>1):
        l.append(img.getpixel((x-1,y-1)))
    if(x<w-1):
        l.append(img.getpixel((x+1,y)))
    if(y<h-1):
        l.append(img.getpixel((x,y+1)))
    if(x<w-1 and y<h-1 ):
        l.append(img.getpixel((x+1,y+1)))
    if(x<w-1 and y>1):
        l.append(img.getpixel((x+1,y-1)))
    if(y<h-1 and x>1):
        l.append(img.getpixel((x-1,y+1)))

    return l


def OldOneCircle(img,center,radius,color):
    (w,h)=img.size
    (a,b)=center

    for x in range(a-radius-1,a+radius+1):
        if(x<0 or x>=w):
            continue
        delta = _GetDelta(a,b,x,radius)
        if(delta<0):
            continue

        y1=int((b+sqrt(delta))/2)
        y2=int((b-sqrt(delta))/2)

        if(y1>=0 and y1<h):
           img.putpixel((x,y1),color)
        if(y2>=0 and y2<h):
            img.putpixel((x,y2),color)
    img.show()
    
def _GetDelta(a,b,x,r):
    return 4*(b**2)-4*((b**2)-(r**2)+(x-a)**2)

def Circle(img,center,radius,color):
    (w,h)=img.size
    (a,b)=center
    quality = 10

    i= (pi)/(quality*radius)
    t=0
    while t <= 2*pi:
        
        x = int(radius*cos(t*180/pi))
        y = int(radius*sin(t*180/pi))
        
        m=(x-a)**2+(y-b)**2-radius**2
        if m>0:
            x+=1
            y-=1
        elif m<0:
            x+=1
        
        if(a+x<w and y+b<h and x+a>=0 and y+b>=0):
            img.putpixel((a+x,b+y),color)
        t+=i

circleImg = Image.new("RGB",(500,500))
Circle(circleImg,(250,250),100,(255,255,255))


def Zoom(img,factor):
    (w,h)=img.size
    newImg = Image.new("RGB",(w*factor,h*factor))

    for x in range(w):
        for y in range(h):
            color = img.getpixel((x,y))
            for n in range(factor):
                newImg.putpixel((factor*x+n,factor*y+n),color)
    img = newImg

Zoom(circleImg,2)
circleImg.show()





#zoomImg = Image.open("teapot.png")
#Zoom(zoomImg,2)

#Blur(zoomImg)


