from PIL import Image;

def egalSommePrecedente(L):
    """
    docstring
    """
    for i in range(len(L)):
        s=0
        for j in range(i):
            s+=L[j]
        if(s==L[i] and L[i]!=0):
            return L[i]
    return None
#print(egalSommePrecedente([1,2,4,7,2,16,1]))

#question 4.1
def CreateEchequier(L,H):
    img = Image.new("RGB",(L,H))
    l=L//8
    h=H//8
    PaintCase(img,64,l,h,(255,255,255))
    return img



def PaintCase(img,i,l,h,color):
    for x in range(((i-1)%8)*l,((i-1)%8+1)*l):
        for y in range(((i-1)//8)*h,((i-1)//8+1)*h):
            img.putpixel((x,y),color)
CreateEchequier(64,64).show()