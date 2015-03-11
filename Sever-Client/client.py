#!/usr/bin/python
#coding:utf-8
#如果想有中文注释就必须得有上面的语句
#File: client.py
#Author: lxw
#Time: 2014-03-27
#Usage: Client.

import socket
import threading
import os.path
import string

def sendFile (soc, absolute):
	# get the filename.
	filename = os.path.basename(absolute)
	content = open(absolute).read()
	
	# send the length of the filename in front of filename
	#soc.sendall('FILE:' + str(len(filename)) + filename)
	
	soc.sendall('FILE:' + chr(len(filename)) + filename)
	print 'SEND FILE' + filename
	soc.sendall(content)
	soc.sendall('__ENDFILEFLAG__')
	

def getInput(soc, ): 	# tuple is essential.
	while True:
		words = raw_input()		
		if words.lower() == 'exit':
			soc.sendall(words)
			# Stop the thread. And stop the client.
			break
		# E.G.: 'FILE:/home/lxw/lxw0109/1.jpg'.	prefix is 'FILE:'
		elif words.startswith('FILE:'):
			absolute = words[5:].strip()
			if os.path.exists(absolute):
				sendFile(soc, absolute)
			else:
				errorInfo = 'Illegal file path.' 
				print errorInfo 
				soc.sendall(errorInfo)
		else:
			soc.sendall(words)
			
						

if __name__ == '__main__':
	HOST = '127.0.0.1'
	PORT = 10086
	
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	
	print '\n------------------- Client Run -------------------------'
	print 'Welcome to our group chat\nInput:'
	
	# words = raw_input('Input: ')
	# Create a new thread to get the input of the client AT ANY TIME.
	thread = threading.Thread(target = getInput, args = (s,))
	# NOTE： getInput method runs only ONCE.
	thread.start()
	
	while True:
		if not thread.isAlive():	# over
			break
		# NOTE: Receive 1024 each time, will this number cause disorder or sth? E.G.: *****  FILE:/home/lxw/1.jpg ******.
		data = s.recv(1024)
		if data:
			if data.strip().startswith('FILE:'):
				try:					
					# data == FILE:1.jpg????1kExif......   VERY LONG
					print 'GET FILE: '					
					filename = data[6:6 + ord(data[5])]
					saveName = thread.name + '_' + filename
					filenameTab = string.maketrans(string.punctuation + '-', '_' * (len(string.punctuation) + 1))
					saveName.translate(filenameTab)					
					print 'saveName is ' + saveName
					fd = open(saveName, 'w')
					content = data[(6 + ord(data[5])):]
					#NOTE-NOTE-NOTE-NOTE-NOTE-NOTE-NOTE:
					#CAN NOT BE LIKE THIS. if content is '', it will not get into the while cycle, and into the following else.
					#while content:
					while True:
						fd.write(content)
						content = s.recv(4096)
						'''
						# This method always show problems. 
						if not content:
							break
						'''
						if '__ENDFILEFLAG__' in content:
							# data is not changed in replace method
							content = content.replace('__ENDFILEFLAG__', '') 
							if not content:
								break
							else:
								fd.write(content)
								break
					print 'FILE RECEIVING FINISHED.'
										
				except:
					error = open('error_except.txt', 'w')
					error.write('error')
					error.close()
					print ' Exception.message-------->' + str(Exception.message)
				finally:					
					fd.close()					
			else:
				print data
	
	print 'Client is over'
	s.close()
