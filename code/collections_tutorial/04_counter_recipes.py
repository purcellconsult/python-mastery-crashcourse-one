#############################################
# Common recipes in the Counter Class
# -----------------------------------
#
# Some common recipes that you can use
# when dealing with the Counter class
# in python. 
# 
#
#
#############################################

from collections import Counter

letters = Counter('abshshgsshHJSJJSHJsczbmz,asgkauwye')  # create a Counter of letters 


print(sum(letters.values())) 				# gets total of all counts
print(list(letters))	     				# returns unique elements 
print(dict(letters))	     				# convert to a regular dictionary 
print(letters.items())	     				# converts to a list of elem/cnt pairs
print(letters.most_common()[:-len(letters)-1:-1])	# n least common elememts



