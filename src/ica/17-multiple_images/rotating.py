from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def rotate_left(oldPic):
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    new_pic = Picture(h, w)
    for x in range(w):
      for y in range(h):
          old_color = oldPic.getColor(x, y)
          newX = y
          newY = w - x - 1
          new_pic.setColor(newX, newY, old_color)

    return new_pic

def rotate_right(oldPic):
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    new_pic = Picture(h,w)

    for x in range(w):
        for y in range(h):
            (r,g,b) = oldPic.getColor(x,y)
            newX = h-y-1
            newY=x
            new_pic.setColor(newX,newY,(r,g,b))
    return new_pic

p1 = Picture("../SampleImages/arches.jpg")
p2 = rotate_right(p1)
p2.show()

keep_windows_open()