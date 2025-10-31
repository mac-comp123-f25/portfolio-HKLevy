import turtle
win = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
turt.ht()
import math

from polar_coordinate_graphing import graph_sin_theta_transformation
from color_shading import shading

if __name__ == '__main__':
    """
    This is starting off by looking very nice. Just maybe not what I want, but I also don't want to delete it.
    I found an inspiration picture that I think I can mimic/adapt.
    This will challenge me more in terms of creativity and coding.
    
    Starting with a purple color just so I can see it. Will give user option of ROYGBVioletPink, I have start to end chosen already.
    For now I will try going light in the middle to dark on the outside. Maybe that should be the other way around.
    """

    """Will have to do a thing if they give me a letter that dne here"""
    color_dict={'R':None,'O':None,'Y':None,'G':None,'B':None,'V':shading('#f0c4ff','#bb02fa',10),'P':None}
    color_list=color_dict['V']

    radius1 = 50 #may respond to user later.

    #draws the central 6 petals filled in the lightest color
    turt.color(color_list[0])
    turt.begin_fill()
    graph_sin_theta_transformation(turt,color_list[0],0,180,0,0,radius1,3,0)
    turt.end_fill()
    turt.begin_fill()
    graph_sin_theta_transformation(turt,color_list[0],0,180,0,0,radius1,3,180)
    turt.end_fill()

    #draws the circle with radius1
    turt.up()
    lstpts12=[]
    turt.goto(0,-1*radius1)
    turt.down()
    for x in range(12):
        lstpts12.append(turt.pos())
        turt.circle(radius1,extent=30)

    #draws the 12 dividing lines through the center
    for x in range(1,len(lstpts12),2):
        turt.up()
        turt.goto(lstpts12[x])
        turt.down()
        turt.goto(0,0)

    #draws the 12 small circles each with radius small_circ_radius and shades around them
    small_circ_radius = radius1*math.sin(math.radians(15))/(1-math.sin(math.radians(15)))
    radius2 = radius1 + 2 * small_circ_radius

    turt.up()
    turt.goto(0,-1*radius2)
    turt.seth(0)
    turt.down()
    turt.color(color_list[1])
    for x in range(12):
        #draws the small circle
        turt.circle(small_circ_radius)

        #shades the more outer part
        turt.begin_fill()
        turt.circle(radius2,extent=30)
        turt.circle(small_circ_radius,extent=-105)
        turt.rt(180)
        turt.circle(small_circ_radius,extent=-105)
        turt.end_fill()

        #shades the more inner part
        turt.circle(small_circ_radius,extent=180)
        turt.rt(180)
        turt.begin_fill()
        turt.circle(radius1,extent=30)
        for y in range(2):
            turt.rt(180)
            turt.circle(small_circ_radius,extent=75)
        turt.end_fill()
        turt.circle(small_circ_radius,extent=180)

        #moves to next circle spot
        turt.circle(radius2,extent=30)

    #draws a circle of radius2 around the 12 small circles
    turt.up()
    turt.goto(0,-1*(radius2))
    turt.seth(0)
    turt.down()
    turt.circle(radius2)

    #draws a separator around what we have so far
    radius3 = radius2+15
    turt.up()
    turt.goto(0,-1*(radius3))
    turt.down()
    turt.color(color_list[2])
    for x in range(60):
        turt.lt(90)
        turt.fd(15)
        turt.bk(15)
        turt.rt(90)
        turt.circle(radius3,extent=6)

    #draws 6 partial circles coming off of the central figure
    turt.color(color_list[4]) #intentionally skipping one.
    circ240_radius = (radius3)/math.sqrt(3)
    for x in range(6):
        turt.rt(90)
        turt.circle(circ240_radius,extent=240)
        turt.rt(90)

    #draws 6 petals inside each of the partial circles
    circ240_dist = circ240_radius*2
    for x in range(6):
        big_angle=60*x
        turt.up()
        turt.goto(0,0)
        turt.seth(0)
        turt.lt(big_angle)
        turt.fd(circ240_dist)
        center=turt.pos()

        turt.down()
        for y in range(6):
            #small_angle = -10 + 40 * y
            #small_angle = -13 + 41 * y closer but not tangent
            small_angle = -16 + 42 * y # I like that a lot :) keeping others for reference.
            graph_sin_theta_transformation(turt,color_list[3],0,60,center[0],center[1],circ240_radius,3,big_angle+small_angle-120)

    #draws a circle around everything we have so far
    radius4 = circ240_dist + circ240_radius
    turt.up()
    turt.goto(0,-1*radius4)
    turt.seth(0)
    turt.down()
    turt.color(color_list[4]) #intentionally going back to what we had before.
    turt.circle(radius4,extent=30)

    #shades in the areas around the 6 partial circles that is inside the largest circle
    for x in range(6):
        turt.begin_fill()
        turt.circle(circ240_radius,extent=120)
        turt.rt(180)
        turt.circle(circ240_radius,extent=120)
        turt.circle(radius4,extent=-60)
        turt.end_fill()
        turt.circle(radius4,extent=60)

    #draws a separator around everything we have so far
    radius5 = radius4 + 25
    turt.up()
    turt.rt(90)
    turt.fd(25)
    turt.lt(90)
    turt.down()
    turt.color(color_list[5])
    for x in range(60):
        turt.circle(radius5,extent=6)
        turt.lt(90)
        turt.fd(25)
        turt.bk(25)
        turt.rt(90)
    turt.pensize(5)
    turt.circle(radius5)
    turt.pensize(2)

    """Take user input in terms of number of layers and color and size.
    layers = 5 #will become user inputted later.
    start_size = 50
    inc_size = 30
    small_dot = inc_size/3
    large_dot = start_size/3
    for x in range(layers):
        petal_size = start_size + x * inc_size
        graph_sin_theta_transformation(turt,'black',0,180,0,0,petal_size,3,30)
        graph_sin_theta_transformation(turt,'black',0,180,0,0,petal_size,3,90)
        turt.up()
        for y in range(6):
            turt.fd(petal_size)
            turt.dot(small_dot)
            turt.bk(petal_size)
            turt.rt(60)
        turt.down()
    turt.dot(large_dot)

    #first, for the outsides
    turt.rt(15)
    petal_size = start_size + inc_size*layers
    for x in range(12):
        angle = 15+30*x
        if x%2==0:
            graph_sin_theta_transformation(turt,'black',18,36,0,0,petal_size,5,angle-18)
        else:
            graph_sin_theta_transformation(turt,'black',0,18,0,0,petal_size,5,angle-18)
        turt.up()
        turt.goto(0,0)
        turt.lt(30)
        turt.fd(petal_size)
        turt.dot(small_dot) #small dot for now
        turt.bk(petal_size)
        turt.down()

    #now for the insides. still need to figure out how to place the dots
    turt.lt(30)
    petal_size = start_size + inc_size*(layers+4)
    for x in range(12):
        angle = 15+30*x
        if x%2==0:
            graph_sin_theta_transformation(turt,'black',25,36,0,0,260,5,angle-18)
        else:
            graph_sin_theta_transformation(turt,'black',0,11,0,0,260,5,angle-18)
            
    Still experimenting with petal sizes for inside and outside poofs"""
    win.exitonclick()


