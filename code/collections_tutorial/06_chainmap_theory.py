#########################################
# ChainMap Example
# -------------
# Highlights some of the common 
# functionality of a ChainMap in python. 
#
#
#
#########################################

from collections import ChainMap

d1 = {'a': 1, 'b': 3}  		# dictionary one
d2 = {'b': 5, 'c': 6}  		# dictionary two 

chain = ChainMap(d1, d2) 	# chains dictionaries together 
print(chain)








