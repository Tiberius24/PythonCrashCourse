import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightblue")

lance = turtle.Turtle()
andy = turtle.Turtle()
mike = turtle.Turtle()
sean = turtle.Turtle()
judge = turtle.Turtle()

lance.speed(5)
andy.speed(5)
judge.speed(7)

lance.color("blue")
andy.color("red")
mike.color("yellow")
sean.color("orange")

lance.shape("turtle")
andy.shape("turtle")
mike.shape("turtle")
sean.shape("turtle")

lance.penup()
andy.penup()
judge.penup()
mike.penup()
sean.penup()

judge.pensize(4)

judge.goto(-180,80)
lance.goto(-195,15)
andy.goto(-195,40)
mike.goto(-195,-15)
sean.goto(-195,-40)


judge.rt(90)
judge.pendown()
judge.fd(150)
judge.bk(150)
judge.penup()
judge.goto(190,80)
judge.pendown()
judge.fd(150)
judge.bk(150)
judge.penup()
judge.rt(90)
judge.goto(190,80)

for i in range(100):
    andy.fd(random.randrange(10))
    lance.fd(random.randrange(10))
    mike.fd(random.randrange(10))
    sean.fd(random.randrange(10))


wn.exitonclick()