"""
Graphs some functions with transformations on a polar graph.
Polar graphs use r (distance from the origin) and theta
(counter-clockwise angle of rotation from facing east, given in radians)
rather than x (horizontal distance) and y (vertical distance)

@author: Helen K. Levy (hlevy@macalester.edu)
"""
import turtle
import math


def draw_axes(length,origin_x,origin_y):
    """Draws the main axes of the polar graph given by
    theta = 0, theta = π/2, theta = π, and theta = 3π/2.
    :param length: the length of the axes
    origin_x: the x coordinate of the origin
    origin_y: the y coordinate of the origin
    :return: None"""
    t.color('black')
    t.width(5)
    t.up()
    t.goto(origin_x,origin_y)
    t.down()
    for x in range(4):
        t.fd(length)
        t.bk(length)
        t.lt(90)

def setup_turtle(color,width,start_x,start_y):
    """Sets up the turtle object for what will be graphed.
    :param color: the color of the turtle
    :param width: the width of the turtle
    :param start_x: the x coordinate of the starting point
    :param start_y: the y coordinate of the starting point
    :return: None"""
    t.up()
    t.goto(start_x,start_y)
    t.down()
    t.color(color)
    t.width(width)

def graph_sin_theta_transformation(color,domain_start,domain_end,center_x,center_y,size,petals,rotation):
    """Graphs the function r = size * sin(petals*theta - rotation).
    :param color: The color of the graph's curve
    :param domain_start: The starting value for the domain, given in degrees
    :param domain_end: The ending value for the domain, given in degrees
    :param center_x: The x coordinate of the center of the graph
    :param center_y: The y coordinate of the center of the graph
    :param size: The farthest away from the origin the graph will get
    :param petals: The number of "petals" in the "flower"-like graph
    :param rotation: The angle of rotation (counter-clockwise from east) in degrees
    :return: None
    """
    setup_turtle(color,2,center_x,center_y)

    true_rotation = petals * math.radians(rotation*petals)
    for a in range(domain_start,domain_end):
        theta = math.radians(a)
        r = size * math.sin(petals*theta - true_rotation)
        x = r * math.cos(theta) + center_x
        y = r * math.sin(theta) + center_y
        if a==0:
            t.up()
            t.goto(x,y)
            t.down()
        else:
            t.goto(x,y)

def graph_cos_theta_transformation(color,domain_start,domain_end,center_x,center_y,size,petals,rotation):
    """Graphs the function r = size * cos(n*theta).
    :param color: The color of the graph
    :param domain_start: The starting value for the domain, given in degrees
    :param domain_end: The ending value for the domain, given in degrees
    :param center_x: The x coordinate of the center of the graph
    :param center_y: The y coordinate of the center of the graph
    :param size: The farthest away from the origin graph will get
    :param petals: The number of "petals" in the flower-like graph
    :param rotation: The angle of rotation (counter-clockwise from east) in degrees
    :return: None"""
    setup_turtle(color,2,center_x,center_y)

    true_rotation = petals * math.radians(rotation*petals) #something is off here. not sure what.
    for a in range(domain_start,domain_end):
        theta = math.radians(a)
        r = size * math.cos(petals*theta - true_rotation)
        x = r * math.cos(theta) + center_x
        y = r * math.sin(theta) + center_y
        if a==0:
            t.up()
            t.goto(x,y)
            t.down()
        else:
            t.goto(x,y)

#sets up the turtle and screen
win = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

draw_axes(275,0,0)
# graph_sin_theta_transformation('red',0,180,0,0,100,5,0)
# graph_sin_theta_transformation('blue',0,180,0,0,50,5,36)
graph_cos_theta_transformation('purple',0,360,0,0,100,2,0)
graph_cos_theta_transformation('green',0,360,0,0,50,2,45)

win.exitonclick()