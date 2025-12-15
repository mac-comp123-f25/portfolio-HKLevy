from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def scale_down(picture):
    new_pic=Picture(round(picture.getWidth()/2),round(picture.getHeight()/2))
    for (old_x,old_y) in picture:
        if old_x%2==0 and old_y%2==0:
            pixel_color=picture.getColor(old_x,old_y)
            new_pic.setColor(old_x/2,old_y/2,(pixel_color))
    return new_pic

def scale_up(picture):
    new_pic=Picture(picture.getWidth()*2,picture.getHeight()*2)
    for (old_x,old_y) in picture:
        pixel_color=picture.getColor(old_x,old_y)
        new_pic.setColor(old_x*2,old_y*2,pixel_color)
        new_pic.setColor(old_x*2+1,old_y*2,pixel_color)
        new_pic.setColor(old_x*2,old_y*2+1,pixel_color)
        new_pic.setColor(old_x*2+1,old_y*2+1,pixel_color)
    return new_pic

leaves=Picture("../SampleImages/fallLeaves.jpg")
leaves.show()
scale_down(leaves).show()

bird=Picture('../SampleImages/blueBird.jpg')
bird.show()
scale_up(bird).show()

keep_windows_open()