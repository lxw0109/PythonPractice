#!/usr/bin/python
#File: grade2QS.py
#Author: lxw
#Time: 2014-03-23
#Usage:	What does 'Quick Sort' look like in Python.

def qs(arr):
	if not arr:
		return []
	return qs([x for x in arr[1:] if x <= arr[0]]) + arr[:1] + qs([x for x in arr[1:] if x > arr[0]])

def show(arr):
	for element in arr:
		print str(element) + ' ',
	print ''

def main():
	arr1 = [1, 2, 3, 4, 5, 5, 6]
	arr2 = [52, 23, 4]
	arr3 = [1]
	arr4 = [2, 3]
	
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
