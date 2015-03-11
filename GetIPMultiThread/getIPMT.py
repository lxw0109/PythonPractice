#!/usr/bin/python2.7
#File: getIPMT.py
#Author: lxw
#Time: 2015-03-11

import socket
from MyThread.myThread import MyThread
import threading
from time import sleep
import traceback

def getIPMT(hostname):
    try:
        localIP = socket.gethostbyname(hostname)
        sleep(5)
        return "Hostname: {0}\t IP: {1}\n".format(hostname, localIP)
    except Exception, e:
        print hostname
        #print traceback.format_exc()

def main():
    #limit the total number of threads to 50.
    threadingNum = threading.Semaphore(50)
    #print(type(threadingNum)) #<threading._Semaphore>
    threads = []
    with open("hosts") as f:
        while 1:
            hostname = f.readline().strip()
            if not hostname:
                break
            mt = MyThread(getIPMT, (hostname,), threadingNum)
            threads.append(mt)

    for thread in threads:
        thread.start()

    with open("./result", "a") as f:
        for thread in threads:
            thread.join()
            f.write(thread.getResult())

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
