# HTLCS 5.6 Exercises
# My name: Don Trapp

# Question 1
# Use a for statement to print 10 random numbers.

# import random
#
# for i in range(1, 11):
#     print(random.randrange(1,11))
#
# # Question 2
# # Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.
#
# import random
#
# for i in range(10):
#     print(random.randrange(25,36))

# Question 3
# The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of
# the other two sides. Look through the math module and see if you can find a function that will compute this
# relationship for you. Once you find it, write a short program to try it out.

# import math
#
# a = int(input("What is the length of the first angle?"))
# b = int(input("What is the length of the second angele?"))
#
# answer = math.hypot(a, b)
# print("If the length of angle a is",a,"and the length of angle b is",b
# ,"then the lenght of angle c is the square root which is",answer)

# Question 4
# Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic.
# Write a program to compute the approximation and then print that value as well as the value of math.pi from the
# math module.

import math

my_pi = 22/7

math_pi = math.pi

print("This is my pi",my_pi)
print("This is the math modules pi",math_pi)



