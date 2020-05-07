#############################
# Process integers in python
# --------------------------
# Will write a function top
# read in integers in python
# will show the results of the
# numbers summed, and the numbers
# multiplied.
#
##############################

import sys

list_of_ints, sum, square = [], 0, 1
for x in sys.argv[1:]:
    read_ints = int(x)
    list_of_ints.append(read_ints)

for summation in list_of_ints:
    sum += summation

for multiply in list_of_ints:
    square *= multiply

if __name__ == '__main__':
    print(f'List of numbers is {list_of_ints}')
    print(f'The sum of numbers is {sum}')
    print(f'The multiplication of numbers is {square}')