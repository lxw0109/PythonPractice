#!/usr/bin/python2.7
#File: calculateTotalLines.py
#Author: lxw
#Time: 2015-01-28
#Usage: Calculate the total lines of the specific Directory(Current working directory as default).

import os
import sys

def main(directory):
    count = 0
    for dirPath, dirNames, fileNames in os.walk(directory):
        for fileName in fileNames:
            with open(dirPath+os.sep+fileName) as f:
                while 1:
                    string = f.readline()
                    if not string:
                        break
                    count += 1
    if directory == ".":
        print("The number of lines in all files in current direcotry is {0}!".format(count))
    else:
        print("The number of lines in all files in direcotry \"{0}\" is {1}!".format(directory, count))



if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main(".")
else:
    print("Being imported as a module.")

