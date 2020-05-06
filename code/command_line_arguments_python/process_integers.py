import sys

for x in sys.argv[1:]:  # reads all the integers in a program 
    if not isinstance(x, int):
        y = int(x)
        print(y)
    else:
        raise ValueError('not an integer')
    