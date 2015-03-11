#!/usr/bin/python
#File: quickSort.py
#Author: lxw
#Time: 2014-03-17
#Usage:	Quick sort in Python.

def quickSort(arr, start, end):
	if start >= end:	# EXIT
		return
	i = start
	j = end
	target = arr[i]
	while i < j:
		while arr[i] <= target and i < end:
			i += 1
		while arr[j] > target and j > start:
			j -= 1
		if i < j:
			arr[i], arr[j] = arr[j], arr[i]
	arr[start] = arr[j]
	arr[j] = target
	quickSort(arr, start, j - 1)
	quickSort(arr, j + 1, end)

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

	quickSort(arr1, 0, len(arr1) - 1)
	quickSort(arr2, 0, len(arr2) - 1)
	quickSort(arr3, 0, len(arr3) - 1)
	quickSort(arr4, 0, len(arr4) - 1)

	show(arr1)
	show(arr2)
	show(arr3)
	show(arr4)
	print '' 

if __name__ == '__main__':
	main()
else:
	print 'Imported as a module'
