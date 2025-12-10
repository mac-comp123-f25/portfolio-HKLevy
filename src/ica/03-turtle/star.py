import turtle
window = turtle.Screen()
gabby = turtle.Turtle()
gabby.shape('turtle')
gabby.color('lightskyblue')
for i in range(5):
    gabby.fd(300)
    gabby.rt(144)

helen = turtle.Turtle()
helen.up()
helen.goto(-150,200)
helen.color("plum")
helen.shape('arrow')
helen.down()
for i in range (5):
    helen.fd(250)
    helen.rt(144)

window.exitonclick()