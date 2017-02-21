#!/usr/bin/python2.7
# File: basicPython.py
# Author: lxw
# Time: 2014-03-10

import random
#[Google Code Style] Do not use '*' in 'import' expression
#'from Thread import MyThread' is better than 'from Thread import *'

#logging.logger
import logging
def loggerDemo():
    print logging.CRITICAL
    print logging.ERROR
    print logging.WARNING
    print logging.INFO
    print logging.DEBUG
    print logging.NOTSET
loggerDemo()

# name of a module
if __name__ == "__main__":
    #[Google Code Style] give priority to %
    #print "{0} is being run by itself".format(__name__)
    print("%s is being run by itself" % __name__)
else:
    # __name__ == basicPython
    print("%s is imported as a module" % __name__)


def whileIfDemo():
    # while & if
    target = random.randint(1, 100)
    # "while 1" is faster than "while Ture".
    # while True:
    while 1:
        #number = int(input("Please input an integer:")) #python 3+
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


def forDemo():
    # for
    # Both of the following 2 methods of "for" are OK.
    # for i in [0, 1, 2, 3, 4]:
    for i in range(0, 5):
        print i,
    for i in range(1, 10, 2):  # "range" is powerful
        print i,


# function demo
def sayHello():
    print "Hello World!"

#sayHello()  # call the function
#print sayHello()  # NOTE the word "NONE" is printed.

def printMax(a, b):
    if a > b:
        print "{0} > {1}".format(a, b)
        # print(a, " > ", b)    #Python 3.0
    elif a < b:
        print "{0} < {1}".format(a, b)
    else:
        print "{0} = {1}".format(a, b)
#printMax(30, 20)


# OO
class Person(object):
    def __init__(self, name):
        self.name = name
    def sayHello(self):  # Every function needs at least a parameter which represent the object itself.
        print "Hello {0}".format(self.name)
    def func(self):
        pass  # empty block

def OODemo():
    p = Person("lxw")
    p.sayHello()
    #with object: <class '__main__.Person'>; without object: <type 'instance'>
    print(type(p))
    #with object: <type 'type'>; without object: <type 'classobj'>
    print(type(Person))


def exceptionDemo():
    # Exception
    try:
        # text = input("Enter something:")
        # For Python 2.7.*: your_input_string is NOT OK.  "your_input_string" is OK. "" here is essential.
        # For Python 3.*: both are OK.
        text = raw_input("Enter something:")
    except EOFError as eof:  # Ctrl + D
    #except EOFError, eof:  #[Google Code Style]The previous line is better than the following line.
        print("Why did you do an EOF on me?")
    except KeyboardInterrupt as ki:  # Ctrl + C
        print("You cancelled the operation.")
    else:   #NOTE: Do NOT come here when except showed.
        print("You entered {0}".format(text))


# To reverse a string in Python is so easy.
def reverse(text):
    return text[::-1]
#print reverse("Hello World!")


#[Google Code Style]
#1.
def strFormat():
    x = 1
    print "x: %d." % x
    #Simple condition expression can be written in a single line.
    x = 5 if x < 5 else x
    print "x: %d." % x


#2. Default Argument Values
def foo(a, b = None):
    if b is None:
        b = []
    print a, b

#the method foo() is better than method foo1().
def foo1(a, b = []):
    print a, b

#If both foo(a, b = None) and foo(a, b = []) exist, the NEAREST(to the caller) will be invoked
'''
def foo(a, b = []):
    print "second"
    print a, b
'''

def callFoo():
    foo(1)
    foo(1, 2)
    #the following line is better than the previous line.
    foo(1, b = 2)

    foo1(1)
    foo1(1, 2)
    foo1(1, b = 2)


#3. Never use == or != to compare singletons like None. Use is or is not.
def Note():
    x = Person("lxw")
    if x is not None:
        print "x is not None"
    if x:   #OK: if not x
        print "x is not None"

    #When handling integers use == or !=:
    num = 10
    #Yes:
    if not x:
        print 'no x'
    if num == 0:
        pass
    if num % 10 == 0:
        pass

    nums = []
    if len(nums) == 0:
        print("[] length is 0")		#Y
    if not nums:
        print("not [] is true")	        #Y
    if nums is None:
        print("[] is None")             #N
    if nums is not None:
        print("[] is not None")         #Y
    if not num % 10:
        print("'not num % 10' is true") #Y
