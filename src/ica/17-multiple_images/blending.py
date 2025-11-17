from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(pic1,pic2):
    new_pic=Picture(pic1.getWidth(),pic1.getHeight())
    for (x,y) in pic1:
        (r1,g1,b1)=pic1.getColor(x,y)
        (r2,g2,b2)=pic2.getColor(x,y)
        (r,g,b)=(r1+r2)/2, (g1+g2)/2, (b1+b2)/2
        new_pic.setColor(x,y,(r,g,b))
        if y==pic1.getHeight():
            new_pic.show()

    return new_pic

def blend2(pic1,pic2):
    w = min(pic1.getWidth(),pic2.getWidth())
    h = min(pic1.getHeight(),pic2.getHeight())
    new_pic=Picture(w,h)

    for (x,y) in new_pic:
        (r1,g1,b1)=pic1.getColor(x,y)
        (r2,g2,b2)=pic2.getColor(x,y)
        (r,g,b)=(r1+r2)/2, (g1+g2)/2, (b1+b2)/2
        new_pic.setColor(x,y,(r,g,b))
        if y==pic1.getHeight():
            new_pic.show()

    return new_pic

# p1=Picture("../SampleImages/daylilies.jpg")
# p2=Picture("../SampleImages/wildColumbine.jpg")
# p3=simple_blend(p1,p2)
# p3.show()

p4 = Picture("../SampleImages/muirWoods.jpg")
p5 = Picture("../SampleImages/peony.jpg")
p6 = blend2(p4,p5)
p6.show()

keep_windows_open()