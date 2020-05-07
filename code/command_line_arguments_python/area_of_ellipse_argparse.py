#############################
# Area of an ellipse
# ------------------
# A=πab
# 'a' is the 'a axis'
# 'b' is the 'b axis'
# We will use the argparse module
# to add flags and process the program.
# This module is used heavily in
# the industry.
###############################

import argparse
from math import pi

parser = argparse.ArgumentParser(description='Compute area of an ellipse')
parser.add_argument('-a', '--Axis', type=int, help='a axis of an ellipse')
parser.add_argument('-b', '--Bxis', type=int, help='b axis of an ellipse')
args = parser.parse_args()


def area_of_ellipse(a_xis, b_xis):
    return pi * a_xis * b_xis


if __name__ == '__main__':
    print(round(area_of_ellipse(args.Axis, args.Bxis), 2))