#!/usr/bin/python
import socket
import sys
if len(sys.argv) != 3:
 print("Usage: vrfy.py <filename> <ip>")
 sys.exit(0)
 
a = open(sys.argv[1], 'r')
names = a.read()

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server
connect = s.connect((sys.argv[2],25))
# Receive the banner
banner = s.recv(1024)
print(banner)

for name in names.split():
	print('Testing for: ', name)
	# VRFY a user
	s.send(('VRFY ' + name + '\r\n').encode())
	result = s.recv(1024)
	print(result, '\n')	
 


# Close the socket
s.close()
