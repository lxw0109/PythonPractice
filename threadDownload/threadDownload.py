#!/usr/bin/python2.7
#coding:utf-8
#File: threadDownload.py
#Author: lxw
#Time: 2015-01-28
#Usage: Multithread downloading.

import urllib2
import os.path
import time
from threading import Thread

class MyThread(Thread):
    '''
    Definition of my thread class.
    '''

    def __init__(self, name, url):
        Thread.__init__(self)   #NOTE: essential.
        self.name = name
        self.url = url

    def run(self):
        handler = urllib2.urlopen(self.url)
        filename = os.path.basename(self.url)
        with open(filename, "w") as f:
            while 1:
                string = handler.read(1024)
                if not string:
                    break
                f.write(string)
        print("Thread {0} has finished downloading \"{1}\"!".format(self.name, self.url))

def main():
    urls = [ "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
             "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
             "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
             "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
             "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
             "http://www.cnblogs.com/lxw0109/p/start_run.html"]
    threads = []
    length = len(urls)
    start = time.time()
    for index in xrange(length):
        th = MyThread(index, urls[index])
        #th.start()
        th.run()
        threads.append(th)

    #for index in xrange(length):
    #    threads[index].join()    #Main thread blocks, until each thread terminates.
    end = time.time()
    #print(type(end))   #float
    print("Program is Over. Time cost: " + str(end - start))

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
