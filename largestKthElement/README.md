Selection Problem:
=================

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
