# PROJECT 1 
# Name: Jaideep Singh Kainth
# ID: 1001508330
#
# Filename: Server.py
# Description: This script has a multithreaded server that connects with multiple clients at same time through a socket
# 
# Citations:
#       1. Skeleton Code from :
#           Blackboard
# 
#       2. MultiThreaded part:
#           https://stackoverflow.com/questions/38958233/the-requested-address-is-not-valid-in-its-context-error
#-----------------------------------------------------------------------------------------------------------------------------
import socket 
import sys
import time
import os

def Main():
	thisPath = os.path.dirname(os.path.abspath(__file__))
	ip=sys.argv
	host = ip[1]
	port = int(ip[2])
	#Checks if page is specified or not
	if len(sys.argv)==4:
		filename=ip[3]
	else:
		filename='/'
	path=r"GET /"+thisPath+"\\"+filename
	# create a socket object
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# connect to the server
	clientSocket.connect((host, port))
	try:
		print("Received Data:\n\n")
		start_time = time.time()
		clientSocket.sendall( path.encode('utf-8'))
		while True:
			data = clientSocket.recv(4096)
			print(data.decode())
			# when to break connection
			if data.endswith(b'</html>') or data.endswith(b'404 Not Found\n\n'):
				break
		end_time = time.time()
		RTT=end_time - start_time
		print("RTT : %s"%RTT)
		print("Host : %s"%host)
		print("Port Number : %s"%port)
		print("Socket Details : %s"%clientSocket)
	finally:
		clientSocket.close() 
if __name__ == '__main__':
	Main()