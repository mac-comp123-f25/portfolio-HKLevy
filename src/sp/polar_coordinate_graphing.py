"""
Graphs some functions with some transformations on a polar graph.
Polar graphs use r (distance from the origin) and theta
(counter-clockwise angle of rotation from facing east, given in radians)
rather than x (horizontal distance) and y (vertical distance)

@author: Helen K. Levy (hlevy@macalester.edu)
"""
import turtle
import math


def setup_turtle(t,color,width,start_x,start_y):
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

def draw_axes(t,length,origin_x,origin_y):
    """Draws the main axes of the polar graph given by
    theta = 0, theta = π/2, theta = π, and theta = 3π/2.
    :param length: the length of the axes
    origin_x: the x coordinate of the origin
    origin_y: the y coordinate of the origin
    :return: None"""
    setup_turtle(t,'black',5,origin_x,origin_y)
    for x in range(4):
        t.fd(length)
        t.bk(length)
        t.lt(90)

def draw_graph(t,theta,r,center_x,center_y,rep):
    """Graphs the point (theta, r)."""
    x = r * math.cos(theta) + center_x
    y = r * math.sin(theta) + center_y
    if rep==0:
        t.up()
        t.goto(x,y)
        t.down()
    else:
        t.goto(x,y)

def graph_sin_theta_transformation(t,color,domain_start,domain_end,center_x,center_y,size,petals,rotation):
    """Graphs the function r = size * sin(petals*theta - rotation) for domain_start ≤ theta ≤ domain_end
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
    setup_turtle(t,color,2,center_x,center_y)

    true_rotation = petals * math.radians(rotation)
    for a in range(domain_start+rotation,domain_end+rotation+1):
        theta = math.radians(a)
        r = size * math.sin(petals*theta - true_rotation)
        if a==domain_start+rotation:
            draw_graph(t, theta, r, center_x, center_y, 0)
        else:
            draw_graph(t,theta,r,center_x,center_y,1)

def graph_cos_theta_transformation(t,color,domain_start,domain_end,center_x,center_y,size,petals,rotation):
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
    setup_turtle(t,color,2,center_x,center_y)

    true_rotation = petals * math.radians(rotation)
    for a in range(domain_start+rotation,domain_end+rotation+1):
        theta = math.radians(a)
        r = size * math.cos(petals*theta - true_rotation)
        if a==domain_start+rotation:
            draw_graph(t, theta, r, center_x, center_y, 0)
        else:
            draw_graph(t,theta,r,center_x,center_y,1)

def graph_sin_theta_degree(t,color,start_x,start_y,size,degree):
    """Graphs the function r = size * sin(theta) ** degree.
    :param color: The color of the graph's curve
    :param start_x: The x coordinate of the starting point
    :param start_y: The y coordinate of the starting point
    :param size: The farthest away from the starting point the graph will get
    :param degree: The degree that sin(theta) is raised to
    :return: None"""
    setup_turtle(t,color,2,start_x,start_y)

    for a in range(181):
        theta=math.radians(a)
        r = size * math.sin(theta) ** degree
        draw_graph(t,theta,r,start_x,start_y,a)

def graph_description(t,caption,center_x,center_y):
    setup_turtle(t,'black',2,center_x,center_y)
    t.write(caption,align='center',font=('Arial',18,'normal'))

if __name__ == '__main__':
    #sets up the turtle and screen
    win = turtle.Screen()
    win.screensize(800,550)
    turt = turtle.Turtle()
    turt.speed(0)

    turt.ht()

    #draws 10 sets of axes
    for a in range(10):
        if a%2==0:
            y = 150
        else:
            y = -150
        x = 250*(a%5) - 500
        draw_axes(turt,100,x,y)

    #draws and labels 10 graphs
    graph_sin_theta_transformation(turt,'red',0,180,-500,150,75,1,0)
    graph_description(turt,"r = sin(θ)",-500,25)

    graph_cos_theta_transformation(turt,'red',0,180,-500,-150,75,1,0)
    graph_description(turt,"r = cos(θ)",-500,-275)

    graph_sin_theta_transformation(turt,'blue',0,180,-250,150,75,3,0)
    graph_description(turt,"r = sin(3θ)",-250,25)

    graph_cos_theta_transformation(turt,'blue',0,180,-250,-150,75,3,0)
    graph_description(turt,"r = cos(3θ)",-250,-275)

    graph_sin_theta_transformation(turt,'blue',0,180,0,150,75,3,90)
    graph_description(turt,"r = sin(3θ)",0,25)
    graph_description(turt,"Rotated 90º",0,0)

    graph_cos_theta_transformation(turt,'blue',0,180,0,-150,75,3,90)
    graph_description(turt,"r = cos(3θ)",0,-275)
    graph_description(turt,"Rotated 90º",0,-300)

    graph_sin_theta_transformation(turt,'green',0,180,250,150,75,5,0)
    graph_description(turt,"r = sin(5θ)",250,25)

    graph_cos_theta_transformation(turt,'green',0,180,250,-150,75,5,0)
    graph_description(turt,"r = cos(5θ)",250,-275)

    graph_sin_theta_transformation(turt,'green',0,36,500,150,75,5,0)
    graph_description(turt,"r = sin(5θ)",500,25)
    graph_description(turt,"0º ≤ θ ≤ 36º",500,0)

    graph_cos_theta_transformation(turt,'green',18,126,500,-150,75,5,0)
    graph_description(turt,"r = cos(5θ)",500,-275)
    graph_description(turt,"18º ≤ θ ≤ 126º",500,-300)

    win.exitonclick()