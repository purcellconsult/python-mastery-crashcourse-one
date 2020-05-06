#############################################
# Counters in python explained
# ----------------------------
#
# A Counter is a specialized container type in
# the collections module. A Counter is a tool
# that's easy and convenient for computing
# tallies. 
#
#
#
#############################################


from collections import Counter
c = Counter()
print(c)
c = Counter('computer')
print(c)
c = Counter({'green':5, 'blue':3, 'yellow':6, 'orange':7, 'blue':5})
print(c)
c = Counter(tigers=5, bears=10, lions=7, elephants=2, zebras=4)
print(c)

