from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def color_shuffle(pic):
    new_pic=pic.copy()
    for (x,y) in new_pic:
        (r,g,b) = new_pic.getColor(x,y)
        new_colors=(b,r,g)
        new_pic.setColor(x,y,new_colors)
    return new_pic

pic=Picture("../SampleImages/raspberries.jpg")
color_shuffle(pic).show()

keep_windows_open()