# HTLCS 2.13 Exercises
# My Name: Don Trapp

# Question 1
# Evaluate the following numerical expressions in your head, then use the active code window to check your results:

# print(5** 2)
# print(9 * 5)
# print(15 / 12)
# print(12 / 15)
# print(15 // 12)
# print(12 // 15)
# print(5 % 2)
# print(9 % 5)
# print(15 % 12)
# print(12 % 15)
# print(6 % 6)
# print(0 % 7)

# Question 2
# What is the order of the arithmetic operations in the following expression. Evaluate the expression by hand and
# then check your work.

# x = 2 + (3 - 1) * 10 / 5 * (2 + 3)
# print(x)

# Question 3
# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you
# set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the
# above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off.

# x = int(input("What is the current time in military time?"))
# y = int(input("How many hours do you want to wait before the alarm goes off?"))
# total_time = x + y
# time = total_time % 24
# print("Your alarm will go off at ",time," hundred hours.")

# Question 4
# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful
# holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights. Write a general version of
# the program which asks for the starting day number, and the length of your stay, and it will tell you the number of
# day of the week you will return on.

# starting_day =  int(input("Which day will your vacation begin? (number)"))
# stay_length = int(input("How many days will you be gone for?"))
# total_vacation = starting_day + stay_length
# return_date = total_vacation % 6
# if return_date == 0:
#     return_date = "Sunday"
# elif return_date == 1:
#     return_date = "Monday"
# elif return_date == 2:
#     return_date = "Tuesday"
# elif return_date == 3:
#     return_date = "Wednesday"
# elif return_date == 4:
#     return_date = "Thursday"
# elif return_date == 5:
#     return_date = "Friday"
# elif return_date == 6:
#     return_date = "Saturday"
# print(return_date)

# Question 5
# Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out
# the sentence on one line using print.

# a = "All"
# b = "work"
# c = "and"
# d = "no"
# e = "play"
# f = "makes"
# g = "Jack"
# h = "a"
# i = "dull"
# j = "boy."
#
# print(a,b,c,d,e,f,g,h,i,j)

# Question 6
# Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

# answer = 6 * (1 -2)
# print(answer)

# Question 7
# The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
# formula for compound interest. A = P (1+r/n)**n*t Write a Python program that assigns the principal amount of 10000
# to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt
# the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount
# after t years.

# p = 10000
# n = 12
# r = .08
# t = int(input("How many years will do you want to invest your money for?"))
#
# a = int(p * (1+r/n)**(n*t))
#
# print("If you invest your",p,"dollars for",t,"years it will be worth",a,"dollars")

# Question 8
# Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message
# back to the user with the answer. A =πr2

# pi = 3.14159265359
# r = int(input("What is the radius of the cicle?"))
# area = pi * r ** 2
#
# print("With a radius of",r,"the area of the circile is",area)

# Question 9
# Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the
# rectangle. Print a nice message with the answer. Width * Length

# w = int(input("What is the width of the rectangel in inches?"))
# l = int(input("What is the length of the rectangel in inches?"))
#
# area = w*l
# print("With a width of",w,"inches and a length of",l,"inches the rectangles area is",area,"inches.")

# Question 10
# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number
# of gallons used. Print a nice message with the answer.

# miles = int(input("How many miles did you drive?"))
# gallon = int(input("How many gallons did you use?"))
#
# mpg = miles / gallon
#
# print("You car averaged",mpg,"miles per gallon.")

# Question 11
# Write a program that will convert degrees celsius to degrees fahrenheit. T = C * 1.8 + 32

# c = int(input("What is the current temperature in celcius?"))
#
# f = int(c * 1.8 + 32)
#
# print("If it is",c,"degrees celcius then it is",f,"degrees fahrenheit.")

# Question 12
# Write a program that will convert degrees fahrenheit to degrees celsius. T = (F - 32) / 1.8

# f = int(input("What is the current temperature in fahrenheit?"))
#
# c = int((f-32)/1.8)
#
# print("If it is",f,"degress fahrenheit then it is",c,"degrees celsius.")





