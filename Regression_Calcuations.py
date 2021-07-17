class RegCalc():
    def __init__(self):
        """Initialize the class"""

    def setup_regression_calc(self, xy_dict):
        """Utilize dictionary to create initial calculations for regression line"""
        x_sum = 0
        x_count = 0
        y_sum = 0
        y_count = 0
        prod_sum = 0
        x_sqr_sum = 0
        for cords, values in xy_dict.items():
            x_cord = values[0]
            y_cord = values[1]
            x_sum = x_sum + x_cord
            x_count = x_count + 1
            y_sum = y_sum + y_cord
            y_count = y_count + 1
            prod_sum = prod_sum + (x_cord * y_cord)
            x_sqr_sum = x_sqr_sum + x_cord ** 2
        x_avg = x_sum / x_count
        y_avg = y_sum / y_count
        m = self.calculate_m(prod_sum, x_count, x_avg, y_avg, x_sqr_sum)
        reg_cordinates = self.calc_regression_coordinates(xy_dict, x_avg, y_avg, m)
        x_cord = 0
        y_cord = 0
        return reg_cordinates

    def calculate_m(ps, xc, xa, ya, xsq):
        """Calculate the value of m"""
        top_m = ps - (xc * xa * ya)
        bot_m = xsq - (xc * xa ** 2)
        ret_m = top_m / bot_m
        return ret_m

    def calc_regression_coordinates (xy_dict, x_avg, y_avg, m, ):
        regression_cords = xy_dict
        for xy_cords, xy_values in regression_cords.items():
            x_cord = xy_values[0]
            y_cord = y_avg + (m * (x_cord - x_avg))
            regression_cords[xy_cords] = x_cord, y_cord
            x_cord = 0
            y_cord = 0
        return regression_cords
