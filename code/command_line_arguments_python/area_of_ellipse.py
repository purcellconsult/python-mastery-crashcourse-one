#############################
# Area of an ellipse
# ------------------
# A=πab
# 'a' is the 'a axis'
# 'b' is the 'b axis'
#
###############################

from math import pi


def area_of_ellipse(a, b):
    return pi * a * b


if __name__ == '__main__':
    print(round(area_of_ellipse(5, 10), 2))