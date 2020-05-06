############################################
# Named Tuple example in python
# -----------------------------
# Highlights the difference between a 
# traditional tuple and a named tuple 
# in python. 
#
#
#
#############################################

from collections import namedtuple

point_one = (5, 10)
point_two = (75, 100)
subtract = (point_two[0] - point_one[0], point_two[1] - point_one[1])
print(subtract)

Point = namedtuple('Point', ['x', 'y'])
point_one = Point(5, 10)
point_two = Point(75, 100)

subtract = point_two.x - point_one.x, point_two.y - point_one.y)
print(subtract)