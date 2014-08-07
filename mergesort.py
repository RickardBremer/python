#
#	punkiq130@gmail.com 
#	mergesort

def merge_sort(mslist):

	if len(mslist) < 2:
		return mslist

	left = mslist[:int(len(mslist)/2)]
	right = mslist[int(len(mslist)/2):]
	
	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left,right):

	result = []

	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				result.append(left[0])
				left.pop(0)
			else:
				result.append(right[0])
				right.pop(0)
		elif len(left) > 0:
			result.append(left[0])
			left.pop(0)
		elif len(right) > 0:
			result.append(right[0])
			right.pop(0)
			
	return result

def main():

	mslist = [-9,1,1,2,3,2,7,3,6,4,5,4,3,5,6,7,8,9,0,0]
	print(merge_sort(mslist))

if __name__ == "__main__":
	main()
