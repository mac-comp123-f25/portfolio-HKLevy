"""
The purpose of this program is to create 5 flowers.
Each flower is made of 5 big circles, 5 small circles, a center dot, and a turtle shape.
There are 4 turtles in this code.
"""

import turtle
import math
def drawFiveCircles(turt,radius,centerX,centerY):
    """
    This function draws 5 circles around a center point.
    :param turt: the name of the turtle drawing the circles
    :param radius: the radius of the circles
    :param centerX: the x-coordinate of the center point
    :param centerY: the y-coordinate of the center point
    :return: None
    """
    turt.up()
    turt.goto(centerX,centerY)
    turt.down()
    for x in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt,centerX,centerY):
    """
    This function draws a center circle.
    :param turt: the name of the turtle drawing the circle
    :param centerX: The x-coordinate of the starting point
    :param centerY: The y-coordinate of the starting point
    :return: None
    """
    turt.up()
    turt.goto(centerX,centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

def drawBee(turt,centerX,centerY):
    """
    This function stamps a turtle. It does not draw a bee
    :param turt: this is the turtle that stamps the turtle shape
    :param centerX: this is the x-coordinate of where the turtle will go
    :param centerY: this is the y-coordinate of where the turtle will go
    :return: None
    """
    turt.up()
    turt.goto(centerX,centerY)
    turt.down()
    turt.stamp()


win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFiveCircles(sepalTurtle,50,0,0)
drawFiveCircles(petalTurtle,25,0,0)
drawCenterCircle(centerTurtle,0,-15)
drawBee(stampTurtle,-2,0)

drawFiveCircles(sepalTurtle,50,0,220)
drawFiveCircles(petalTurtle,25,0,220)
drawCenterCircle(centerTurtle,0,205)
drawBee(stampTurtle,-2,220)

drawFiveCircles(sepalTurtle,50,220,0)
drawFiveCircles(petalTurtle,25,220,0)
drawCenterCircle(centerTurtle,220,-15)
drawBee(stampTurtle,218,0)

drawFiveCircles(sepalTurtle,50,0,-220)
drawFiveCircles(petalTurtle,25,0,-220)
drawCenterCircle(centerTurtle,0,-235)
drawBee(stampTurtle,-2,-220)

drawFiveCircles(sepalTurtle,50,-220,0)
drawFiveCircles(petalTurtle,25,-220,0)
drawCenterCircle(centerTurtle,-220,-15)
drawBee(stampTurtle,-222,0)

win.exitonclick()