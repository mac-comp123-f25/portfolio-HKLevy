from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(pic1,pic2):
    new_pic=Picture(pic1.getWidth(),pic1.getHeight())
    for (x,y) in pic1:
        new_pic.show()
        (r1,g1,b1)=pic1.getColor(x,y)
        (r2,g2,b2)=pic2.getColor(x,y)
        (r,g,b)=(r1+r2)/2, (g1+g2)/2, (b1+b2)/2
        new_pic.setColor(x,y,(r,g,b))

    return new_pic

p1=Picture("../SampleImages/daylilies.jpg")
p2=Picture("../SampleImages/wildColumbine.jpg")
p3=simple_blend(p1,p2)
p3.show()

keep_windows_open()