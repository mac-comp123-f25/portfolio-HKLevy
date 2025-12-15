from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def negative(pic):
    new_pic=pic.copy()
    for (x,y) in new_pic:
        (r,g,b)=new_pic.getColor(x,y)
        (newr,newg,newb) = (255-r,255-g,255-b)
        new_pic.setColor(x,y,(newr,newg,newb))
    return new_pic

pic=Picture("../SampleImages/bristleconePine.jpg")
negative(pic).show()

keep_windows_open()