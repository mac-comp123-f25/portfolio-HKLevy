from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def copy_pic_into(small_pic,big_pic, start_x,start_y):
    for (x,y) in small_pic:
        (r,g,b) = small_pic.getColor(x,y)
        (newx,newy)=x+start_x, y+start_y
        big_pic.setColor(newx,newy,(r,g,b))
    return big_pic

small=Picture("../SampleImages/blueBird.jpg")
big=Picture("../SampleImages/bryceCanyon.jpg")
copy_pic_into(small,big,480,210)
copy_pic_into(small,big,320,100)
big.show()

keep_windows_open()