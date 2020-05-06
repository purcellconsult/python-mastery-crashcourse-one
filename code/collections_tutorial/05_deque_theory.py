#######################################
# Deque theory
# -------------
# Small code snippets that highlight the
# the functionality of a deque in python. 
#
#
#
#
#######################################

from collections import deque

d = deque([2, 1, 4, 6, 10, 10, 100])

print(d)
print(d[0])
print(d[-1])
print(len(d))

for item in d:
    print(item)

print(d.pop())
print(d)
d.appendleft(500)
print(d)
print(list(d))
print(list(reversed(d)))
d.extend([5, 7, 10])
print(d)





























































