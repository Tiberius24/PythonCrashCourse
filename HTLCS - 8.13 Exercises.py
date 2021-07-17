# HTLCS 8.13 Exercises
# My name: Don Trapp

# Problem 1
# Add a print statement to Newton’s sqrt function that prints out better each time it is calculated.
# Call your modified function with 25 as an argument and record the results.

# def newtonSqrt(n, howmany):
#     approx = 0.5 * n
#     tapprox = 0
#     while approx != tapprox:
#         betterapprox = 0.5 * (approx + n/approx)
#         print(betterapprox)
#         tapprox = approx
#         approx = betterapprox
#     return betterapprox
#
# print("Answer", newtonSqrt(25, 10))


# BETTER ANSWER IN MY OPINION

# def newtonSqrt(n, howmany):
#     approx = 0.5 * n
#     for i in range(howmany):
#         betterapprox = 0.5 * (approx + n/approx)
#         if betterapprox == approx:
#             break
#         else:
#             print(betterapprox)
#             approx = betterapprox
#     return betterapprox
#
# print("Answer", newtonSqrt(25, 10))

# Problem 2
# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
# A call to print_triangular_numbers(5) would produce the following output:

# import turtle
#
# def nextRow(h,i):
#     for j in range(i):
#         h.fd(10)
#         h.dot(5)
#     for k in range(i):
#         h.bk(10)
#
# def drawDotTriangle(h, n):
#     h.lt(90)
#     for i in range(n):
#         if i > 0:
#             h.rt(90)
#             h.fd(10)
#             h.lt(90)
#             h.dot(5)
#             nextRow(h, i)
#         else:
#             h.dot(5)
#     h.rt(90)
#     h.fd(20)
#
# def print_triangular_number(n, h):
#     for i in range(1, (n+1)):
#         answer = i*(i+1)/2
#         answer = int(answer)
#         drawDotTriangle(h, i)
#         print(answer)
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#
#     honey = turtle.Turtle()
#     honey.shape("turtle")
#     honey.color("chocolate")
#     honey.speed(20)
#     honey.pencolor("black")
#     honey.pu()
#     honey.goto(-195,0)
#
#     print_triangular_number(10, honey)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Problem 3
# Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime number
# and False otherwise.

# import math
#
# def is_prime(n):
#     for i in range(2,n):
#         value = n % i
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(3))

# Problem 4
# Modify the walking turtle program so that rather than a 90 degree left or right turn the angle of the turn
# is determined randomly at each step.

# import turtle
# import random
#
# def turtleWalk(n):
#     x_cor = int(n.xcor())
#     y_cor = int(n.ycor())
#
#     while (x_cor < 199) and (x_cor > -199) and (y_cor < 199) and (y_cor > -199):
#         coin = random.randrange(0, 2)
#         turn = random.randrange(15, 91, 15)
#         if coin == 0:
#             n.lt(turn)
#         else:
#             n.rt(turn)
#         n.fd(50)
#         n.dot()
#         x_cor = int(n.xcor())
#         y_cor = int(n.ycor())
#
#
# def main():
#
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200, -200, 200, 200)
#     wn.bgcolor("light green")
#
#     niko = turtle.Turtle()
#     niko.color("deep sky blue")
#     niko.shape("turtle")
#     niko.speed(10)
#     niko.pu()
#
#     turtleWalk(niko)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Problem 5
# Modify the turtle walk program so that you have two turtles each with a random starting location.
# Keep the turtles moving until one of them leaves the screen.

# import turtle
# import random
#
# def dualTurtle(n, h):
#     nx_cord = random.randrange(-100,100,1)
#     ny_cord = random.randrange(-100,100,1)
#     n.goto(nx_cord, ny_cord)
#
#     hx_cord = random.randrange(-100,100,1)
#     hy_cord = random.randrange(-100,100,1)
#     h.goto(hx_cord, hy_cord)
#
#     turtleWalk(n, h)
#
# def turtleWalk(n, h):
#     nx_cor = int(n.xcor())
#     ny_cor = int(n.ycor())
#     hx_cor = int(h.xcor())
#     hy_cor = int(h.ycor())
#     while ((nx_cor < 199) and (nx_cor > -199) and (ny_cor < 199) and (ny_cor > -199)) and \
#             ((hx_cor < 199) and (hx_cor > -199) and (hy_cor < 199) and (hy_cor > -199)):
#         coin = random.randrange(0, 2)
#         turn = random.randrange(15, 91, 15)
#         if coin == 0:
#             n.lt(turn)
#         else:
#             n.rt(turn)
#         coin = random.randrange(0, 2)
#         turn = random.randrange(15, 91, 15)
#         if coin == 0:
#             h.lt(turn)
#         else:
#             h.rt(turn)
#         n.fd(50)
#         h.fd(50)
#         n.dot()
#         h.dot()
#         nx_cor = int(n.xcor())
#         ny_cor = int(n.ycor())
#         hx_cor = int(h.xcor())
#         hy_cor = int(h.ycor())
#
#
# def main():
#
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200, -200, 200, 200)
#     wn.bgcolor("light green")
#
#     niko = turtle.Turtle()
#     niko.color("deep sky blue")
#     niko.shape("turtle")
#     niko.speed(10)
#     niko.pu()
#
#     honey = turtle.Turtle()
#     honey.color("chocolate")
#     honey.shape("turtle")
#     honey.speed(10)
#     honey.pu()
#
#     dualTurtle(niko, honey)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Problem 6
# Modify the previous turtle walk program so that the turtle turns around when it hits the wall or
# when one turtle collides with another turtle

# import turtle
# import random
#
# def dualTurtle(n, h):
#     nx_cord = random.randrange(-50,50,1)
#     ny_cord = random.randrange(-50,50,1)
#     n.goto(nx_cord, ny_cord)
#
#     hx_cord = random.randrange(-50,50,1)
#     hy_cord = random.randrange(-50,50,1)
#     h.goto(hx_cord, hy_cord)
#
#     turtleWalk(n, h)
#
# def perimeter_check (t):
#     tx = int(t.xcor())
#     ty = int(t.ycor())
#     if (tx > 199) or (tx < -199) or (ty > 199) or (ty < -199):
#         t.bk(75)
#
# def turtleWalk(n, h):
#     nx_cor = int(n.xcor())
#     ny_cor = int(n.ycor())
#     hx_cor = int(h.xcor())
#     hy_cor = int(h.ycor())
#     while ((nx_cor < 199) and (nx_cor > -199) and (ny_cor < 199) and (ny_cor > -199)) and \
#             ((hx_cor < 199) and (hx_cor > -199) and (hy_cor < 199) and (hy_cor > -199)):
#         coin = random.randrange(0, 2)
#         turn = random.randrange(15, 91, 15)
#         if coin == 0:
#             n.lt(turn)
#         else:
#             n.rt(turn)
#         coin = random.randrange(0, 2)
#         turn = random.randrange(15, 91, 15)
#         if coin == 0:
#             h.lt(turn)
#         else:
#             h.rt(turn)
#         n.fd(50)
#         if n.distance(h) < 12:
#             n.bk(25)
#         h.fd(50)
#         if n.distance(h) < 12:
#             h.bk(25)
#         n.dot()
#         h.dot()
#
#         perimeter_check(n)
#         perimeter_check(h)
#
#         nx_cor = int(n.xcor())
#         ny_cor = int(n.ycor())
#         hx_cor = int(h.xcor())
#         hy_cor = int(h.ycor())
# def main():
#
#     wn = turtle.Screen()
#     wn.setworldcoordinates(-200, -200, 200, 200)
#     wn.bgcolor("light green")
#
#     niko = turtle.Turtle()
#     niko.color("deep sky blue")
#     niko.shape("turtle")
#     niko.speed(10)
#     niko.pu()
#
#     honey = turtle.Turtle()
#     honey.color("chocolate")
#     honey.shape("turtle")
#     honey.speed(10)
#     honey.pu()
#
#     dualTurtle(niko, honey)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()