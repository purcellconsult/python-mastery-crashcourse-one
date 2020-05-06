#############################################
# Demo of methods in Counter
# --------------------------
#
# Below is a little script to demo the
# functionality of a Counter in python. 
# After all, sometimes the description of 
# what they do is not as evident as seeing
# a self-explanatory snippet of code. 
#
#############################################

from collections import Counter


# elements
# --------
# returns an iterator over elements repeating
# each as many times as its count. Elements are
# returned in the order in which they're first
# encountered


vowels = Counter(a=5, e=3, i=7, o=9, u=5)
sorted(vowels.elements())
print(vowels)


# most_common
# -----------
# returns a list of the n most common elements 
# and their counts from the most common to the least


phrase = Counter('This is a big world after all').most_common()
for x in phrase:
    print(x)


# subtract
# --------
# Elements are subtracted from an iterable or from another mapping or dict
# In other words it's similar to dict.update() except that it subtracts

names_one = Counter(['jack', 'jill', 'jim', 'jeff'])
names_two = Counter(['jack', 'jim'])
names_one.subtract(names_two)
print(names_one)
