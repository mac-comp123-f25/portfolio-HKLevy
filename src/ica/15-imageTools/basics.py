from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


pic=Picture("../SampleImages/mightyMidway.jpg")
#pic.show()
num_pixels=pic.getWidth() * pic.getHeight()
print(num_pixels)

pic1=pic.copy()
width=pic1.getWidth()
height=pic1.getHeight()
pic1.setColor(0,0,'red')
pic1.setColor(width-1,0,'red')
pic1.setColor(0,height-1,'red')
pic1.setColor(width-1,height-1,'red')
pic1.show()
pic1.explore()

keep_windows_open()