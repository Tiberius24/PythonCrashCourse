import turtle
import random

def turtleWalk(n):
    x_cor = int(n.xcor())
    y_cor = int(n.ycor())

    while x_cor > -199 and x_cor < 199 and y_cor > -199 and y_cor < 199:
        coin = random.randrange(0, 2)
        if coin == 0:
            n.lt(90)
        else:
            n.rt(90)
        n.fd(50)
        n.dot()
        x_cor = int(n.xcor())
        y_cor = int(n.ycor())


def main():

    wn = turtle.Screen()
    wn.setworldcoordinates(-200, -200, 200, 200)
    wn.bgcolor("light green")

    niko = turtle.Turtle()
    niko.color("deep sky blue")
    niko.shape("turtle")
    niko.speed(10)
    niko.pu()

    turtleWalk(niko)

    wn.exitonclick()

if __name__ == '__main__':
    main()