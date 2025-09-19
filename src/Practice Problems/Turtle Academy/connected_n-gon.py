import turtle
wn = turtle.Screen()
t = turtle.Turtle()
def get_points(n,side_length):
    #figure out how to center this
    point_list=[]
    angle = 180-(180*(n-2)/n)
    for x in range(n):
        t.fd(side_length)
        t.lt(angle)
        t.dot(5)
        point_list.append(t.pos())
    return point_list
get_points(8,100)
wn.exitonclick()