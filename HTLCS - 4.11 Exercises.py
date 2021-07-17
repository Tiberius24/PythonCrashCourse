# HTLCS 4.11 Exercises
# My name: Don Trapp

# Question 1
# Write a program that prints We like Python's turtles! 100 times.

# for i in range(100):
#     print("We like Python's turtles!")

# Question 2
# turtle-8-3: Turtle objects have methods and attributes. For example, a turtle has a position and when you move the
# turtle forward, the position changes. Think about the other methods shown in the summary above. Which attributes,
# if any, does each method relate to? Does the method change the attribute?

# The turtle's position is an attribute that is related to invoking the turtle method and the screen method. No.

# Question 3
# Write a program that uses a for loop to print
#    One of the months of the year is January
#    One of the months of the year is February
#    One of the months of the year is March
#    etc ...

# for i in ("January","February","March","April","May","June","July","August","September","October","November",
#                "December"):
#     print("One of the months of the year is",i)

# Question 4
# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
#     Write a loop that prints each of the numbers on a new line.
#     Write a loop that prints each number and its square on a new line.

# for i in (12,10,32,3,66,17,42,99,20):
#     print("The current number for this loop is",i,"and its squared value is",i**2)

# Question 5
# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths,
# all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

# import turtle
# wn = turtle.Screen()
# niko = turtle.Turtle()
# niko.pensize(3)
#
# for i in("triangle","square","hexagon","octagon"):
#     if i == "triangle":
#         angles = 3
#         niko.penup()
#         niko.goto(-100,100)
#     elif i == "square":
#         angles = 4
#         niko.penup()
#         niko.goto(-100, -100)
#     elif i == "hexagon":
#         angles = 6
#         niko.penup()
#         niko.goto(100, 100)
#     elif i == "octagon":
#         angles = 8
#         niko.penup()
#         niko.goto(100, -100)
#     for i in range(angles):
#         niko.pendown()
#         niko.fd(50)
#         degrees = 360 // angles
#         niko.lt(degrees)
#
# wn.exitonclick()

# Question 6
# Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color
# of a regular polygon. The program should draw the polygon and then fill it in.

# import turtle
#
# wn = turtle.Screen()
# koda = turtle.Turtle()
# wn.bgcolor("light green")
# koda.color("brown","black")
#
# sides = int(input("How many sides should the polygon have?"))
# length = int(input("How long should each side be?"))
# color = input("Which color should the polygon be?")
#
# koda.color(color)
# koda.begin_fill()
#
# for i in range(sides):
#     koda.pencolor(color)
#     koda.fd(length)
#     koda.lt(360/sides)
#
# koda.end_fill()
#
# wn.exitonclick()

# Question 7
# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another
# 100 steps, turns another random amount, etc. A social science student records the angle of each turn before
# the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles
# are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking,
# print the current heading

# import turtle
# import random
#
# wn = turtle.Screen()
# wn.bgcolor("light green")
#
# jerad = turtle.Turtle()
# jerad.color("red","black")
# jerad.shape("turtle")
#
#
# jerad.penup()
# for i in range(9):
#     x = random.choice([160, -43, 270, -97, -43, 200, -940, 17, -86])
#     jerad.rt(x)
#     for j in range(10):
#         jerad.fd(10)
#         jerad.dot()
#     jerad.stamp()
#
# print(jerad.pos())
# wn.exitonclick()

# Question 8
# On a piece of scratch paper, trace the following program and show the drawing. When you are done, press run and
# check your answer.


# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.right(90)
# tess.left(3600)
# tess.right(-90)
# tess.left(3600)
# tess.left(3645)
# tess.forward(-100)
#
# wn.exitonclick()

# Question 9
# Write a program to draw a star:

# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("light blue")
#
# norbert = turtle.Turtle()
# norbert.color("orange","red")
# norbert.pencolor("black")
# norbert.pensize(2)
#
# for i in range(5):
#     norbert.fd(100)
#     norbert.rt(144)
#
# wn.exitonclick()

# Question 10
# Write a program to draw a face of a clock that uses turtle stamps.

# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("light green")
#
# niko = turtle.Turtle()
# niko.shape("turtle")
# niko.color("blue")
# niko.pensize(3)
# niko.penup()
# niko.speed(2)
#
# niko.lt(90)
# for i in range(12):
#     niko.fd(75)
#     niko.pd()
#     niko.fd(10)
#     niko.pu()
#     niko.fd(15)
#     niko.stamp()
#     niko.bk(100)
#     niko.rt(360//12)
#
# niko.home()
#
# wn.exitonclick()

# Question 11
# Write a program to draw some kind of picture. Be creative and experiment with the turtle methods provided in
# Summary of Turtle Methods.

# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("blue")
#
# koda = turtle.Turtle()
# koda.color("red")
# koda.pensize(2)
# koda.speed(15)
#
# koda.pu()
# for z in range(13):
#     koda.fd(100)
#     koda.fillcolor("white")
#     koda.begin_fill()
#     for i in range(5):
#         koda.pd()
#         koda.fd(50)
#         koda.rt(144)
#         koda.pu()
#     koda.end_fill()
#     koda.bk(100)
#     koda.rt(360//13)
# koda.penup()
# koda.home()
# koda.hideturtle()
# koda.write("Happy 4th of July!!",align="center",font=("Arial",12,"bold"))
#
# wn.exitonclick()

# Question 12
# Create a turtle and assign it to a variable. When you print its type, what do you get?

# import turtle
#
# honey = turtle.Turtle()
#
# print(type(honey))

# Question 13
# A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is
# 360 / n degrees. Write a program to draw a sprite where the number of legs is provided by the user.

# import turtle
#
# wn = turtle.Screen()
# norbert = turtle.Turtle()
#
# wn.bgcolor("light green")
# norbert.color("red")
# norbert.shape("turtle")
# norbert.speed(15)
#
# legs = int(input("How many legs do you want your sprite to have?"))
#
# for i in range(legs):
#     norbert.fd(100)
#     norbert.stamp()
#     norbert.bk(100)
#     norbert.stamp()
#     norbert.rt(360//legs)
#
#
# wn.exitonclick()
