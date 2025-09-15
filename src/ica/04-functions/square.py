import turtle
def turtle_square(sqTurt,side_len):
    for x in range(4):
        sqTurt.fd(side_len)
        sqTurt.rt(90)

wn = turtle.Screen()
t = turtle.Turtle()
turtle_square(t,100)
turtle_square(t,50)
turtle_square(t,200)
wn.exitonclick()