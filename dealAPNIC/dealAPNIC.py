#!/usr/bin/python
#File: dealAPNIC.py
#Author: lxw
#Time: 2014-08-09
#Instruction:Count the number of the IPv4 addresses of each country listed.
#            Count the number of the addresses which belong to class C.

import sys
import os.path
import fileinput
import traceback

def main():
    if len(sys.argv) != 2:
        print 'Usage: "python fileName dataFile"'
        sys.exit(0)
    elif not os.path.isfile(sys.argv[1]):
        print "You've input an illegal fileName."
        print 'Usage: "python fileName dataFile"'
        sys.exit(0) 

    try:
        ipAmount = {}
        #for lineContent in fileinput.input(sys.argv[1], "r"):
        for lineContent in fileinput.input(sys.argv[1]):
            process(lineContent, ipAmount)

        num = raw_input("Order by which column?(1 or 2) ")
        if num == "1":
            for item in sorted(ipAmount.keys()):
                print "{0:<10}{1:<20}{2:<20}".format(item, ipAmount[item], ipAmount[item]/256)
        elif num == "2":
            templist = sorted(ipAmount.iteritems(), key = lambda x:x[1], reverse=True)   #list
            for item in templist:
                print "{0:<10}{1:<20}{2:<20}".format(item[0], ipAmount[item[0]], ipAmount[item[0]]/256)

    except Exception, e:
        print "NOTE: Exception --> " + str(e)
        traceback.print_exc() 


def process(line, Amount):
    lineList = line.split("|")
    if len(lineList) < 2:
        return

    if lineList[2] == "ipv4":
        if len(lineList[1]) == 2:
            if not Amount.get(lineList[1]):
                Amount[lineList[1]] = int(lineList[4])
            else:
                Amount[lineList[1]] += int(lineList[4])


if __name__ == "__main__":
    main()
