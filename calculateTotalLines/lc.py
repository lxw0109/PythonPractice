#!/usr/bin/python3
#File: lc.py
#Author: lxw
#Time: 2016-05-11
#Usage: Calculate the total lines of the specific Directory(Current working directory as default).

import os
import sys

def main(directory):
    count = 0
    for dirPath, dirNames, fileNames in os.walk(directory):
        for fileName in fileNames:
            try:
                #-e(--extension)
                if fileName.endswith(".java"):
                    with open(dirPath + os.sep + fileName, "rU") as f:
                        while 1:
                            string = f.readline()
                            if not string:
                                break
                            count += 1
            except Exception as e:
                print("---------Exception-----:\n\t" + str(e))

    if directory == ".":
        print("Result:\n  The number of lines in all files in current direcotry is {0}!".format(count))
    else:
        print("Result:\n  The number of lines in all files in direcotry \"{0}\" is {1}!".format(directory, count))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: lc [DIR]\nYou did not specify \"[DIR]\", the program takes the current working directory(\".\") as the default value of [DIR]\n\n")
        main(".")
else:
    print("Being imported as a module.")
