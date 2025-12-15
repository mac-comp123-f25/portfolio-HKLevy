import turtle

def tele_turtle(n):
  win = turtle.Screen()
  tele_t = turtle.Turtle()
  for i in range(n):
    move = input("Enter next move: ")
    do_move(tele_t, move)
  win.exitonclick()

def do_move(turt, move):
    if move =='f':
        turt.fd(15)
    elif move =='b':
        turt.bk(15)
    elif move =='r':
        turt.rt(90)
    elif move=='l':
        turt.lt(90)
    else:
        print("Warning message")

if __name__ == "__main__":
  tele_turtle(10)   # will ask the user to enter 10 commands, use other
                    # values and notice what will happen
