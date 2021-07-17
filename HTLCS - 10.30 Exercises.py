# HTLCS 10.30 Exercises
# My name: Don Trapp

# Question 15
# Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76. Do it with both append
# and with concatenation, one item at a time.

# myList = []
# myList.append(76)
# myList.append(92.3)
# myList = myList + ["hello"]
# myList = myList + [True]
# myList.append(4)
# myList.append(76)
# print(myList)


# Question 16
# Use the list function index to determine where "hello" is within myList.
# Use the list function count to determine how many iterations of 76 are in myList.
# Use the remove function to remove 76 from myList.
# Use the pop function to remove True entry from myList. Save it as a variable and print it along with myList.

# myList = []
# myList.append(76)
# myList.append(92.3)
# myList = myList + ["hello"]
# myList = myList + [True]
# myList.append(4)
# myList.append(76)
#
# i_myList = myList.index("hello")
# print(i_myList)
# c_myList = myList.count(76)
# print(c_myList)
# myList.remove(76)
# print(myList)
# p_myList = myList.pop(myList.index(True))
# print(p_myList)
# print(myList)

# Question 17
# Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
# Write a function called average that will take the list as a parameter and return the average.
#
# import random
#
# def listAverage(rI):
#     total = 0
#     average = 0
#     for i in rI:
#         total = total + i
#     average = total / len(rI)
#     return average
# def main():
#     radInt = []
#     for i in range(100):
#         radNum = random.randrange(0, 10000)
#         radInt.append(radNum)
#
#     print(listAverage(radInt))
#
# if __name__ == '__main__':
#     main()

# Problem 18
# Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the
# maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)

# import random
#
# def maxList(rI):
#     maximum = 0
#     for i in rI:
#         if i > maximum:
#             maximum = i
#     return maximum
#
# def main():
#     radInt = []
#     for i in range(100):
#         radNum = random.randrange(0, 10000)
#         radInt.append(radNum)
#
#     print(maxList(radInt))
#
# if __name__ == '__main__':
#     main()

# Question 19
# Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs.
# For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:

# import random
#
# def sum_of_squares(xs):
#     answer = 0
#     square_list = []
#     for i in xs:
#         square_list.append(i ** 2)
#         answer = (i ** 2) + answer
#     print(square_list)
#     return answer
#
# def main():
#     orig_list = []
#     for i in range(10):
#         orig_list.append(random.randint(1, 20))
#     print(orig_list)
#     print(sum_of_squares(orig_list))
#
# if __name__ == '__main__':
#     main()

# Question 20
# Write a function to count how many odd numbers are in a list.

# import random
#
# def countOdd(lst):
#     answer = 0
#     for i in lst:
#         if i % 2 == 1:
#             answer = answer + 1
#     # print(answer)
#     return answer
#
# def main():
#     orig_list = [1, 3, 5, 7, 9]
#     # for i in range(20):
#     #     orig_list.append(random.randint(1, 100))
#     # print(orig_list)
#     odd_list = countOdd(orig_list)
# #   answer = odd_list.__len__()
#     print(odd_list)
#
# if __name__ == '__main__':
#     main()


# Problem 21
# Sum up all the even numbers in a list.

# import random
#
# def sumEven(lst):
#     answer = 0
#     for i in lst:
#         if i % 2 == 0:
#             answer = answer + i
#     # print(answer)
#     return answer
#
# def main():
#     orig_list = [-1, -2, -3, -4, -5]
#     # for i in range(20):
#     #     orig_list.append(random.randint(1, 100))
#     print(orig_list)
#     answer = sumEven(orig_list)
#     # answer = even_list.__len__()
#     print(answer)
#
# if __name__ == '__main__':
#     main()

# Problem 22
# Sum up all the negative numbers in a list.

# import random
#
# def sumNegatives(lst):
#     answer = 0
#     for i in lst:
#         if i < 0:
#             answer = answer + i
#     return answer
#
# def main():
#     orig_list = []
#     for i in range(20):
#         orig_list.append(random.randint(-50, 50))
#     # print(orig_list)
#     answer = sumNegatives(orig_list)
#     print(answer)
#
# if __name__ == '__main__':
#     main()

# Problem 23
# Count how many words in a list have length 5.

# def countWords(lst):
#     answer = 0
#     l_word = 0
#     for i in range(len(lst)):
#         l_word = len(lst[i])
#         if l_word >= 5:
#             answer = answer + 1
#         else:
#             continue
#     return answer
#
# def main():
#
#     orig_list = ['Four', 'ago', 'on', 'nation', 'the', 'are', 'are', 'civil', 'testing', 'any', 'so', 'We', 'great',
#                  'of', 'come', 'of', 'final', 'who', 'gave', 'nation', 'altogether', 'we', 'larger', 'dedicate',
#                  'consecrate', 'hallow', 'living', 'here', 'above', 'add', 'note', 'we', 'can', 'did', 'It', 'living',
#                  'here', 'which', 'have', 'is', 'be', 'great', 'take', 'cause', 'the', 'devotion', 'that', 'that',
#                  'have', 'that', 'a', 'of', 'people', 'from']
#
#     print(countWords(orig_list))
#
# if __name__ == '__main__':
#     main()

# Problem 24
# Sum all the elements in a list up to but not including the first even number.

# import random
#
# def sumUntilEven(lst):
#     answer = 0
#     for i in lst:
#         if i % 2 != 0:
#             answer = answer + i
#         else:
#             break
#     return answer
#
# def main():
#     orig_list = []
#     for i in range(0,40):
#         orig_list.append(random.randint(0,100))
#
#     print(sumUntilEven(orig_list))
#
# if __name__ == '__main__':
#     main()

# Problem 25
# Count how many words occur in a list up to and including the first occurrence of the word “sam”.

# import random
#
# def count(lst):
#     answer = 0
#     for i in lst:
#         if i != "Sam":
#             answer = answer + 1
#         elif i == "Sam":
#             answer = answer + 1
#             break
#         else:
#             continue
#     return answer
#
# def main():
#         orig_list = ['Juliana','Debi','Lianne','Nigel','Ettie','Myrta','Ayana','Agatha','Harris','Monte','Chanell',
#                      'Liz','Marquitta','Antony','Tabitha','Ricky','Yasmine','Signe','Kanisha','Dorian','Julietta',
#                      'Jolie','Vertie','Jacklyn','Shiloh','Sharice','Kathrin','Angelyn','Serina','Kendal']
#         orig_list.insert(random.randint(0,31),"Sam")
#
#         print(count(orig_list))
#
# if __name__ == '__main__':
#     main()

# Problem 26
# Although Python provides us with many list methods, it is good practice and very instructive to think about how
# they are implemented. Implement a Python function that works like the following:
# count
# in
# reverse
# index
# insert

# def count(value, lst):
#     answer = 0
#     for i in lst:
#         if i == value:
#             answer = answer + 1
#     return answer
#
# def is_in(value, lst):
#     for i in lst:
#         if i == value:
#             return True
#         else:
#             continue
#     return False
#
# def reverse(lst):
#     rev_lst = []
#     for i in range(-1, len(lst) * -1, -1):
#         rev_lst.append(lst[i])
#     return rev_lst
#
# def index(value, lst):
#     answer = 0
#     for i in lst:
#         if answer == value:
#             return i
#         else:
#             answer = answer + 1
#             continue
#
#
# def insert(value, pos, lst):
#     new_lst = []
#     for i in range(len(lst)):
#         if i == pos:
#             new_lst.append(value)
#             new_lst.append(lst[i])
#         else:
#             new_lst.append(lst[i])
#     return new_lst
#
#
# def main():
#
#     lst = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(count(1, lst))
#     print(is_in(4, lst))
#     print(reverse(lst))
#     print(index(2, lst))
#     print(insert('cat', 4, lst))
#
# if __name__ == '__main__':
#     main()

# Problem 27
# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:

import string

# def replace(s, old, new):
#     new_word = ""
#     for i in s:
#         if i == old:
#             i = new
#             new_word = new_word + i
#         else:
#             new_word = new_word + i
#     return new_word
#
#
# def main():
#     s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
#     old = "om"
#     new = "am"
#
#     print(replace(s, old, new))
#
#
# if __name__ == '__main__':
#     main()


# import string
#
#
# def listGenrator(text):
#     letters = string.ascii_letters
#     punctuation = string.punctuation
#     container = ""
#     newList = []
#     for i in text:
#         if i in letters:
#             container = container + i
#         elif i == " ":
#             if container != "":
#                 newList.append(container)
#                 container = ""
#             else:
#                 continue
#         elif i in punctuation:
#             newList.append(container)
#             container = ""
#             newList.append(i)
#         else:
#             continue
#     if len(newList) == 0:
#         newList.append(container)
#     return newList
#
# def replace(s, old, new):
#     s = listGenrator(s)
#     new_phrase = ""
#     check = 0
#     punctuation = string.punctuation
#     # print(len(s))
#     for i in s:
#         if len(s) > 1:
#             check = check + 1
#         if old in i:
#             new_word = i.replace(old, new)
#             if s[check] in punctuation:
#                 new_phrase = new_phrase + new_word
#             elif len(s) == 1:
#                 new_phrase = new_phrase + new_word
#             else:
#                 new_phrase = new_phrase + new_word + " "
#         elif i in punctuation:
#             new_phrase = new_phrase + i + " "
#         else:
#             if s[check] in punctuation:
#                 new_phrase = new_phrase + i
#             else:
#                 new_phrase = new_phrase + i + " "
#
#     return new_phrase
#
# def main():
#     s = 'Mississippi'
#     old = "i"
#     new = "I"
#
#     print(replace(s, old, new))
#
#
# if __name__ == '__main__':
#     main()

