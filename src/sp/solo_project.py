import turtle
win = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
turt.ht()
import math

from polar_coordinate_graphing import graph_sin_theta_transformation

if __name__ == '__main__':
    """
    This is starting off by looking very nice. Just maybe not what I want, but I also don't want to delete it.
    I found an inspiration picture that I think I can mimic/adapt.
    This will challenge me more in terms of creativity and coding.
    """
    radius1 = 50
    graph_sin_theta_transformation(turt,'black',0,180,0,0,radius1,3,0)
    graph_sin_theta_transformation(turt,'black',0,180,0,0,radius1,3,180)
    turt.up()
    lstpts=[]
    turt.goto(0,-50)
    turt.down()
    for x in range(12):
        lstpts.append(turt.pos())
        turt.circle(50,extent=30)
    for x in range(1,len(lstpts),2):
        turt.up()
        turt.goto(lstpts[x])
        turt.down()
        turt.goto(0,0)
    turt.up()
    turt.goto(0,-1*radius1)
    turt.rt(180)
    turt.down()
    small_circ_radius = radius1*math.sin(math.radians(15))/(1-math.sin(math.radians(15)))
    for x in range(12):
        turt.circle(small_circ_radius)
        turt.rt(180)
        turt.circle(50,extent=30)
        turt.rt(180)
    radius2 = radius1+2*small_circ_radius
    turt.up()
    turt.goto(0,-1*(radius2))
    turt.seth(0)
    turt.down()
    turt.circle(radius2)

    radius3 = radius2+15
    turt.up()
    turt.goto(0,-1*(radius3))
    turt.down()
    turt.circle(radius3)

    # turt.up()
    # turt.goto(0,-0)
    # turt.seth(0)
    # turt.rt(30)
    # turt.down()
    # turt.pensize(2)
    # turt.color('red')
    # turt.fd(100)
    # turt.lt(90)
    # turt.circle(100,extent=240)
    # turt.lt(90)
    # turt.fd(100)
    # for y in range(6):
    #     small_angle = -10 + 40 * y
    #     graph_sin_theta_transformation(turt,'red',0,60,0,0,100,3,small_angle-30)


    for x in range(60):
        turt.lt(90)
        turt.fd(15)
        turt.bk(15)
        turt.rt(90)
        turt.circle(radius3,extent=6)

    circ240_radius = (radius3)/math.sqrt(3)
    for x in range(6):
        turt.rt(90)
        turt.circle(circ240_radius,extent=240)
        turt.rt(90)

    circ240_dist = circ240_radius*2
    """This center for each circle is right. The petals could get a tiny tiny bit more spread out."""
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
            small_angle = -16 + 42 * y # i like that a lot :)
            graph_sin_theta_transformation(turt,'black',0,60,center[0],center[1],circ240_radius,3,big_angle+small_angle-120)



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


