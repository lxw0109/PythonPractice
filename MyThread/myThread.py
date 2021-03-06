#!/usr/bin/python2.7
#File: myThread.py
#Author: lxw
#Time: 2014-09-06

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, num, name=""):
    #def __init__(self, func, args, name=""):
        #if the subclass overrides the constructor, it must make sure to invoke the base class constructor (Thread.__init__()) before doing anything else to the thread.
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.num = num
        self.name = name

    def getResult(self):
        return self.res

    def run(self):
        self.res = ""
        with self.num:
            #print("start {0} at: {1}".format(self.name, ctime()))
            self.res = apply(self.func, self.args)
            #print("end {0} at: {1}".format(self.name, ctime()))
        """
        print("start {0} at: {1}".format(self.name, ctime()))
        self.res = apply(self.func, self.args)
        print("end {0} at: {1}".format(self.name, ctime()))
        """
