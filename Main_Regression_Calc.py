from turtle import Screen
from TPoint_Plotter import TPointPlotter as TPP
from Regression_Calcuations import RegCalc as RC


def create_dict_from_list(c_list):
    """Create a dictionary from list that was generated from a file."""
    xy_dict = {}
    numb = 0
    for i in c_list:
        xy_cord = "xy_cord" + str(numb)
        brk_pt = i.index(" ")
        x_value = int(i[:brk_pt])
        y_value = int(i[brk_pt + 1:])
        xy_dict[xy_cord] = x_value, y_value
        numb += 1
    return xy_dict


def open_file():
    """Open file and put contents of file into list for further processing."""
    filename = 'C:/Users/willi/Documents/labdata.txt'
    with open(filename) as file_object:
        content = file_object.readlines()
    line_count = 0
    for line in content:
        line = line.strip()
        content[line_count] = line
        line_count += 1
    return content


def main():
    wn = Screen()
    xy_raw_list = open_file()
    xy_dictionary = TPP.create_dict_from_list(TPP, xy_raw_list)
    xy_regression_dict = RC.setup_regression_calc(RC, xy_dictionary)
    TPP.plotRegression(TPP, xy_regression_dict)

    wn.exitonclick()


if __name__ == '__main__':
    main()
