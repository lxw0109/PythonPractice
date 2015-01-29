#!/usr/bin/python
#File: SelectionProblem.py
#Author: lxw
#Time: 2014-04-19
#Usage: 2 implementations of 'Selection Problem'. And some variation problems.

'''
Selection Problem: Get the Kth largest element in an array.
In my program, I set 'k = len(array) / 2'

A good method of implementation of the 'Selection Problem' is based on Quick Sort(abbr. QS).
In my Program, I implemented 2 methods: one is based on QS, the other is based on Selection Sort(abbr. SS).

I implemented some variation problems about 'Selection Problem', they are:
    1. Get k largest items in the arr. The result are NOT in order.
    2. Get k largest items in the arr. The result are in order.

One thing needs to be introduced in advance:
In the following functions, bigKItems() and kthBig() are very very similar. Actually I coded bigKItems() based on kthBig(). 
The difference between them is that kthBig() doesn't change the arr, while bigKItems() changes the arr.

Hope that I didn't confuse you.
'''

import random
import sys
import time


# Based on QS.
#Get the kth largest item in the arr. The standard 'Selection Problem'.
def kthBig(arr, k):
    assert arr
    arr1 = [x for x in arr[1:] if x > arr[0]]
    length = len(arr1)
    if length == k:
        res = arr[0]    # The EXIT of RECURSION.
    elif len(arr1) > k:
        res = kthBig(arr1, k)
    else:
        res = kthBig([x for x in arr[1:] if x <= arr[0]], k - length - 1)
    return res


# Based on SS.
def selectBig(arr, times):
    num = 0
    bound = len(arr)
    index = 0
    while num < times:
        target = -sys.maxint - 1    #arr[0]
        index = 0
        while index < bound:
            if arr[index] > target:
                target = arr[index]
                targetIndex = index
            index += 1
        if targetIndex != bound - 1:    # swap.
            arr[bound - 1], arr[targetIndex] = arr[targetIndex], arr[bound - 1]
        bound -= 1
        num += 1
    return target


# Variation 1.
# Based on QS.
# Get k largest items in the arr. The result are NOT in order.
# The difference between bigKItems() and kthBig() is that kthBig() doesn't change the arr, while bigKItems() changes the arr.
def bigKItems(arr, k):
    assert arr
    arr1 = [x for x in arr[1:] if x > arr[0]]
    arr2 = [x for x in arr[1:] if x <= arr[0]]
    length = len(arr1)
    if length == k:
        arr[:] = arr1 + arr[0:1] + arr2
        return    # The EXIT of RECURSION.
    elif len(arr1) > k:
        bigKItems(arr1, k) 
        #bigKItems(arr[0:len(arr1)], k)  # NO 
    else:
        bigKItems(arr2, k - length - 1)
        #bigKItems(arr[len(arr1)+1:], k - length - 1)    # NO
    arr[:] = arr1 + arr[0:1] + arr2


# Variation 2.
# Based on QS.
# Get k largest items in the arr. The result are in order.
def bigKItemsOrder(arr, k):
    assert arr
    arr1 = [x for x in arr[1:] if x > arr[0]]
    arr2 = [x for x in arr[1:] if x <= arr[0]]
    length = len(arr1)
    if length == k:
        arr1.sort(reverse = True)
        arr[:] = arr1 + arr[0:1] + arr2
        return    # The EXIT of RECURSION.
    elif len(arr1) > k:
        bigKItemsOrder(arr1, k) 
        #bigKItems(arr[0:len(arr1)], k)  # NO 
    else:
        arr1.sort(reverse = True)
        bigKItemsOrder(arr2, k - length - 1)
        #bigKItems(arr[len(arr1)+1:], k - length - 1)    # NO
    arr[:] = arr1 + arr[0:1] + arr2


def tryKthBig():
    while 1:
        #bound = 10
        bound = input('How many intagers do you want to try: ')
        num = 0
        arr = []
        while num < bound:
            arr.append(random.randint(0, 100))
            num += 1

        k = bound / 2
        print('arr is:\n{0}'.format(arr))
        print('')
        print('')
        result = kthBig(arr[:], k - 1)
        arr.sort(reverse = True)
        #arr.sort()
        #arr.reverse()
        # NOTE: arr.sort().reverse() is NOT OK.
        # To verify whether I have get the right answer.
        if result != arr[k - 1]:
            print('WRONG, you stupid! Input anything and system exit!') 
            exit()

        print('The {0}th largest element in the arrary is {1}'.format(k, result))
        

def trySelectBig():
    while 1:
        #bound = 10
        bound = input('How many intagers do you want to try: ')
        num = 0
        arr = []
        while num < bound:
            arr.append(random.randint(0, 100))
            num += 1

        k = bound / 2
        print('arr is:\n{0}'.format(arr))
        print('\n')
        result = selectBig(arr[:], k)
        arr.sort(reverse = True)
        #arr.sort()
        #arr.reverse()
        # NOTE: arr.sort().reverse() is NOT OK.
        # To verify whether I have get the right answer.
        if result != arr[k - 1]:
            print('WRONG, you stupid! Input anything and system exit!') 
            exit()

        print('The {0}th largest element in the arrary is {1}'.format(k, result))
        

def tryBigKItems():
    bound = input('How many intagers do you want to try: ')
    num = 0
    arr = []
    while num < bound:
        arr.append(random.randint(0, 100))
        num += 1
    k = bound / 2
    print('arr is:\n{0}'.format(arr))
    print('\n')
    bigKItems(arr, k - 1)
    print('The largest {0} elements in the arrary are {1}'.format(k, arr[0:k]))
    print('Now arr is:\n{0}'.format(arr))
    print('\n')


def tryBigKItemsOrder():
    bound = input('How many intagers do you want to try: ')
    num = 0
    arr = []
    while num < bound:
        arr.append(random.randint(0, 100))
        num += 1
    k = bound / 2
    print('arr is:\n{0}'.format(arr))
    print('\n')
    bigKItemsOrder(arr, k - 1)
    print('The largest {0} elements in the arrary are {1}'.format(k, arr[0:k]))
    print('Now arr is:\n{0}'.format(arr))
    print('\n')


def testTime():
    num = 0
    bound = 200
    arr = []
    while num < bound:
        arr.append(random.randint(0, 10000))
        num += 1

    print('Based on QuickSort:')
    nowBound = 10
    while nowBound <= bound:
        arrCopy = arr[:nowBound]
        start = time.time()
        bigKItemsOrder(arrCopy, nowBound/2-1)
        #result = kthBig(arr[:nowBound], nowBound/2-1)
        end = time.time()
        result1 = arrCopy[nowBound/2-1]
        runTime1 = end - start

        start = time.time()
        result2 = selectBig(arr[:nowBound], nowBound/2)
        end = time.time()
        runTime2 = end - start
        
        assert result1 == result2
        if runTime1 < runTime2:
            print('{0:^15}{1:^30}{2:^30}{3:^15}'.format(nowBound, runTime1, runTime2, result1))
        nowBound += 10


if __name__ == '__main__':
    choice = raw_input('Compare the 2 implementations: press \'1, <Enter>\'; \n'
            'Get the Kth largest element based on QS: press \'2, <Enter>\';\n'
            'Get the Kth largest element based on SS: press \'3, <Enter>\';\n'
            'Get the Largest K items NOT in order based on QS: press \'4, <Enter>\';\n'
            'Get the Largest K items in order based on QS: press \'5, <Enter>\'\n')

    if choice.strip() == '1':
        print('{0:^15}{1:^30}{2:^15}'.format('Length of arr', 'runTime of QS', 'runTime of SS', 'Kth Largest'))
        testTime()
    elif choice.strip() == '2':
        tryKthBig()
    elif choice.strip() == '3':
        trySelectBig()
    elif choice.strip() == '4':
        tryBigKItems()
    else:
        tryBigKItemsOrder()
        
    print('Congratulations, Program runs over! Bye-Bye!')

else:
    print('This file is imported by someone.')
