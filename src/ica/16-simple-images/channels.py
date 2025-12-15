from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def red_channel(pic):
    new_pic=pic.copy()
    for (x,y) in new_pic:
        (r,g,b)=new_pic.getColor(x,y)
        new_pic.setColor(x,y,(r,0,0))
    return new_pic

def green_channel(pic):
    new_pic=pic.copy()
    for (x,y) in new_pic:
        (r,g,b)=new_pic.getColor(x,y)
        new_pic.setColor(x,y,(0,g,0))
    return new_pic

def blue_channel(pic):
    new_pic=pic.copy()
    for (x,y) in new_pic:
        (r,g,b)=new_pic.getColor(x,y)
        new_pic.setColor(x,y,(0,0,b))
    return new_pic


pic=Picture("../SampleImages/threeFlowers.jpg")
red_channel(pic).show()
green_channel(pic).show()
blue_channel(pic).show()

keep_windows_open()