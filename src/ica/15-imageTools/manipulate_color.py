from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def change_red(picture,factor):
    for (x,y) in picture:
        (red,green,blue)=picture.getColor(x,y)
        new_red = red*factor
        picture.setColor(x,y,(new_red,green,blue))

def change_blue(picture,factor):
    for (x,y) in picture:
        (red,green,blue)=picture.getColor(x,y)
        new_blue = blue*factor
        picture.setColor(x,y,(red,green,new_blue))

def main():
    # fruit_pic = Picture("../SampleImages/raspberries.jpg")
    # fruit_pic.show()
    # change_red(fruit_pic, 1.2)
    # fruit_pic.show()

    blue_pic = Picture("../SampleImages/fireworks.jpg")
    blue_pic.show()
    change_blue(blue_pic,4.0)
    blue_pic.show()

    keep_windows_open()

if __name__=="__main__":
    main()