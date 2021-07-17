# HTLCS 12.7 Exercises
# My name: Don Trapp


# Problem 15
# Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each letter occurs.
# Case should be ignored.

# import string
#
#
# def count_letters_matrix(p,d):
#     new_d = {}
#     for m in p:
#         if m in d.keys():
#             d[m] = d[m] + 1
#         else:
#             continue
#     for (k, v) in d.items():
#         if v > 0:
#             new_d[k] = v
#         else:
#             continue
#     return new_d
#
#
# def count_dictionary():
#     count_dictionary_func = {}
#     for i in string.ascii_lowercase:
#         count_dictionary_func[i] = 0
#     return count_dictionary_func
#
#
# def main():
#     quote = str(input("Please enter a sentence to be analyized"))
#     if quote != "None":
#         c_quote = quote.lower()
#         ct_dictionary = count_dictionary()
#         check_diction = count_letters_matrix(c_quote, ct_dictionary)
#
#         print(quote)
#         print(check_diction)
#     else:
#         print("Why don't you like us?", "\nPlease try again.")
#
#
# if __name__ == '__main__':
#     main()

# Problem 16
#
# def add_fruit(inventory, fruit, quantity=0):
#     if fruit in inventory:
#         inventory[fruit] = inventory[fruit] + quantity
#     else:
#         inventory[fruit] = quantity
#     return inventory
#
# # make these tests work...
# new_inventory = {}
# print(add_fruit(new_inventory, 'strawberries', 10))
# #  test that 'strawberries' in new_inventory
# #  test that new_inventory['strawberries'] is 10
# if 'strawberries' in new_inventory and new_inventory['strawberries'] == 10:
#     print(add_fruit(new_inventory, 'strawberries', 25))
# #  test that new_inventory['strawberries'] is now 35)
# if new_inventory['strawberries'] == 35:
#     print("Success")
# else:
#     print("Failure")


# Problem 17
# Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical
# listing of all the words, and the number of times each occurs, in the text version of
# Alice’s Adventures in Wonderland. How many times does the word, alice, occur in the book?
#
# import string
#
#
# def word_count_dict(cword_list, mword_list):
#     dict_word_count = {}
#     for word in cword_list:
#         ct_word = mword_list.count(word)
#         dict_word_count[word] = ct_word
#     return dict_word_count
#
#
# def word_list_func(line_list):
#     main_word_list = []
#     count_word_list = []
#     tester = string.punctuation
#     for line_string in line_list:
#         sub_word_lst = line_string.split()
#         for word in sub_word_lst:
#             word = word.lower()
#             word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
#             word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
#             word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
#             word = word.replace(']', '').replace(';', '')
#             main_word_list.append(word)
#     for uniq_word in main_word_list:
#         if uniq_word not in count_word_list:
#             count_word_list.append(uniq_word)
#     answer = word_count_dict(count_word_list, main_word_list)
#     return answer
#
#
# def main():
#     filename = 'C:/Users/willi/Documents/alice_wonderland.txt'
#     with open(filename) as file_object:
#         content = file_object.readlines()
#     lst_content = []
#     for line in content:
#         line = line.strip()
#         if line != '':
#             lst_content.append(line)
#     check = word_list_func(lst_content)
#     output_string = ''
#     new_filename = 'C:/Users/willi/Documents/alice_wonderland_word_count.txt'
#     with open(new_filename, 'a') as file_object:
#         for key, value in sorted(check.items()):
#             output_string = key + '\t' + str(value) + '\n'
#             file_object.write(output_string)
#
#
# if __name__ == '__main__':
#     main()


# Problem 18

# def word_count_dict(cword_list, mword_list):
#     dict_word_count = {}
#     for word in cword_list:
#         ct_word = mword_list.count(word)
#         len_word = len(word)
#         dict_word_count[word] = len_word
#     return dict_word_count
#
#
# def word_list_func(line_list):
#     main_word_list = []
#     count_word_list = []
#     for line_string in line_list:
#         sub_word_lst = line_string.split()
#         for word in sub_word_lst:
#             word = word.lower()
#             main_word_list.append(word)
#     for uniq_word in main_word_list:
#         if uniq_word not in count_word_list:
#             count_word_list.append(uniq_word)
#     answer = word_count_dict(count_word_list, main_word_list)
#     return answer
#
#
# def main():
#     filename = 'C:/Users/willi/Documents/alice_wonderland.txt'
#     with open(filename) as file_object:
#         content = file_object.readlines()
#     lst_content = []
#     for line in content:
#         line = line.strip()
#         if line != '':
#             lst_content.append(line)
#     check = word_list_func(lst_content)
#     output_string = ''
#     new_filename = 'C:/Users/willi/Documents/alice_wonderland_word_length.txt'
#     with open(new_filename, 'a') as file_object:
#         for key, value in sorted(check.items()):
#             output_string = key + '\t' + str(value) + '\n'
#             file_object.write(output_string)
#
#
# if __name__ == '__main__':
#     main()

# Problem 19
# Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.
#
# import re
#
#
# def translate_user_input(dict_trans):
#     translation = ''
#     usr_input = input("Give me a phrase in English and I will translate it into Pirate: ")
#     usr_input = usr_input.split()
#     for word in usr_input:
#         word = word.lower()
#         if word in dict_trans.keys():
#             pir_word = dict_trans.get(word)
#         else:
#             pir_word = word
#         if translation == '':
#             pir_word = pir_word.title()
#             translation = translation + pir_word
#         else:
#             translation = translation + " " + pir_word
#     test = translation
#
# def build_dict_translator(raw_list):
#     translate_dict = {}
#     for words in raw_list:
#         words = words.split()
#         key = words.pop(0)
#         if len(words) > 1:
#             value1 = words.pop(0)
#             value2 = words.pop(0)
#             value = value1 + " " + value2
#         else:
#             value = words.pop(0)
#         translate_dict[key] = value
#     translate_user_input(translate_dict)
#
#
# def main():
#     filename = 'C:/Users/willi/Documents/English_to_Pirate.txt'
#     with open(filename) as file_object:
#         content = file_object.readlines()
#     lst_content = []
#     for line in content:
#         line = re.sub(r'\W+', ' ', line)
#         line = line.strip()
#         if line != '':
#             lst_content.append(line)
#
#     build_dict_translator(lst_content)
#
#
# if __name__ == '__main__':
#     main()
