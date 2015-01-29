#!/usr/bin/python
#File: grade1QS.py
#Author: lxw
#Time: 2014-03-20
#Usage: Quick Sort. 
#Reference: http://www.kaifazhe.com/python/874.html

def qs(arr):
	if not arr:
		return [] 
	low = []
	high = []
	for x in arr[1:]:
		if x <= arr[0]:
			low.append(x)
		else:
			high.append(x)
	low = qs(low)
	high = qs(high)
	return low + arr[:1] + high	# low + arr[0] + high   is NOT OK! --> ERROR PROMPT: 'can only concatenate list(not int) to list'

def show(arr):
	for x in arr:
		print str(x) + ' ',
	print ''
	
def main():
	arr1 = [1, 2, 3, 2, 5, 5, 6]
	arr2 = [52, 23, 4]
	arr3 = [1]
	arr4 = [12, 3]
	
	show(arr1)
	show(arr2)
	show(arr3)
	show(arr4)
	print '' 

	arr1 = qs(arr1)
	arr2 = qs(arr2)
	arr3 = qs(arr3)
	arr4 = qs(arr4)

	show(arr1)
	show(arr2)
	show(arr3)
	show(arr4)
	print '' 

if __name__ == '__main__':
	main()
else:
	print 'Imported as a module'
