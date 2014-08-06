#
#	punkiq130@gmail.com 
#

import random

def qsort(qslist):
	
	small = []
	big = []

	if (len(qslist) < 2):
		return qslist

	elif (len(qslist) > 1):

		pivot = qslist[int(random.randrange(len(qslist)))]

		for x in range(len(qslist)):
			if qslist[x] <= pivot: 
				small.append(qslist[x])
			else: 
				big.append(qslist[x])
		if(len(big) == 0):
			big.append(pivot)
			small.remove(pivot)

	return qsort(small) + qsort(big) 

qslist = [9,1,8,2,7,3,6,4,5]

print(qsort(qslist))


