# HTLCS 9.22 Exercises
# My name: Don Trapp

# Problem 1
# What is the result of each of the following:

# print("Python"[1])
# print ('Strings are sequences of characters.'[5])
# print (len("wonderful"))
# print("Mystery"[:4])
# print("p" in "Pineapple")
# print('apple' in 'Pineapple')
# print('pear' not in 'Pineapple')
# print('apple' > 'pineapple')
# print('pineapple' < 'Peach')

# Problem 2
# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack,
# Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.

# prefixes = "JKLMNOPQ"
# suffix = "ack"
# suffix2 = "uack"
#
# for p in prefixes:
#     if p != 'O' and p != 'Q':
#         print(p + suffix)
#     else:
#         print(p + suffix2)

# Problem 3
# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text -
# perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then
# keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:

# import string
#
# def count(q):
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#
#     charCount = 0
#     eCount = 0
#     for i in q:
#         if i in lower or i in upper:
#             charCount = charCount + 1
#             if i == "e":
#                 eCount = eCount + 1
#     charPercent = int((eCount / charCount)*100)
#     print("This speech contains", charCount, "alphabetic characters, of which", eCount, "("+str(charPercent)
#           + "%) are 'e'.")
#
#
# def main():
#
#     quote = '''Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in
#     Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war,
#     testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great
#     battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who
#     here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
#     But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground.
#     The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract.
#     The world will little note, nor long remember what we say here, but it can never forget what they did here.
#     It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far
#     so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these
#     honored dead we take increased devotion to that cause for which they gave the last full measure of devotion --
#     that we here highly resolve that these dead shall not have died in vain -- that this nation, under God,
#     shall have a new birth of freedom -- and that government  of the people, by the people, for the people,
#     shall not perish from the earth.
#
#     Abraham Lincoln
#     November 19, 1863'''
#
#     count(quote)
# if __name__ == '__main__':
#     main()

# Problem 4
# Print out a neatly formatted multiplication table, up to 12 x 12.

# print("n", '\t', "n*1", '\t', "n*2", '\t', "n*3", '\t', "n*4", '\t', "n*5", '\t', "n*6", '\t', "n*7", '\t', "n*8", '\t',
#       "n*9", '\t', "n*10", '\t', "n*11", '\t', "n*12")     # table column headings
# print("--", '\t', "----", '\t', "----", '\t', "----", '\t', "----", '\t', "----", '\t', "----", '\t', "----", '\t',
#       "----", '\t', "----", '\t', "----", '\t', "----", '\t', "----",)
#
# for x in range(13):        # generate values for columns
#     print(x, '\t', 1 * x, '\t', 2 * x, '\t', 3 * x, '\t', 4 * x, '\t', 5 * x, '\t', 6 * x, '\t', 7 * x, '\t', 8 * x,
#           '\t', 9 * x, '\t', 10 * x, '\t', 11 * x, '\t', 12 * x)

# Problem 5
# Write a function that will return the number of digits in an integer.

# def numDigits(n):
#     answer = len(str(n))
#     return answer
#
# print(numDigits(123456789))

# Problem 6
# Write a function that reverses its string argument.

# def reverse(astring):
#     variable = ""
#     for i in astring:
#         variable = i + variable
#     return variable
#
# print(reverse("Johnny Apple Seed"))

# Problem 7
# Write a function that mirrors its argument.


# def reverse(astring):
#     variable = ""
#     for i in astring:
#         variable = i + variable
#     return variable
#
# def mirror(mystr):
#     reflection = reverse(mystr)
#     if mystr == reverse(reflection):
#         answer = (mystr+reflection)
#     else:
#         False
#     return answer
#
# print(mirror("apple"))

# Problem 8
# Write a function that removes all occurrences of a given letter from a string.

# def remove_letter(theLetter, theString):
#     answer = ''
#     for i in theString:
#         if i not in theLetter:
#             answer = answer + i
#     return answer
#
# print(remove_letter("t", "The President of the United States"))

# Problem 9
# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).

# def reverse(astring):
#     variable = ""
#     for i in astring:
#         variable = i + variable
#     return variable
#
# def is_palindrome(myStr):
#     check = reverse(myStr)
#     if myStr == check:
#         return True
#     else:
#         return False
#
# print(is_palindrome("abba"))

# Problem 10
# Write a function that counts how many times a substring occurs in a string.

# 85%
# def count(substr, theStr):
#     i = 0
#     answer = 0
#     found = False
#     while i < len(theStr):
#         if substr in theStr and substr != theStr:
#             answer = answer + 1
#             # j = i + 1
#             i = i + 1
#             theStr = theStr[i:]
#
#         else:
#             i = i + 1
#     return answer
# print(count("aaa", "aaaaaa"))

# 100%
# def count(substr, theStr):
#     i = 0
#     answer = 0
#     start = 0
#     while i < len(theStr):
#         if substr in theStr:
#             a = theStr.find(substr,start)
#             if a == -1:
#                 break
#             answer += 1
#             start = a+1
#         else:
#             i = i + 1
#     return answer
# print(count("aaa", "aaaaaa"))

# Question 11
# Write a function that removes the first occurrence of a string from another string.

# def remove (substr, theStr):
#     i = 0
#     start = 0
#     r_len = len(substr)
#     found = False
#     while i < len(theStr) and found is not True:
#         if substr in theStr:
#             start = theStr.find(substr)
#             if start == -1:
#                 break
#             strLen = len(theStr)
#             answer = theStr[:start]+theStr[start+r_len:]
#             found = True
#         else:
#             answer = theStr
#             found = True
#     return answer
# test = "bicycle"
# r_test = "cyc"
#
# print(remove(r_test, test))

# Question 12
# Write a function that removes all occurrences of a string from another string.

# def remove_all(substr, theStr):
#     i = 0
#     start = 0
#     r_len = len(substr)
#     found = False
#     while i < len(theStr) and found is not True:
#         if substr in theStr:
#             start = theStr.find(substr)
#             if start == -1:
#                 break
#             strLen = len(theStr)
#             answer = theStr[:start] + theStr[start+r_len:]
#             theStr = answer
#             i += 1
#         else:
#             answer = theStr
#             found = True
#     return answer
# test = "python rocks on"
# r_test = "on"
#
# print(remove_all(r_test, test))

# Question 13
# Here is another interesting L-System called a Hilbert curve. Use 90 degrees:

# import turtle
#
# def applyRule (lhch):
#     rhstr = ""
#     if lhch == "L":
#         rhstr = "+RF-LFL-FR+"
#     elif lhch == "R":
#         rhstr = "-LF+RFR+FL-"
#     else:
#         rhstr = lhch
#     return rhstr
#
# def processStr(oldStr):
#     newStr = ""
#     # iter = 0
#     # checker = len(oldStr)
#     for ch in oldStr:
#         # iter = iter + 1
#         newStr = newStr + applyRule(ch)
#         # iterCheck = checker - iter
#     return newStr
#
# def createLSystem(numIters, axiom):
#     startString = axiom
#     endString = ""
#     for i in range(numIters):
#         endString = processStr(startString)
#         startString = endString
#     return endString
#
# def drawLSystem (h, instructions, angle, distance):
#     for cmd in instructions:
#         if cmd == "F":
#             h.fd(distance)
#         elif cmd == "B":
#             h.bk(distance)
#         elif cmd == "+":
#             h.rt(angle)
#         elif cmd == "-":
#             h.lt(angle)
#
# def main():
#
#     inst = createLSystem(4, "L")
#     # check = len(inst)
#     print(inst)
#
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     wn.setworldcoordinates(-250, -250, 250, 250)
#
#     honey = turtle.Turtle()
#     honey.color("chocolate")
#     honey.shape("turtle")
#     honey.speed(20)
#
#     honey.pu()
#     honey.goto(-50,50)
#     honey.pd()
#
#     drawLSystem(honey, inst, 90, 5)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()


# Question
# Here is a dragon curve. Use 90 degrees


# import turtle
#
# def applyRule (lhch):
#     rhstr = ""
#     if lhch == "X":
#         rhstr = "X+YF+"
#     elif lhch == "Y":
#         rhstr = "-FX-Y"
#     else:
#         rhstr = lhch
#     return rhstr
#
# def processStr(oldStr):
#     newStr = ""
#     for ch in oldStr:
#         newStr = newStr + applyRule(ch)
#     return newStr
#
# def createLSystem(numIters, axiom):
#     startString = axiom
#     endString = ""
#     for i in range(numIters):
#         endString = processStr(startString)
#         startString = endString
#     return endString
#
# def drawLSystem (h, instructions, angle, distance):
#     for cmd in instructions:
#         if cmd == "F":
#             h.fd(distance)
#         elif cmd == "B":
#             h.bk(distance)
#         elif cmd == "+":
#             h.rt(angle)
#         elif cmd == "-":
#             h.lt(angle)
#
# def main():
#
#     inst = createLSystem(10, "FX")
#     print(inst)
#
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     wn.setworldcoordinates(-250, -250, 250, 250)
#
#     honey = turtle.Turtle()
#     honey.color("chocolate")
#     honey.shape("turtle")
#     honey.speed(20)
#
#     honey.pu()
#     honey.goto(-50,50)
#     honey.pd()
#
#     drawLSystem(honey, inst, 90, 5)
#
#     wn.exitonclick()
#
# if __name__ == '__main__':
#     main()

# Question 18
# Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for
# another to garble the message. For example A -> Q, B -> T, C -> G etc. your function should take two parameters,
# the message you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet.
# Your function should return a string that is the encrypted version of the message.

# import string
#
# def encrypt(vari, shift):
#     upperCase = string.ascii_uppercase
#     lowerCase = string.ascii_lowercase
#     output = ""
#     for ch in vari:
#         if ch in upperCase or ch in lowerCase:
#             value = ord(ch)
#             newCh = ""
#             if value <= 90:
#                 value = value + shift
#                 if value > 90:
#                     value = value - 26
#                 newCh = chr(value)
#                 output = output + newCh
#             else:
#                 value = value + shift
#                 if value > 122:
#                     value = value - 26
#                 newCh = chr(value)
#                 output = output + newCh
#         else:
#             output = output + ch
#     return output
# print(encrypt("Linkin", 6))

# Question 19
# Write a function that decrypts the message from the previous exercise. It should also take two parameters.
# The encrypted message, and the mixed up alphabet. The function should return a string that is the same as
# the original unencrypted message.

# import string
#
# def decryption(vari, shift):
#     upperCase = string.ascii_uppercase
#     lowerCase = string.ascii_lowercase
#     output = ""
#     for ch in vari:
#         if ch in upperCase or ch in lowerCase:
#             value = ord(ch)
#             if value <= 90:
#                 value = value - shift
#                 if value < 65:
#                     value = value + 26
#                 newCh = chr(value)
#                 output = output + newCh
#             else:
#                 value = value - shift
#                 if value < 97:
#                     value = value + 26
#                 newCh = chr(value)
#                 output = output + newCh
#         else:
#             output = output + ch
#     return output
#
# print(decryption("Nkrru, Cuxrj!", 6))

