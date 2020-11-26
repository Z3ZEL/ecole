from PIL import Image

def CreateCross(img, crossWidth, crossHeight,color):
    (w,h) = img.size
    #bande vertical
    for y in range(h//2,h//2+(crossHeight//2)+1):
        for x in range(w//2,w//2+(crossWidth//2)+1):
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i and j) == 0 :
                        continue
                    img.putpixel((i*x,j*y),color)
                    img.putpixel((i*y,j*x),color)
                    
    
test = Image.new("RGB",(250,250))
CreateCross(test,30,100,(255,255,255))
test.show()


def minAndMax(img,crossColor):
    (w,h) = img.size
    max = 0
    min = h
    for x in range(w):
        for y in range(h):
             c1 = img.getpixel((x,y))        
             if(c1 == crossColor and y>max):
                max = y
                continue
           
    for x in range(w):
         for y in range(h):             
             c2 = img.getpixel((x,(h-1)-y))
             if(c2 == crossColor and y<min):
                min = y
                continue

    return max-min

print(minAndMax(test,(255,255,255)))