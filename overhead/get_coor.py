import turtle

screen = turtle.Screen()
screen.addshape("map.gif")
turtle.shape("map.gif")
i = 0
fp = open("x.txt", "w")
fp1 = open("y.txt", "w")


def add(x, y):
    global i
    i += 1
    fp.write(str(x)+"\n")
    fp1.write(str(y)+"\n")
    print(i, end=" ")

    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(x, y)
    tim.write("Ok")


turtle.onscreenclick(add)
screen.onkeyrelease(screen.exitonclick, "a")
turtle.mainloop()

fp.close()
fp1.close()
