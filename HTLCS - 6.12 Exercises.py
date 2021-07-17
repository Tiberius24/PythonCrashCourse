# HTLCS 6.12 Exercises
# My name: Don Trapp

# Question 1
# Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side
# is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when
# the program ends.

# import turtle
#
# def drawSquare(h, length):
#     for i in range(4):
#         h.fd(length)
#         h.lt(90)
#
# def startDrawing(h):
#     h.pu()
#     h.goto(-80,0)
#     h.pd()
#     x = -80
#     for i in range(4):
#         size = 20
#         drawSquare(h, size)
#         h.pu()
#         x = x + 40
#         h.goto(x, 0)
#         h.pd()
#     h.pu()
#     h.hideturtle()
#     h.home()
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("lawn green")
#     wn.setworldcoordinates(-100,-100,100,100)
#     honey = turtle.Turtle()
#     honey.color("chocolate")
#     honey.pencolor("hot pink")
#     honey.pensize(3)
#     honey.speed(3)
#
#     startDrawing(honey)
#
#     wn.exitonclick()
# main()

# Question 2
# Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is
# 20 units bigger, per side, than the one inside it

# import turtle
#
# def drawSquare(k, length):
#     for i in range(4):
#         k.fd(length)
#         k.lt(90)
#
# def startDrawing(k):
#     size = 20
#     for i in range(5):
#         drawSquare(k, size)
#         k.pu()
#         x = k.xcor() - 10
#         y = k.ycor() - 10
#         k.goto(x,y)
#         k.pd()
#         size = size + 20
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("lawn green")
#     wn.setworldcoordinates(-200,-200,200,200)
#     koda = turtle.Turtle()
#     koda.color(""deep sky blue")
#     koda.pencolor("hot pink")
#     koda.pensize(3)
#     koda.speed(10)
#
#     startDrawing(koda)
#
#     wn.exitonclick()
# if __name__ == '__main__':
#     main()

# Question 3
# Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle draw a regular polygon.
# When called with drawPoly(tess, 8, 50), it will draw a shape like this


# import turtle
#
# def drawPoly(n, sides, size):
#     for i in range(sides):
#         n.fd(size)
#         s = 360//sides
#         n.lt(s)
#
# def startDrawing(n, wn):
#     sides = int(input("How many sides will the polygon have?"))
#     size = int(input("How long should the sides of the polygon be?"))
#     drawPoly(n, sides, size)
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     niko = turtle.Turtle()
#     niko.color("deep sky blue")
#     niko.pencolor("hot pink")
#     niko.pensize(3)
#     niko.speed(10)
#
#     startDrawing(niko,wn)
#
#
#     wn.exitonclick()
# if __name__ == '__main__':
#     main()

# Question 4
# Draw the spiral square pattern.

# import turtle
#
# def drawSquare(n, lenth, turn):
#     for i in range(4):
#         n.fd(lenth)
#         n.lt(turn)
#
# def mainPic(n):
#     size = 100
#     degrees = 90
#     for i in range(5):
#         drawSquare(n, size, degrees)
#         n.lt(180)
#         drawSquare(n, size, degrees)
#         degrees = degrees * -1
#         drawSquare(n, size, degrees)
#         n.lt(180)
#         drawSquare(n, size, degrees)
#         multiSquare = 360/5
#         n.lt(multiSquare)
#
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     norb = turtle.Turtle()
#     norb.color("orange")
#     norb.pencolor("blue")
#     norb.shape("turtle")
#     norb.pensize(3)
#     norb.speed(15)
#
#     mainPic(norb)
#     norb.hideturtle()
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 5
# The two square spirals differ only by the turn angle. Draw both.

# import turtle
#
# def sqrSpiral(k):
#     fwd = 1
#     for i in range(90):
#         k.rt(90)
#         k.fd(fwd)
#         fwd = fwd + 2
#     k.rt(90)
#     k.fd(fwd)
#
# def alt_sqrSpiral(h):
#     fwd = 1
#     for i in range(90):
#         h.rt(89)
#         h.fd(fwd)
#         fwd = fwd + 2
#     h.rt(90)
#
# def mainPic(k,h):
#     k.pu()
#     k.goto(-150,0)
#     k.pd()
#     h.pu()
#     h.goto(150,0)
#     h.pd()
#     sqrSpiral(k), alt_sqrSpiral(h)
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-300,-300,300,300)
#     wn.bgcolor("light green")
#     koda = turtle.Turtle()
#     koda.color("Saddle Brown")
#     koda.pencolor("blue")
#     koda.shape("turtle")
#     koda.pensize(3)
#     koda.speed(15)
#     honey = turtle.Turtle()
#     honey.color("Chocolate")
#     honey.pencolor("blue")
#     honey.shape("turtle")
#     honey.pensize(3)
#     honey.speed(15)
#
#
#     mainPic(koda, honey)
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 6
# Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly from the previous
# question to have its turtle draw a equilateral triangle

# import turtle
#
# def drawPoly(h, sides, size):
#     for i in range(sides):
#         h.fd(size)
#         s = 360//sides
#         h.lt(s)
#
# def drawEquitriangel(h,sides, size):
#     drawPoly(h, sides, size)
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     honey = turtle.Turtle()
#     honey.shape("turtle")
#     honey.color("chocolate")
#     honey.pencolor("hot pink")
#     honey.pensize(3)
#     honey.speed(10)
#     size = int(input("How long should the sides of the equilateral triangle be?"))
#     sides = 3
#     drawEquitriangel(honey,sides, size)
#
#
#     wn.exitonclick()
# if __name__ == '__main__':
#     main()

# Question 7
# Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n.
# So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.
#
#
# def sumTo(n):
#     answer = (n * (n + 1))/2
#     return (answer)
# def main():
#     integer_sum = int(input("What is the number that you would like to know the sum of all the integers?"))
#     print(sumTo(integer_sum))
#
# if __name__ == '__main__':
#     main()

# Question 8
# Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

# import math
#
# def areaOfCircle(r):
#     answer = math.pi*r**2
#     return (answer)
#
# def main():
#     radius = int(input("What is the radius of the circle?"))
#     print("Based on the radius (",radius,")the area of the circle is",areaOfCircle(radius))
#
# if __name__ == '__main__':
#     main()

# Question 9
# Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.

import turtle

# def drawStar(n, size, sides):
#     for i in range(sides):
#         n.fd(size)
#         points = 720 // sides
#         n.rt(points)
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     niko = turtle.Turtle()
#     niko.shape("turtle")
#     niko.color("deep sky blue")
#     niko.pensize(3)
#     niko.pencolor("black")
#
#     sides = int(input("How many points do you want the star to be?"))
#     size = int(input("How long should each side of the star be?"))
#
#     drawStar(niko, size, sides)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 10
# Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units,
# turn right by 144, put the pen down, and draw the next star. You’ll get something like this (note that you will
# need to move to the left before drawing your first star in order to fit everything in the window):

# import turtle
#
# def drawStar(n, size, sides):
#     for i in range(sides):
#         n.fd(size)
#         points = 720 // sides
#         n.rt(points)
#
# def draw5Star(n, size, sides):
#     n.pu()
#     n.goto(-150, 50)
#     n.pd()
#     for i in range(5):
#         drawStar(n, size, sides)
#         n.pu()
#         n.fd(300)
#         n.rt(720 // 5)
#         n.pd()
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     norb = turtle.Turtle()
#     norb.shape("turtle")
#     norb.color("orange")
#     norb.pensize(2)
#     norb.pencolor("hot pink")
#     norb.speed(15)
#
#     sides = 5
#     size = 100
#
#     draw5Star(norb, size, sides)
#
#     norb.pu()
#     norb.home()
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 11
# Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3).

# import turtle
#
# def drawStar(n, size, sides):
#     degreeFactor = 720 + (((sides - 5) / 2) * 360)
#     for i in range(sides):
#         n.fd(size)
#         turnSide = degreeFactor / sides
#         n.lt(turnSide)
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     norb = turtle.Turtle()
#     norb.shape("turtle")
#     norb.color("orange")
#     norb.pensize(2)
#     norb.pencolor("hot pink")
#     norb.speed(15)
#
#     points = int(input("How many points should the star have (odd numbers)?"))
#     length = int(input("What should the length of each point be?"))
#
#     drawStar(norb, length, points)
#
#     norb.pu()
#     norb.home()
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()


# Question 12
# Write a function called drawSprite that will draw a sprite. The function will need parameters for the turtle,
# the number of legs, and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120.

# import turtle
#
# def drawSprite(k, legs, length):
#     for i in range(legs):
#             k.fd(length)
#             k.dot(20)
#             k.bk(length)
#             k.dot(20)
#             k.rt(360//legs)
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     koda = turtle.Turtle()
#     koda.shape("turtle")
#     koda.color("Saddle Brown")
#     koda.pensize(2)
#     koda.speed(15)
#
#     sprite_legs = 15
#     sprite_length = 120
#
#     drawSprite(koda, sprite_legs, sprite_length)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 13
# Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n.
# This time use the accumulator pattern.

# def sumTo(n):
#     answer = 0
#     for i in range(1, n+1):
#         answer = answer + i
#     return (answer)
#
# def main():
#
#     number = int(input("Provide a number to see the sum of all its integers."))
#
#     print(sumTo(number))
#
# if __name__ == '__main__':
#     main()

# Question 14
# Write a function called mySqrt that will approximate the square root of a number, call it n, by using
# Newton’s algorithm. Newton’s approach is an iterative guessing algorithm where the initial guess is n/2 and
# each subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess)).

# def mySqrt(n):
#     oldguess = n/2
#     oldguess = (1 / 2) * (oldguess + (n / oldguess))
#     oldguess = (1 / 2) * (oldguess + (n / oldguess))
#     newguess = (1 / 2) * (oldguess + (n / oldguess))
#     newguess = int(newguess)
#     return newguess
#
# def main():
#     number = int(input("Provide a non-prime number to determine its square root."))
#
#     print(mySqrt(number))
#
# if __name__ == '__main__':
#     main()

# Question 15
# Write a function called myPi that will return an approximation of PI (3.14159...). Use the Leibniz approximation.

# def myPi(iters):
#     pi = 0
#     sign = 1
#     denominator = 1
#     for i in range(iters):
#         pi = pi + (sign/denominator)
#         sign = sign * -1
#         denominator = denominator + 2
#     pi = pi * 4
#     return pi
#
# def main():
#     print(myPi(1000))
#
# if __name__ == '__main__':
#     main()

# Question 16 (SKIPPED)

# Question 17
# Write a function called fancySquare that will draw a square with fancy corners (sprites on the corners).
# You should implement and use the drawSprite function from above. For an even more interesting look,
# how about adding small triangles to the ends of the sprite legs.

# import turtle
#
# def fancySquare(h):
#     h.pu()
#     h.goto(-75,-75)
#     h.pd()
#     for i in range(4):
#         h.fd(150)
#         h.lt(45)
#         for i in ("red","blue","green","hot pink", "purple"):
#             h.pencolor(i)
#             h.fd(25)
#             h.dot(10)
#             h.bk(25)
#             h.rt(36)
#         h.pencolor("chocolate")
#         h.lt(225)
#     h.pu()
#     h.home()
#     h.lt(360)
#
# def main():
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200,-200,200,200)
#     wn.bgcolor("light green")
#     honey = turtle.Turtle()
#     honey.shape("turtle")
#     honey.color("chocolate")
#     honey.pensize(2)
#     honey.speed(5)
#
#     fancySquare(honey)
#     wn.exitonclick()
#
#
# if __name__ == '__main__':
#     main()