import turtle
win = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
turt.ht()
import math

from polar_coordinate_graphing import graph_sin_theta_transformation
from color_shading import shading

def line(t,length):
    t.fd(length)
    t.bk(length)

def separator(t,inside_radius,thickness,num_separators):
    t.up()
    t.goto(0,-1*(inside_radius+thickness))
    t.seth(0)
    t.down()
    for a in range(num_separators):
        t.lt(90)
        line(t,thickness)
        t.rt(90)
        t.circle(inside_radius+thickness,extent=int(360/num_separators))

if __name__ == '__main__':
    """
    This is starting off by looking very nice. Just maybe not what I want, but I also don't want to delete it.
    I found an inspiration picture that I think I can mimic/adapt.
    This will challenge me more in terms of creativity and coding.
    
    Starting with a purple color just so I can see it. Will give user option of ROYGBVioletPink, I have start to end chosen already.
    For now I will try going light in the middle to dark on the outside. Maybe that should be the other way around.
    """

    """Will have to do a thing if they give me a letter that dne here"""
    color_dict={'R':None,'O':None,'Y':None,'G':None,'B':None,'V':shading('#f0c4ff','#bb02fa',8),'P':None}
    color_list=color_dict['V']
    print(color_list)

    radius1 = 50 #may respond to user later.

    #draws the central 6 petals filled in the lightest color
    turt.color(color_list[0])
    turt.begin_fill()
    graph_sin_theta_transformation(turt,color_list[0],0,180,0,0,radius1,3,0)
    turt.end_fill()
    turt.begin_fill()
    graph_sin_theta_transformation(turt,color_list[0],0,180,0,0,radius1,3,180)
    turt.end_fill()

    #draws the circle around the 6 petals with radius1
    turt.up()
    turt.goto(0,-1*radius1)
    turt.down()
    turt.circle(radius1)

    #draws the 12 dividing lines through the center
    turt.up()
    turt.goto(0,0)
    turt.seth(0)
    turt.down()
    for x in range(6):
        line(turt,50)
        turt.lt(60)

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

    #draws a separator around what we have so far
    turt.color(color_list[2])
    separator(turt,radius2,15,60)
    radius3 = radius2 + 15

    #draws 6 partial circles coming off of the central figure
    turt.color(color_list[4])
    circ240_radius = radius3/math.sqrt(3)
    for x in range(6):
        turt.rt(90)
        turt.circle(circ240_radius,extent=240)
        turt.rt(90)

    #draws 6 petals inside each of the partial circles
    circ240_dist = circ240_radius*2
    for x in range(6):
        big_angle=60*x
        turt.up()
        center=(circ240_dist*math.cos(math.radians(big_angle)),circ240_dist*math.sin(math.radians(big_angle)))
        turt.goto(center)
        turt.down()
        for y in range(6):
            small_angle = -16 + 42 * y #gotten through trial and error
            #graph_sin_theta_transformation(turt,color_list[3],0,60,center[0],center[1],circ240_radius,3,big_angle+small_angle-120)

    #shades in the areas around the 6 partial circles that is inside the largest circle
    radius4 = circ240_dist + circ240_radius
    turt.up()
    turt.goto(radius4,0)
    turt.lt(90)
    turt.down()
    turt.color(color_list[4])
    for x in range(6):
        turt.begin_fill()
        turt.circle(circ240_radius,extent=120)
        turt.rt(180)
        turt.circle(circ240_radius,extent=120)
        turt.circle(radius4,extent=-60)
        turt.end_fill()
        turt.circle(radius4,extent=60)

    #draws a separator around everything we have so far.
    separator(turt,radius4,25,60)
    radius5 = radius4 + 25

    #draws 30 tiny circles around what we have so far.
    tiny_radius = radius5*math.sin(math.radians(6))/(1-math.sin(math.radians(6)))
    turt.color(color_list[6])
    for x in range(30):
        turt.rt(180)
        if x%5==0:
            turt.begin_fill()
            turt.circle(tiny_radius)
            turt.end_fill()
        else:
            turt.circle(tiny_radius)
        turt.rt(180)
        turt.circle(radius5,extent=12)

    # radius6 = radius5 + 2 * tiny_radius
    # turt.up()
    # turt.goto(radius6,0)
    # turt.down()
    # turt.lt(90)
    # turt.circle(radius6)
    # #draws little firework thingies at the topmost part of each partial circle. save for end?
    # turt.color(color_list[7])
    # turt.pensize(5)
    # for x in range(6):
    #     turt.rt(90)
    #     for y in range(3):
    #         line(turt,35-10*y)
    #         turt.rt(30)
    #     turt.lt(120)
    #     for y in range(1,3):
    #         line(turt,35-10*y)
    #         turt.lt(30)
    #     turt.up()
    #     turt.circle(radius6, extent=60)
    #     turt.down()

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
    print("End state: ",turt.pos(),turt.heading())
    win.exitonclick()


