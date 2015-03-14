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
        return "{0},{1}\n".format(hostname, localIP)
    except Exception, e:
        return hostname + "\n"

def main():
    with open("hosts") as f:
        with open("./result.csv", "w") as f1:
            while 1:
                hostname = f.readline().strip()
                if not hostname:
                    break
                content = getIP(hostname)
                f1.write(content)
                f1.flush()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
