#!/usr/bin/python2.7
# File: basicPython.py
# Author: lxw
# Time: 2014-03-10

import random

# name of a module
if __name__ == "__main__":
    print "{0} is being run by itself".format(__name__)
else:
    print "{0} is imported as a module".format(__name__)  # __name__ == BasicPython

# while & if
# target = 24
target = random.randint(1, 100)
# "while 1" is faster than "while Ture".
# while True:
while 1:
    # number = int(input("Please input an integer:")) #python 3+
    number = input("Please input an integer:")  # python 2+ #NOTE:The parenthesis is essential.
    if number == target:
        print "You got it"
        break  # Both "break" and "continue" can be found in Python
    elif number > target:
        print "Smaller, you stupid"
    else:
        print "Bigger, you stupid"

print "Over"


# There is no "switch" in Python


# for
# Both of the following 2 methods of "for" are OK.
# for i in [0, 1, 2, 3, 4]:
for i in range(0, 5):
    print i,
for i in range(1, 10, 2):  # "range" is powerful
    print i,


# function
def sayHello():
    print "Hello World!"
sayHello()  # call the function
print sayHello()  # NOTE the word "NONE" is printed. <A Byte of Python> P41

def printMax(a, b):
    if a > b:
        print "{0} > {1}".format(a, b)
        # print(a, " > ", b)    #Python 3.0
    elif a < b:
        print "{0} < {1}".format(a, b)
    else:
        print "{0} = {1}".format(a, b)
printMax(30, 20)

def retFunc(x, y):
    if x > y:
        return x
    else:
        return y
print retFunc(10, 20)


# OO
class Person:
    def __init__(self, name):
        self.name = name
    def sayHello(self):  # Every function needs at least a parameter which represent the object itself.
        print "Hello {0}".format(self.name)
    def func(self):
        pass  # empty block

p = Person("lxw")
p.sayHello()


# Exception
try:
    # text = input "Enter something:"
    # For Python 2.7.*: your_input_string is NOT OK.  "your_input_string" is OK. "" here is essential.
    # For Python 3.*: both are OK.
    text = raw_input("Enter something:")
except EOFError:  # Ctrl + D
    print("Why did you do an EOF on me?")
except KeyboardInterrupt:  # Ctrl + C
    print("You cancelled the operation.")
else:   #NOTE: Do NOT come here when except showed. 
    print("You entered {0}".format(text))


# To reverse a string in Python is so easy.
def reverse(text):
    return text[::-1]
print reverse("Hello World!")
textOne = "lxw"
print reverse(textOne)
