#
#	punkiq130@gmail.com 
#

import random

def qsort(list):
	
	small = []
	big = []

	if (len(list) < 2):
		return list

	elif (len(list) > 1):

		pivot = list[int(random.randrange(len(list)))]

		for x in range(len(list)):
			if list[x] <= pivot: 
				small.append(list[x])
			else: 
				big.append(list[x])
		if(len(big) == 0):
			big.append(pivot)
			small.remove(pivot)

	return qsort(small), qsort(big) 

list = [9,1,8,2,7,3,6,4,5]

print qsort(list)

