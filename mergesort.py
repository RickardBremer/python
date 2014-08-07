#
#	punkiq130@gmail.com 
#	mergesort

def merge_sort(mslist):

	if len(mslist) <= 1:
		return mslist

	middle = len(mslist)//2

	left = mslist[:middle]
	right = mslist[middle:]
	
	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left,right):

	result = []

	leftlen = len(left)
	rightlen = len(right)

	while leftlen > 0 or rightlen > 0:
		if leftlen > 0 and rightlen > 0:
			if left[0] <= right[0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		elif leftlen > 0:
			result.append(left.pop(0))
		elif rightlen > 0:
			result.append(right.pop(0))
		
		leftlen = len(left)
		rightlen = len(right)	

	return result

def main():

	mslist = [-9,1,1,2,3,2,7,3,6,4,5,4,3,5,6,7,8,9,0,0] * 10
	print(merge_sort(mslist))

if __name__ == "__main__":
	main()
