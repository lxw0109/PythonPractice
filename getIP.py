#!/usr/bin/python2.7
#File: getIP.py
#Author: lxw
#Time: 2015-03-11

import socket
from time import sleep
import traceback

def getIP(hostname):
    try:
        localIP = socket.gethostbyname(hostname)
        sleep(1)
        return "Hostname: {0}\t IP: {1}\n".format(hostname, localIP)
    except Exception, e:
        print hostname
        #print traceback.format_exc()

def main():
    with open("hosts") as f:
    #with open("newHost") as f:
        with open("./result", "a") as f1:
            while 1:
                hostname = f.readline().strip()
                if not hostname:
                    break
                content = getIP(hostname)
                if content:
                    f1.write(content)
                    f1.flush()


if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
