from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def scale_down(picture):
    new_pic=Picture(round(picture.getWidth()/2),round(picture.getHeight()/2))
    for (old_x,old_y) in new_pic:
        if old_x%2==0 and old_y%2==0:
            pixel_color=picture.getColor(old_x,old_y)
            new_pic.setColor(old_x/2,old_y/2,(pixel_color))
    return new_pic

leaves=Picture("../SampleImages/fallLeaves.jpg")
scale_down(leaves).show()

keep_windows_open()