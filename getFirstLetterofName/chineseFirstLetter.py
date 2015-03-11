#!/usr/bin/python
#coding:utf-8
#File: chineseFirstLetter.py
#Author: lxw
#Time: 2014-04-25
#Usage: 输入一个名字，得到其姓氏的声母(首字母).
'''
现在这段只是好使的而已，但具体的编码unicode ascii gbk UTF-8之间的关系我还不懂，最近比较忙，还是先把我的作业做完在搞这个吧！
'''

import unicodedata
def getFirstLetter(firstName):
	#print repr(firstName)
	nameArr = firstName.encode('gbk')
	num1 = ord(nameArr[0])
	num2 = ord(nameArr[1])
	num = num1 * 256 + num2
	'''
	//table   of   the   constant   list 
	// 'A';           //45217..45252 
	// 'B';           //45253..45760 
	// 'C';           //45761..46317 
	// 'D';           //46318..46825 
	// 'E';           //46826..47009 
	// 'F';           //47010..47296 
	// 'G';           //47297..47613 
	// 'H';           //47614..48118 
	//没有I
	// 'J';           //48119..49061 
	// 'K';           //49062..49323 
	// 'L';           //49324..49895 
	// 'M';           //49896..50370 
	// 'N';           //50371..50613 
	// 'O';           //50614..50621 
	// 'P';           //50622..50905 
	// 'Q';           //50906..51386 
	// 'R';           //51387..51445 
	// 'S';           //51446..52217 
	// 'T';           //52218..52697 
	//没有U,V 
	// 'W';           //52698..52979 
	// 'X';           //52980..53640 
	// 'Y';           //53689..54480 
	// 'Z';           //54481..55289 
	'''

	# python 允许这种写法？
	if 45217 <= num <= 45252:
		return 'A'
	elif 45253 <= num <= 45760:
		return 'B'
	elif 45761 <= num <= 46317:
		return 'C'
	elif 46318 <= num <= 46825:
		return 'D'
	elif 46826 <= num <= 47009:
		return 'E'
	elif 47010 <= num <= 47296:
		return 'F'
	elif 47297 <= num <= 47613:
		return 'G'
	elif 47614 <= num <= 48118:
		return 'H'
	elif 48119 <= num <= 49061:
		return 'J'
	elif 49062 <= num <= 49323:
		return 'K'
	elif 49324 <= num <= 49895:
		return 'L'
	elif 49896 <= num <= 50370:
		return 'M'
	elif 50371 <= num <= 50613:
		return 'N'
	elif 50614 <= num <= 50621:
		return 'O'
	elif 50622 <= num <= 50905:
		return 'P'
	elif 50906 <= num <= 51386:
		return 'Q'
	elif 51387 <= num <= 51445:
		return 'R'
	elif 51446 <= num <= 52217:
		return 'S'
	elif 52218 <= num <= 52697:
		return 'T'
	elif 52698 <= num <= 52979:
		return 'W'
	elif 52980 <= num <= 53640:
		return 'X'
	elif 53689 <= num <= 54480:
		return 'Y'
	elif 54481 <= num <= 55289:
		return 'Z'
	else:
		return NONE


def main():
	word = raw_input('请输入名字: ')
	uWord = word.decode('UTF-8')	# 'lxw'	or '刘晓伟'

	# Get the First Name.
	firstWord = uWord[0]	# 'l' or '刘'
	firstWordStr = repr(firstWord)	# u'l' or u'刘'
	#print(len(firstWord))	# 1
	#print(len(firstWordStr))	# 4(u'l') or 9(u'\u5218')
	#print(str(firstWord))	#UnicodeEncodeError: 'ascii' codec can't encode character u'\u4e86' in position 0: ordinal not in range(128)

	result = ''
	if len(firstWordStr) == 4:	# not Chinese
		result = firstWord.upper()
	elif len(firstWordStr) == 9:	# Chinese
		result = getFirstLetter(firstWord)
	else:
		print('Your input is neither Chinese nor English, or something else happened. System Exit!')
		exit(0)

	if not result:
		print('Something wrong has happened. System Exit!')
	print('The first LETTER of your name is {0}'.format(result))


if __name__ == '__main__':
	main()
