import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("Cyan")
norb = turtle.Turtle()
norb.shape("turtle")
norb.speed(15)

# def drawSquare(t, sz):
#     """Make turtle t draw a square of sz."""
#
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
#
# def drawTriangel(t, sz):
#     t.penup()
#     t.goto(-100,100)
#     t.pendown()
#     for i in range(3):
#         t.fd(sz)
#         t.lt(120)
#
# def drawoctagon(t,sz):
#     t.penup()
#     t.goto(100,-100)
#     t.pendown()
#     for i in range(8):
#         t.fd(sz)
#         t.lt(45)
#
# drawSquare(norb,50)
# drawTriangel(norb,50)
# drawoctagon(norb,25)

def drawpolygon(t, sidelenght, numsides):
    for i in range(numsides):
        turn = 360 / numsides
        t.fd(sidelenght)
        t.lt(turn)

radius = 20
circum = 2*math.pi*radius
sides = 360
length = 360 / circum

norb.penup()
# norb.goto()
norb.pendown()

drawpolygon(norb,length,sides)

norb.penup()
norb.home()
wn.exitonclick()