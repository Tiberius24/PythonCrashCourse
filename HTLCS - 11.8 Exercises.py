# HTLCS - 11.8 Exercises
# My Name: Don Trapp

# The following sample file called studentdata.txt contains one line for each student in an imaginary class.
# The student’s name is the first thing on each line, followed by some exam scores. The number of scores might be
# different for each student. Using the text file studentdata.txt write a program that prints out the names of
# students that have more than six quiz scores.


# import string
#
# '''Global Variables'''
# character = string.ascii_lowercase
# punctuation = string.punctuation
# letters = string.ascii_letters
#
#
# def build_dictionary(s_list, g_list):
#     bd_student_grades_dict = {}
#     for indx in range(len(s_list)):
#         bd_student = s_list[indx]
#         bd_grades = g_list[indx]
#         bd_student_grades_dict[bd_student] = bd_grades
#     return bd_student_grades_dict
#
#
# def student_grades(c_list):
#     sg_student_list = []
#     sg_grades_list = []
#     for i in c_list:
#         s_name = ""
#         str_slice_value = 0
#         sg_idv_grades_list = []
#         for j in i:
#             if j in character:
#                 str_index_value = i.index(j)
#                 s_name = s_name + i[str_index_value]
#                 str_slice_value = str_slice_value + 1
#             else:
#                 continue
#         grades = i[str_slice_value:]
#         g_score = ""
#         for k in grades:
#             if k not in letters and k not in punctuation and k != " ":
#                 str_index_value = i.index(k)
#                 g_score = g_score + i[str_index_value]
#                 str_slice_value = str_slice_value + 1
#             elif g_score != "" and k == " ":
#                 sg_idv_grades_list.append(g_score)
#                 g_score = ""
#             else:
#                 continue
#         sg_grades_list.append(sg_idv_grades_list)
#         sg_student_list.append(s_name)
#     sg_master_dict = build_dictionary(sg_student_list, sg_grades_list)
#     return sg_master_dict
#
#
# def quiz_check(data):
#     qc_quiz_analysis = ""
#     qc_master_dict = student_grades(data)
#     for (key, values) in qc_master_dict.items():
#         if len(values) >= 6:
#             qc_quiz_analysis = qc_quiz_analysis + key.capitalize() + "\n"
#         else:
#             continue
#     return qc_quiz_analysis
#
#
# def open_file(f_name):
#     with open(f_name) as file_object:
#         content = file_object.readlines()
#     line_cnt = 0
#     for line in content:
#         line = line.strip()
#         content[line_cnt] = line
#         line_cnt += 1
#     return quiz_check(content)
#
#
# def main():
#     filename = 'studentdata.txt'
#     test = open_file(filename)
#     print(test)
#
#
# if __name__ == '__main__':
#     main()


# Problem 2
# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for each
# student, and print out the student’s name along with their average grade.

# import string
#
# '''Global Variables'''
# character = string.ascii_lowercase
# punctuation = string.punctuation
# letters = string.ascii_letters
#
# def student_grades(c_list):
#     sg_student_list = []
#     sg_grades_list = []
#     sg_master_list = []
#     for i in c_list:
#         s_name = ""
#         str_slice_value = 0
#         sg_idv_grades_list = []
#         for j in i:
#             if j in character:
#                 str_index_value = i.index(j)
#                 s_name = s_name + i[str_index_value]
#                 str_slice_value = str_slice_value + 1
#             else:
#                 continue
#         grades = i[str_slice_value:]
#         g_score = ""
#         for k in grades:
#             if k not in letters and k not in punctuation and k != " ":
#                 str_index_value = i.index(k)
#                 g_score = g_score + i[str_index_value]
#                 str_slice_value = str_slice_value + 1
#             elif g_score != "" and k == " ":
#                 sg_idv_grades_list.append(g_score)
#                 g_score = ""
#             else:
#                 continue
#         sg_grades_list.append(sg_idv_grades_list)
#         sg_student_list.append(s_name)
#     sg_master_list.append(sg_student_list)
#     sg_master_list.append(sg_grades_list)
#     return sg_master_list
#
#
# def quiz_check(data):
#     qc_quiz_analysis = ""
#     qc_master_list = student_grades(data)
#     for sep_list in range(len(qc_master_list)):
#         qc_pop_list = qc_master_list.pop(0)
#         qc_p_lst_check = qc_pop_list[0]
#         if isinstance(qc_p_lst_check, list):
#             qc_p_lst_check = qc_p_lst_check[0]
#             if qc_p_lst_check.isalpha() is True:
#                 qc_student_list = qc_pop_list
#             else:
#                 qc_grades_list = qc_pop_list
#         else:
#             if qc_p_lst_check.isalpha() is True:
#                 qc_student_list = qc_pop_list
#             else:
#                 qc_grades_list = qc_pop_list
#     for i in range(len(qc_student_list)):
#         qc_student_grades = qc_grades_list[i]
#         qc_quiz_sum = 0
#         for n in qc_student_grades:
#             qc_quiz_sum = qc_quiz_sum + int(n)
#         qc_quiz_avg = qc_quiz_sum // len(qc_student_grades)
#         qc_student = qc_student_list[i]
#         qc_quiz_analysis = qc_quiz_analysis + (qc_student.title() + ": " + str(qc_quiz_avg)) + " GPA" "\n"
#     return qc_quiz_analysis
#
#
# def open_file(f_name):
#     with open(f_name) as file_object:
#         content = file_object.readlines()
#     line_cnt = 0
#     for line in content:
#         line = line.strip()
#         content[line_cnt] = line
#         line_cnt += 1
#     return quiz_check(content)
#
# def main():
#     filename = 'studentdata.txt'
#     test = open_file(filename)
#     print(test)
#
#
# if __name__ == '__main__':
#     main()

# Problem 3
# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the minimum and
# maximum score for each student. Print out their name as well.


# import string
#
# '''Global Variables'''
# character = string.ascii_lowercase
# punctuation = string.punctuation
# letters = string.ascii_letters
#
# def student_grades(c_list):
#     sg_student_list = []
#     sg_grades_list = []
#     sg_master_list = []
#     for i in c_list:
#         s_name = ""
#         str_slice_value = 0
#         sg_idv_grades_list = []
#         for j in i:
#             if j in character:
#                 str_index_value = i.index(j)
#                 s_name = s_name + i[str_index_value]
#                 str_slice_value = str_slice_value + 1
#             else:
#                 continue
#         grades = i[str_slice_value:]
#         g_score = ""
#         for k in grades:
#             if k not in letters and k not in punctuation and k != " ":
#                 str_index_value = i.index(k)
#                 g_score = g_score + i[str_index_value]
#                 str_slice_value = str_slice_value + 1
#             elif g_score != "" and k == " ":
#                 sg_idv_grades_list.append(g_score)
#                 g_score = ""
#             else:
#                 continue
#         sg_grades_list.append(sg_idv_grades_list)
#         sg_student_list.append(s_name)
#     sg_master_list.append(sg_student_list)
#     sg_master_list.append(sg_grades_list)
#     return sg_master_list
#
#
# def determine_max_min(s_list, g_list):
#     dm_quiz_analysis = ""
#     for i in range(len(s_list)):
#         dm_student_grades_int = []
#         dm_student_grades = g_list[i]
#         for grade in dm_student_grades:
#             dm_grade = int(grade)
#             dm_student_grades_int.append(dm_grade)
#         dm_max_grade = max(dm_student_grades_int)
#         dm_min_grade = min(dm_student_grades_int)
#         dm_student = s_list[i]
#         dm_quiz_analysis = dm_quiz_analysis + (dm_student.title() + ": Max " + str(dm_max_grade) +
#                                                " Min: " + str(dm_min_grade)) + "\n"
#     return dm_quiz_analysis
#
#
# def quiz_check(data):
#     qc_master_list = student_grades(data)
#     for sep_list in range(len(qc_master_list)):
#         qc_pop_list = qc_master_list.pop(0)
#         qc_p_lst_check = qc_pop_list[0]
#         if isinstance(qc_p_lst_check, list):
#             qc_p_lst_check = qc_p_lst_check[0]
#             if qc_p_lst_check.isalpha() is True:
#                 qc_student_list = qc_pop_list
#             else:
#                 qc_grades_list = qc_pop_list
#         else:
#             if qc_p_lst_check.isalpha() is True:
#                 qc_student_list = qc_pop_list
#             else:
#                 qc_grades_list = qc_pop_list
#     qc_max_min = determine_max_min(qc_student_list, qc_grades_list)
#     return qc_max_min
#
#
# def open_file(f_name):
#     with open(f_name) as file_object:
#         content = file_object.readlines()
#     line_cnt = 0
#     for line in content:
#         line = line.strip()
#         content[line_cnt] = line
#         line_cnt += 1
#     # return quiz_check(content)
#
# def main():
#     filename = 'studentdata.txt'
#     test = open_file(filename)
#     print(test)
#
#
# if __name__ == '__main__':
#     main()

# Problem 4
# Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair.
# Write a function called plotRegression that reads the data from this file and uses a turtle to plot those points
# and a best fit line according to the following formulas:
# where x¯x¯ is the mean of the x-values, y¯y¯ is the mean of the y- values and nn is the number of points.
# If you are not familiar with the mathematical ∑∑ it is the sum operation. For example ∑xi∑xi means to add up
# all the x values.Your program should analyze the points and correctly scale the window using setworldcoordinates so
# that that each point can be plotted. Then you should draw the best fit line, in a different color, through the points.

# import turtle
#
#
# def dict_to_lst(dl_dict):
#     new_lst = []
#     for values in dl_dict.values():
#         new_lst.append(values)
#     new_lst.sort()
#     return new_lst
#
#
# def calculate_m(ps, xc, xa, ya, xsq):
#     top_m = ps - (xc * xa * ya)
#     bot_m = xsq - (xc * xa**2)
#     ret_m = top_m / bot_m
#     return ret_m
#
#
# def break_cord(bc_dict):
#     aft_bc_x_lst = []
#     aft_bc_y_lst = []
#     after_bc_lst = []
#     for i, z in bc_dict.items():
#         one_val = z[0]
#         two_val = z[1]
#         aft_bc_x_lst.append(one_val)
#         aft_bc_y_lst.append(two_val)
#     after_bc_lst.append(aft_bc_x_lst)
#     after_bc_lst.append(aft_bc_y_lst)
#     return after_bc_lst
#
#
# def plot_points(n, wn, pp_dict):
#     min_max_lst = break_cord(pp_dict)
#     x_lst = min_max_lst.pop(0)
#     y_lst = min_max_lst.pop(0)
#     x_max_value = max(x_lst)
#     y_max_value = max(y_lst)
#     n.speed(15)
#     wn.setworldcoordinates(-10, -10, x_max_value + 10, y_max_value + 10)
#     for cords, points in pp_dict.items():
#         x_point = points[0]
#         y_point = points[1]
#         n.up()
#         n.goto(x_point, y_point)
#         n.dot()
#
#
# def plotRegression(pr_dict, n):
#     new_pr_lst = dict_to_lst(pr_dict)
#     pr_lst = []
#     pr_lst.append(new_pr_lst.pop(0))
#     pr_lst.append(new_pr_lst.pop())
#     for points in pr_lst:
#         x_point = points[0]
#         y_point = points[1]
#         n.goto(x_point, y_point)
#         n.pd()
#
#
# def setup_formula(xy_dict, n, wn):
#     x_sum = 0
#     x_count = 0
#     y_sum = 0
#     y_count = 0
#     prod_sum = 0
#     x_sqr_sum = 0
#     for cords, values in xy_dict.items():
#         x_cord = values[0]
#         y_cord = values[1]
#         x_sum = x_sum + x_cord
#         x_count = x_count + 1
#         y_sum = y_sum + y_cord
#         y_count = y_count + 1
#         prod_sum = prod_sum + (x_cord * y_cord)
#         x_sqr_sum = x_sqr_sum + x_cord**2
#     plot_points(n, wn, xy_dict)
#     x_avg = x_sum / x_count
#     y_avg = y_sum / y_count
#     m = calculate_m(prod_sum, x_count, x_avg, y_avg, x_sqr_sum)
#     return m
#
#
# def calc_regression_cords(xy_dict, n, wn):
#     m = setup_formula(xy_dict, n, wn)
#     x_sum = 0
#     x_count = 0
#     y_sum = 0
#     y_count = 0
#     regression_cords = xy_dict
#     for cords, values in xy_dict.items():
#         x_cord = values[0]
#         y_cord = values[1]
#         x_sum = x_sum + x_cord
#         x_count = x_count + 1
#         y_sum = y_sum + y_cord
#         y_count = y_count + 1
#     x_avg = x_sum / x_count
#     y_avg = y_sum / y_count
#     x_cord = 0
#     y_cord = 0
#     for xy_cords, xy_values in regression_cords.items():
#         x_cord = xy_values[0]
#         y_cord = y_avg + (m * (x_cord - x_avg))
#         regression_cords[xy_cords] = x_cord, y_cord
#         x_cord = 0
#         y_cord = 0
#     plotRegression(regression_cords, n)
#
#
# def create_list(c_list, n, wn):
#     xy_dict = {}
#     numb = 0
#     for i in c_list:
#         xy_cord = "xy_cord" + str(numb)
#         brk_pt = i.index(" ")
#         x_value = int(i[:brk_pt])
#         y_value = int(i[brk_pt + 1:])
#         xy_dict[xy_cord] = x_value, y_value
#         numb += 1
#     return calc_regression_cords(xy_dict, n, wn)
#
#
# def open_file(n, wn):
#     filename = 'C:/Users/willi/Documents/labdata.txt'
#     with open(filename) as file_object:
#         content = file_object.readlines()
#     line_count = 0
#     for line in content:
#         line = line.strip()
#         content[line_count] = line
#         line_count += 1
#     return create_list(content, n, wn)
#
#
# def main():
#     wn = turtle.Screen()
#     niko = turtle.Turtle()
#     niko.shape('turtle')
#     niko.speed(15)
#     open_file(niko, wn)
#
#     wn.exitonclick()
#
#
# if __name__ == '__main__':
#     main()

# Problem 5
# At the bottom of this page is a very long file called mystery.txt The lines of this file contain either the word UP
# or DOWN or a pair of numbers. UP and DOWN are instructions for a turtle to lift up or put down its tail. The pairs of
# numbers are some x,y coordinates. Write a program that reads the file mystery.txt and uses the turtle to draw the
# picture described by the commands and the set of points
#
import turtle

key_words = ('UP', 'DOWN')


def create_drawing(xy_dict, k, wn):
    for key, values in xy_dict.items():
        if key.find('UP') > -1 or key.find('DOWN'):
            if 'UP' in key:
                k.pu()
                for n in values:
                    n = n.split()
                    x_cord = int(n.pop(0))
                    y_cord = int(n.pop(0))
                    k.goto(x_cord, y_cord)
            else:
                k.pd()
                for n in values:
                    n = n.split()
                    x_cord = int(n.pop(0))
                    y_cord = int(n.pop(0))
                    k.goto(x_cord, y_cord)


def create_dictionary(lst_file, k, wn):
    xy_cord_dict = {}
    transfer_lst = []
    numb_key = 0
    for line in lst_file:
        if line in key_words:
            if numb_key == 0:
                key_vari = str(numb_key) + "_" + line
                numb_key += 1
            else:
                xy_cord_dict[key_vari] = transfer_lst
                transfer_lst = []
                key_vari = str(numb_key) + "_" + line
                numb_key += 1
        else:
            transfer_lst.append(line)
    create_drawing(xy_cord_dict, k, wn)


def open_file(k, wn):
    filename = 'C:/Users/willi/Documents/mystery.txt'
    with open(filename) as file_object:
        contents = file_object.readlines()
    line_count = 0
    for line in contents:
        line = line.strip()
        contents[line_count] = line
        line_count += 1
    create_dictionary(contents, k, wn)


def main():
    wn = turtle.Screen()
    koda = turtle.Turtle()
    wn.bgcolor('light green')
    koda.shape('turtle')
    koda.color('chocolate4')
    koda.speed(10)

    open_file(koda, wn)
    wn.exitonclick()


if __name__ == '__main__':
    main()
