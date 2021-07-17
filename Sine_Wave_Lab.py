
import turtle, math, random

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.setworldcoordinates(0,-1.25,360,1.25)

niko = turtle.Turtle()
niko.pensize(2)
niko.speed(5)
niko.penup()
niko.goto(-1,0)
niko.pendown()
niko.fd(360)
niko.penup()
niko.goto(182,1.25)
niko.pendown()
niko.rt(90)
niko.fd(2.50)
niko.penup()
niko.goto(-1,0)
niko.pendown()

x = 0
for angle in range(360):
    y = math.sin(math.radians(angle))
    x = x+1
    niko.goto(x,y)


wn.exitonclick()