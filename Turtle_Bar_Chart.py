import turtle


def printNumber(t, height):
    x = t.xcor()
    y = t.ycor()+2
    t.penup()
    t.goto(x,y)
    t.write(height, align="center" ,font=("Arial", 10))
    x = t.xcor()
    y = t.ycor() - 2
    t.goto(x, y)
    t.pendown()


def drawBar(t, height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)  # height of the bar graph
    t.rt(90)
    t.fd(20)  # Width of the bar graph
    printNumber(t, height)
    t.fd(20)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    t.fd(5)  # Setup the turtle to start the next bar


def main():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    xs = [48, 117, 200, 240, 160, 260, 220]
    maxheight = max(xs)
    numbars = len(xs)
    border = 10
    wn.setworldcoordinates(0-border, 0-border, 45*numbars+border, maxheight+border)
    niko = turtle.Turtle()
    niko.color("deep sky blue")
    niko.pencolor("navy")
    niko.fillcolor("red")
    niko.pensize(3)
    niko.speed(10)

    for v in xs:  # 4 loop to draw the graph based off the number of entries
        drawBar(niko, v)
    wn.exitonclick()


if __name__ == '__main__':
    main()
