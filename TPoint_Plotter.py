import turtle

wn = turtle.Screen()
niko = turtle.Turtle()
niko.shape('turtle')
niko.speed(15)


class TPointPlotter():
    def __init__(self):
        """Initialize the class"""

    def create_dict_from_list(self, c_list):
        """Create a dictionary from list that was generated from a file."""
        numb = 0
        xy_dict = {}
        for i in c_list:
            xy_cord = "xy_cord" + str(numb)
            brk_pt = i.index(" ")
            x_value = int(i[:brk_pt])
            y_value = int(i[brk_pt + 1:])
            xy_dict[xy_cord] = x_value, y_value
            numb += 1
        self.plot_points(self, xy_dict)
        return xy_dict

    def plot_points(self, pp_dict):
        """Plot the points of the raw data on a graph."""
        min_max_lst = self.break_cord(pp_dict)
        x_lst = min_max_lst.pop(0)
        y_lst = min_max_lst.pop(0)
        x_max_value = max(x_lst)
        y_max_value = max(y_lst)
        niko.speed(15)
        wn.setworldcoordinates(-10, -10, x_max_value + 10, y_max_value + 10)
        for cords, points in pp_dict.items():
            x_point = points[0]
            y_point = points[1]
            niko.up()
            niko.goto(x_point, y_point)
            niko.dot()

    def plotRegression(self, pr_dict):
        """Plot the regression line on the graph"""
        new_pr_lst = self.dict_to_lst(pr_dict)
        pr_lst = []
        """take the minimum and maximum coordinates and draw the regression line"""
        pr_lst.append(new_pr_lst.pop(0))
        pr_lst.append(new_pr_lst.pop())
        for points in pr_lst:
            x_point = points[0]
            y_point = points[1]
            niko.goto(x_point, y_point)
            niko.pd()

    def break_cord(bc_dict):
        """Build two lists to de able to determine the min and max setting for turtle screen"""
        aft_bc_x_lst = []
        aft_bc_y_lst = []
        after_bc_lst = []
        for i, z in bc_dict.items():
            one_val = z[0]
            two_val = z[1]
            aft_bc_x_lst.append(one_val)
            aft_bc_y_lst.append(two_val)
        after_bc_lst.append(aft_bc_x_lst)
        after_bc_lst.append(aft_bc_y_lst)
        return after_bc_lst

    def dict_to_lst(dl_dict):
        """Convert the dictionary to lists"""
        new_lst = []
        for values in dl_dict.values():
            new_lst.append(values)
        new_lst.sort()
        return new_lst
