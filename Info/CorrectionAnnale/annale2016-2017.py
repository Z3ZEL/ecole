from PIL import Image

def Peigne(img):
    (w,h) = img.size
    newImage = Image.new("RGB",(w,h))
    shift = w//4
    for y in range (h):
        for x in range (w):

            if not(y%2):
                pxColor = img.getpixel((x,y))
                if x - shift < 0:
                   newImage.putpixel(((3*w+4*x)//4,y),(255,255,255))
                else:
                   newImage.putpixel((x-shift,y),pxColor)
            else:
                pxColor = img.getpixel(((w-1)-x,y))
                if (w-1)-x + shift >= w:
                    newImage.putpixel(((-3*w+4*((w-1)-x))//4,y),(255,255,255))
                else:
                    newImage.putpixel(((w-1)-x+shift,y),pxColor)
    return newImage

testImg = Image.open("teapot.png")
Peigne(testImg).show()