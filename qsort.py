#
#	punkiq130@gmail.com 
#	quicksort

import random

def qsort(qslist):
	
	small = []
	big = []

	if (len(qslist) < 2):
		return qslist

	else:
		pivot = random.choice(qslist)

		for x in qslist:
			if x <= pivot: 
				small.append(x)
			elif x > pivot:
				big.append(x)
			
		if(len(big) == 0):
			big.append(pivot)
			small.remove(pivot)

	return qsort(small) + qsort(big) 

qslist = [9,1,8,2,7,3,6,4,5]

print(qsort(qslist))


