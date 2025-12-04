from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def weighted_scale(pic,w1,w2,w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (w1*r + w2*g + w3*b)
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

pic=Picture("../SampleImages/butterfly.jpg")
newpic=weighted_scale(pic,0,0,1)
newpic.show()

keep_windows_open()