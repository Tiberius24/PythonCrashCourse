# HTLCS 7.10 Exercises
# My name: Don Trapp

# Question 1
# What do the following boolean expressions evaluate to?

# print(3 == 3)
# print(3 != 3)
# print(3 >= 4)
# print(not 3 >= 4)

# Question 2
# Give the logical opposites of these conditions. You are not allowed to use the not operator.

# day = 4
#
# print(3 < 4)
# print(3 <= 4)
# print(3 <= 18 or day != 3)
# print(3 <= 18 and day == 3)

# Question 3
# Write a function which is given an exam mark, and it returns a string — the grade for that mark —
# according to this scheme

# def getGrade(s):
#     if s >= 90:
#         letter = "A"
#     elif s >= 80 and s < 90:
#         letter = "B"
#     elif s >= 70 and s < 80:
#         letter = "C"
#     elif s >= 60 and s < 70:
#         letter = "D"
#     else:
#         letter = "F"
#     return letter
#
# def determineScore (correct, tot):
#     score  = (correct / tot) * 100
#     return getGrade(score)
#
# def main():
#     totQuestions = int(input("How many total questions where there on the assignment?"))
#     totCorrect = int(input("How many answers did the student answer correctly?"))
#
#     print("The students letter grade for the assigment is:",determineScore(totCorrect, totQuestions))
#
# if __name__ == '__main__':
#     main()

# Question 4
# Modify the turtle bar chart program from the previous chapter so that the bar for any value of 200 or more
# is filled with red, values between [100 and 200) are filled yellow, and bars representing values less than 100
# are filled green.

# import turtle
#
# def printNumber(t, height):
#     x = t.xcor()
#     y = t.ycor()+2
#     t.penup()
#     t.goto(x,y)
#     t.pencolor("black")
#     t.write(height, align="center" ,font=("Arial", 10))
#     x = t.xcor()
#     y = t.ycor() - 2
#     t.goto(x, y)
#     t.pendown()
#
# def drawBar(t, height):
#     if height > 200:
#         t.fillcolor("red")
#     elif height <= 200 and height >=100:
#         t.fillcolor("yellow")
#     else:
#         t.fillcolor("green")
#     t.begin_fill()
#     t.lt(90)
#     t.fd(height)  # height of the bar graph
#     t.rt(90)
#     t.fd(20)  # Width of the bar graph
#     printNumber(t, height)
#     t.fd(20)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#     t.fd(5)  # Setup the turtle to start the next bar
#
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     xs = [48, 117, 200, 240, 160, 260, 220]
#     maxheight = max(xs)
#     numbars = len(xs)
#     border = 10
#     wn.setworldcoordinates(0-border, 0-border, 45*numbars+border, maxheight+border)
#     niko = turtle.Turtle()
#     niko.color("deep sky blue")
#     niko.pencolor("navy")
#     niko.pensize(3)
#     niko.speed(10)
#
#     for v in xs:  # 4 loop to draw the graph based off the number of entries
#         drawBar(niko, v)
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 5
# In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list
# is negative? Go back and try it out. Change the program so that when it prints the text value for the negative bars,
# it puts the text above the base of the bar (on the 0 axis).

# import turtle
#
# def printNumber(t, height):
#     x = t.xcor()
#     y = t.ycor()+2
#     t.penup()
#     if height < 0:
#         oldX_Cord = t.xcor()
#         oldY_Cord = t.ycor()
#         t.goto(oldX_Cord,2)
#     else:
#         t.goto(x, y)
#     t.pencolor("black")
#     t.write(height, align="center" ,font=("Arial", 10))
#     x = t.xcor()
#     y = t.ycor() - 2
#     if height < 0:
#         t.goto(oldX_Cord, oldY_Cord)
#     else:
#         t.goto(x, y)
#     t.pendown()
#
# def drawBar(t, height):
#     if height > 200:
#         t.fillcolor("red")
#     elif height <= 200 and height >=100:
#         t.fillcolor("yellow")
#     else:
#         t.fillcolor("green")
#     t.begin_fill()
#     t.lt(90)
#     t.fd(height)  # height of the bar graph
#     t.rt(90)
#     t.fd(20)  # Width of the bar graph
#     printNumber(t, height)
#     t.fd(20)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#     t.fd(5)  # Setup the turtle to start the next bar
#
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     xs = [48, 117, 200, 240, -160, 260, 220]
#     maxheight = max(xs)
#     minheight = -160
#     numbars = len(xs)
#     border = 10
#     wn.setworldcoordinates(0 + border, minheight + border, 45*numbars + border, maxheight + border)
#     niko = turtle.Turtle()
#     niko.color("deep sky blue")
#     niko.pencolor("navy")
#     niko.pensize(3)
#     niko.speed(10)
#
#     for v in xs:  # 4 loop to draw the graph based off the number of entries
#         drawBar(niko, v)
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 6
# Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and
# it should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from
# the math module)

# import math
#
# def findHypot(a, b):
#     c = math.sqrt((a ** 2) + (b ** 2))
#     return c
#
# def main():
#     side_A = int(input("What is the length of side A?"))
#     side_B = int(input("What is the length of side B?"))
#
#     print("Give the length of A",side_A,"and the lenth of side B",side_B,"the hypotenuse function determine the length"
#           "side C to be",findHypot(side_A, side_B))
#
# if __name__ == '__main__':
#     main()

# Question 7
# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument
# is an even number and False if it is odd.

# def is_even(n):
#     answer = n % 2
#     answer = answer == 0
#     return answer
#
# def main():
#     number = int(input("Please provide a number to determine if it is even or odd?"))
#
#     print("True or False: The following number is even:",number,is_even(number))
#
# if __name__ == '__main__':
#     main()

# Question 8
# Now write the function is_odd(n) that returns True when n is odd and False otherwise.

# def is_odd(n):
#     answer = n % 2 != 0
#     return answer
#
# def main():
#     number = int(input("Please provide a number to determine if it is even or odd?"))
#
#     print("True or False: The following number is odd:",number,is_odd(number))
#
# if __name__ == '__main__':
#     main()


# Question 9
# Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.

# def is_even(n):
#     answer = n % 2 == 0
#     return answer
#
# def is_odd(n):
#     if is_even(n):
#         return False
#     else:
#         return True
#
# def main():
#     number = int(input("Please provide a number to determine if it is even or odd?"))
#
#     print("True or False: The following number is odd:",number,is_odd(number))
#
# if __name__ == '__main__':
#     main()

# Question 10
# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether
# the triangle is right-angled. Assume that the third argument to the function is always the longest side.
# It will return True if the triangle is right-angled, or False otherwise.Hint: floating point arithmetic is not
# always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to
# know whether x is equal or close enough to y, they would probably code it up as

# def is_rightangled(a, b, c):
#     answer1 = (c ** 2)
#     answer2 = ((a ** 2) + (b ** 2))
#     if answer1 - answer2 < 0.001:
#         return True
#     else:
#         return False
#
#
# def main():
#     side_A = int(input("What is the length of side A of the triangle?"))
#     side_B = int(input("What is the length of side B of the triangle?"))
#     side_C = int(input("What is the length of side C of the triangle?"))
#
#     print(is_rightangled(side_A, side_B, side_C))
#
# if __name__ == '__main__':
#     main()

# Question 11
# Extend the above program so that the sides can be given to the function in any order.

# def is_rightangled(a, b, c):
#     if  a > b and a > c:
#         if a ** 2 - (c ** 2 + b ** 2) < 0.001:
#             return True
#         else:
#             return False
#     elif b > a and b > c:
#         if b ** 2 - (a ** 2 + c ** 2) < 0.001:
#             return True
#         else:
#             return False
#     else:
#         if c ** 2 - (a ** 2 + b ** 2) < 0.001:
#             return True
#         else:
#             return False
#
#
# def main():
#     side_A = float(input("What is the length of side A of the triangle?"))
#     side_B = float(input("What is the length of side B of the triangle?"))
#     side_C = float(input("What is the length of side C of the triangle?"))
#
#     print(is_rightangled(side_A, side_B, side_C))
#
# if __name__ == '__main__':
#     main()

# Question 12
# 3 criteria must be taken into account to identify leap years:
# The year is evenly divisible by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
# Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.

# def isLeap(y):
#     if y % 100 == 0 and y % 400 == 0:
#         return True
#     elif y % 4 == 0 and y % 100 == 0:
#         return False
#     elif y % 4 == 0:
#         return True
#     else:
#         return False
#
# def main():
#     year = int(input("What year do you want to determine if it is a leap year?"))
#
#     print("True or False: The year",year,"is a leap year.", isLeap(year))
#
# if __name__ == '__main__':
#     main()

# Question 13
# Implement the calculator for the date of Easter.
# The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.
# Ask the user to enter a year. Compute the following:
#
# a = year % 19
# b = year % 4
# c = year % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d + 5) % 7
# dateofeaster = 22 + d + e
#
# Special note: The algorithm can give a date in April. Also, if the year is one of four special years
# (1954, 1981, 2049, or 2076) then subtract 7 from the date.
# Your program should print an error message if the user provides a date that is out of range.

# def calcEaster(y):
#
#     a = y % 19
#     b = y % 4
#     c = y % 7
#     d = (19 * a + 24) % 30
#     e = (2 * b + 4 * c + 6 * d + 5) % 7
#     dateofeaster = 22 + d + e
#
#     if y == 1954 or y == 1981 or y == 2049 or y == 2076:
#         dateofeaster= dateofeaster - 7
#
#     return dateofeaster
#
# def main():
#
#     year = int(input("Which year do you want to know the date of Easter for?"))
#     Easter = calcEaster(year)
#     if Easter > 31:
#         print("April", Easter - 31)
#     else:
#         print("March", Easter)
#
# if __name__ == '__main__':
#     main()
