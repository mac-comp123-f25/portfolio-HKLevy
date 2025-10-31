import turtle
def draw_nested_squares(turtle):
    for x in range(8):
        side_length = 10*(x+1)
        for y in range(4):
            turtle.forward(side_length)
            turtle.left(90)

win = turtle.Screen()
squares = turtle.Turtle()
draw_nested_squares(squares)
win.exitonclick()