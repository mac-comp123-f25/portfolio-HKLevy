"""
Graphs some functions on a polar graph.
Polar graphs use r (distance from the origin) and
theta (counter-clockwise angle of rotation from facing east, given in radians)
rather than x (horizontal distance) and y (vertical distance)

@author: Helen K. Levy (hlevy@macalester.edu)
"""
import turtle
import math


def draw_axes(length):
    """Draws the main axes of the polar graph given by
    theta = 0, theta = π/2, theta = π, and theta = 3π/2.
    :param length: the length of the axes
    :return: None"""
    t.color('black')
    t.width(5)
    t.up()
    t.goto(0,0)
    t.down()
    for x in range(4):
        t.fd(length)
        t.bk(length)
        t.lt(90)

def setup_turtle(color,width):
    """Sets up the turtle object for what will be graphed.
    :param color: the color of the turtle
    :param width: the width of the turtle
    :return: None"""
    t.up()
    t.goto(0,0)
    t.down()
    t.color(color)
    t.width(width)

def graph_sin_ntheta(n,color,domain_start,domain_end):
    """
    Graphs the function r = sin(n*theta).
    :param n: The number of "petals" in the flower-like graph
    :param color: The color of the graph
    :param domain_start: The starting value for the domain, given in degrees
    :param domain_end: The ending value for the domain, given in degrees
    :return: None
    """
    setup_turtle(color,2)
    for a in range(domain_start,domain_end):
        theta = math.radians(a)
        r = 100 * math.sin(n*theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if a==0:
            t.up()
            t.goto(x,y)
            t.down()
        else:
            t.goto(x,y)

def graph_cos_ntheta(n,color,domain_start,domain_end):
    """Graphs the function r = cos(n*theta).
    :param n: The number of "petals" in the flower-like graph
    :param color: The color of the graph
    :param domain_start: The starting value for the domain, given in degrees
    :param domain_end: The ending value for the domain, given in degrees
    :return: None"""
    setup_turtle(color,2)
    for a in range(domain_start,domain_end):
        theta = math.radians(a)
        r = 100 * math.cos(n*theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
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

draw_axes(275)
graph_sin_ntheta(7,'purple',0,180)
graph_cos_ntheta(5,'blue',0,180)

win.exitonclick()