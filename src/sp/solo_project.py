"""
This script draws a mandala. The user can choose the colors or color scheme of the mandala.

@author: Helen K. Levy (hlevy@macalester.edu)
"""
import turtle
import math
from polar_coordinate_graphing import graph_sin_theta_transformation
from color_shading import shading


def line(t,length,dot):
    """
    A turtle draws a line and goes back, so the turtle starts
    and ends at the same point facing the same direction.
    There is an option to include a dot at the other side of the line.

    :param t: The turtle that will draw the line.
    :param length: The length of the line.
    :param dot: A boolean value that will determine whether a dot is drawn.
    :return: None
    """
    t.fd(length)
    if dot:
        t.dot(10)
    t.bk(length)


def separator(t,inside_radius,thickness,num_separators,fill_bool):
    """
    A turtle draws a circular separator for the mandala. The turtle
    starts and ends directly south of the circle's center, facing east.
    There is an option to have the whole separator filled in.

    :param t: The turtle that will draw the separator.
    :param inside_radius: The radius of the inside of the separator.
    :param thickness: The thickness of the separator.
    :param num_separators: The number of divisions in the separator ring. Must be a factor of 360.
    :param fill_bool: A boolean value that will determine whether the separator is filled in.
    :return: None
    """
    t.up()
    t.goto(0,-1*(inside_radius+thickness))
    t.seth(0)
    t.down()
    if fill_bool:
        t.begin_fill()
        t.lt(90)
        t.fd(thickness)
        t.rt(90)
        t.circle(inside_radius)
        t.lt(90)
        t.bk(thickness)
        t.rt(90)
        t.circle(inside_radius+thickness,extent=-360)
        t.end_fill()
    else:
        for a in range(num_separators):
            t.lt(90)
            line(t,thickness,False)
            t.rt(90)
            t.circle(inside_radius+thickness,extent=int(360/num_separators))


if __name__ == '__main__':
    """This sets up the turtle and the screen."""
    win = turtle.Screen()
    turt = turtle.Turtle()
    turt.speed(0)
    turt.ht()

    """This section generates a list of the colors that will be used. Each layer of the
    mandala will be a slightly different color, so the color will progressively change."""
    color_dict={'R':shading('#ffcfcf','#ff0000',6),
                'O':shading('#ffe8c9','#ff9500',6),
                'Y':shading('#fffaa3','#fff200',6),
                'G':shading('#b3ffb8','#00ff11',6),
                'B':shading('#b5eaff','#00b7ff',6),
                'V':shading('#f0c4ff','#bb02fa',6),
                'P':shading('#ffe8f8','#ff00b3',6)}
    print(""" ––––––––––Color Options–––––––––––
    To use one of the pre-made color schemes, enter the corresponding letter.
    To choose your own color scheme, enter C. You must enter one capital letter.
    
    Red:– – – – – – – – R
    Orange: – – – – – – O
    Yellow: – – – – – – Y
    Green:– – – – – – – G
    Blue: – – – – – – – B
    Purple: – – – – – – V
    Pink: – – – – – – – P
    Choose your own:– – C
    """)
    keyword=input("Enter your choice: ")
    while keyword not in color_dict and keyword != 'C':
        keyword=input("Enter your choice. It must be one capital letter from the options above. ")
    if keyword in color_dict:
        color_list=color_dict[keyword]
        print("Ok!")
    elif keyword == 'C':
        print("Enter your colors in the form of a rrggbb hex code with all lowercase letters. Do not include # before your entry.")
        print()
        acceptable_characters=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

        #Checks whether the first color is in the right form.
        start_color=input("What color do you want on the inside of the mandala? ")
        condition=False
        while not condition:
            pt1=True
            pt2=True
            if len(start_color)!=6:
                pt1=False
            for x in start_color:
                if x not in acceptable_characters:
                    pt2=False
            if pt1==True and pt2==True:
                condition=True
            else:
                start_color=input("Enter your color again. It must be in the form of a rrggbb hex code with all lowercase letters. Do not include a #. ")

        #Checks whether the second color is in the right form.
        print()
        end_color=input("What color do you want on the outside of the mandala? ")
        condition=False
        while not condition:
            pt1=True
            pt2=True
            if len(end_color)!=6:
                pt1=False
            for x in end_color:
                if x not in acceptable_characters:
                    pt2=False
            if pt1==True and pt2==True:
                condition=True
            else:
                end_color=input("Enter your color again. It must be in the form rrggbb. Do not include a #. ")

        #Generates the list of colors for each layer of the mandala
        color1='#'+start_color
        color2='#'+end_color
        color_list=shading(color1,color2,6)
        print("Ok!")
    else:
        #This block should never be reached, but it exists just in case.
        color_list=shading('#000000','#000000',6)

    """This draws the innermost section of the mandala."""
    radius1 = 50
    turt.color(color_list[0])
    turt.begin_fill()
    graph_sin_theta_transformation(turt,color_list[0],0,180,0,0,radius1,3,0)
    graph_sin_theta_transformation(turt,color_list[0],0,180,0,0,radius1,3,180)
    turt.end_fill()
    for x in range(6):
        line(turt,radius1,False)
        turt.lt(60)

    """This draws the next section of the mandala - 12 tangent circles"""
    small_circ_radius = radius1 * math.sin(math.radians(15)) / (1 - math.sin(math.radians(15)))
    radius2=radius1+2*small_circ_radius
    turt.color(color_list[1])
    separator(turt,radius1,small_circ_radius*2,1,True)
    turt.fillcolor('white')
    for x in range(12):
        turt.begin_fill()
        turt.circle(small_circ_radius)
        turt.end_fill()
        turt.circle(radius2,extent=30)

    """This draws a separator around the 2 sections we have so far."""
    turt.color(color_list[2])
    separator(turt,radius2,15,60,False)
    separator(turt,radius2+15,5,1,True)
    radius3 = radius2 + 20

    """This draws the background for the next section of the mandala."""
    turt.color(color_list[3])
    circ240_radius = radius3/math.sqrt(3)
    for x in range(6):
        turt.rt(90)
        turt.begin_fill()
        turt.circle(circ240_radius,extent=240)
        turt.rt(90)
        turt.circle(radius3,extent=-60)
        turt.end_fill()
        turt.circle(radius3,extent=60)

    """This draws the design in the next section of the mandala."""
    circ240_dist = circ240_radius*2
    for x in range(6):
        big_angle=60*x
        turt.up()
        center=(circ240_dist*math.cos(math.radians(big_angle)),circ240_dist*math.sin(math.radians(big_angle)))
        turt.goto(center)
        turt.down()
        for y in range(6):
            small_angle = -16 + 42 * y
            turt.fillcolor('white')
            turt.begin_fill()
            graph_sin_theta_transformation(turt,color_list[3],0,60,center[0],center[1],circ240_radius,3,big_angle+small_angle-120)
            turt.end_fill()

    """This draws a circle, then a three-layer separator around what we have so far."""
    radius4 = circ240_dist + circ240_radius
    turt.up()
    turt.goto(radius4,0)
    turt.lt(90)
    turt.down()
    turt.color(color_list[4])
    turt.circle(radius4)
    separator(turt,radius4,5,1,True)
    separator(turt,radius4+5,20,90,False)
    separator(turt,radius4+25,5,1,True)
    radius5 = radius4 + 30

    """This draws the next layer - 30 tangent circles with every 5th one filled in."""
    tiny_radius = radius5*math.sin(math.radians(6))/(1-math.sin(math.radians(6)))
    turt.color(color_list[5])
    for x in range(30):
        turt.rt(180)
        if x%5==0:
            turt.begin_fill()
            turt.circle(tiny_radius)
            turt.end_fill()
        else:
            turt.circle(tiny_radius)
        turt.rt(180)
        turt.up()
        turt.circle(radius5,extent=12)
        turt.down()

    """This draws the final part - ornaments at 60º intervals on the outside of what has been drawn."""
    final_dist = math.cos(math.radians(5)) * (radius5 + tiny_radius)
    turt.color(color_list[6])
    for x in range(6):
        angle = 60 * x
        center = (final_dist*math.cos(math.radians(angle)),final_dist*math.sin(math.radians(angle)))
        turt.up()
        turt.goto(center)
        turt.seth(angle-30)
        turt.fd(radius1)
        turt.down()
        turt.dot(10)
        graph_sin_theta_transformation(turt,color_list[6],18,36,center[0],center[1],radius1,5,angle-30-18)
        turt.seth(angle)
        line(turt,radius1,True)
        graph_sin_theta_transformation(turt,color_list[6],0,18,center[0],center[1],radius1,5,angle+30-18)
        turt.dot(10)
    win.exitonclick()