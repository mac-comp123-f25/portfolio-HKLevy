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
    color_dict={'R':shading('#ffcfcf','#ff0000',7), #feels better with lighter colors in the middle
                'O':shading('#ffe8c9','#ff9500',7),
                'Y':shading('#fffaa3','#fff200',7),
                'G':shading('#b3ffb8','#00ff11',7),
                'B':shading('#b5eaff','#00b7ff',7),
                'V':shading('#f0c4ff','#bb02fa',7),
                'P':shading('#ffe8f8','#ff00b3',7)}

    print(""" –––––Color Options–––––
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
    working_options=['R','O','Y','G','B','V','P','C']

    if keyword == 'R':
        color_list=color_dict['R']
    elif keyword == 'O':
        color_list=color_dict['O']
    elif keyword == 'Y':
        color_list=color_dict['Y']
    elif keyword == 'G':
        color_list=color_dict['G']
    elif keyword == 'B':
        color_list=color_dict['B']
    elif keyword == 'V':
        color_list=color_dict['V']
    elif keyword == 'P':
        color_list=color_dict['P']
    elif keyword == 'C':
        print("Enter your colors in the form rrggbb. Do not include # before your entry.")
        print()
        acceptable_characters=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        condition=False
        while condition==False:
            start_color=input("What color do you want on the inside of the mandala?")
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
                print("Enter your color again. It must be in the form rrggbb. Do not include a #.")

        condition=False
        while condition==False:
            end_color=input("What color do you want on the outside of the mandala?")
            pt1=True
            pt2=True
            if len(start_color)!=6:
                pt1=False
            for x in end_color:
                if x not in acceptable_characters:
                    pt2=False
            if pt1==True and pt2==True:
                condition=True
            else:
                print("Enter your color again. It must be in the form rrggbb. Do not include a #.")
        color1='#'+start_color
        color2='#'+end_color
        color_list=shading(color1,color2,7)


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
        line(turt,radius1)
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

    #draws poofs coming out of what we have so far.
    final_dist = math.cos(math.radians(5)) * (radius5 + tiny_radius)
    turt.color(color_list[7])
    for x in range(6):
        angle = 60 * x
        center = (final_dist*math.cos(math.radians(angle)),final_dist*math.sin(math.radians(angle)))
        turt.up()
        turt.goto(center)
        turt.lt(angle+30-18)
        turt.fd(radius3)
        turt.down()
        graph_sin_theta_transformation(turt,color_list[7],18,36,center[0],center[1],radius3,5,angle-30-18)
        turt.seth(angle)
        line(turt,radius3)
        graph_sin_theta_transformation(turt,color_list[7],0,18,center[0],center[1],radius3,5,angle+30-18)
    print("End state: ",turt.pos(),turt.heading())
    win.exitonclick()


