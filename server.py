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
from socket import *
import threading
import sys
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
host='127.0.0.1'
ip=sys.argv
if len(sys.argv)==2:
	port=int(ip[1])
else:
	port=8080
serverSocket.bind((host,port))
serverSocket.listen(5)
threadsclient = []
print ('Ready to serve...')
def Main(connectionSocket,addr):
	while True:
		try:
			message = connectionSocket.recv(1024)
			#Favicon.ico requests and empty requests from the browsers - the server takes any kind of requests from the client including favicon.ico requests (fake requests).
			if ((message).startswith(b'GET /favicon.ico')) or (message == b''):
				return
			print("Client Address :",addr)
			print("Socket Details :",connectionSocket)
			thisPath = os.path.dirname(os.path.abspath(__file__))
			fpath=message.split()[1]
			fpath=fpath.decode("utf-8")
			#Checks if page is not specified(then serves default page i.e index.html), otherwise serves requested page
			if (fpath[-1])=="/":
				filename=thisPath+"\\"+'index.html'
				f = open(filename[0:])
			else :
				filename = fpath
				f = open(filename[1:])
			outputdata = f.read()
			print(outputdata)
			#Send one HTTP header line into socket
			#Fill in start
			result = '\nHTTP/1.1 200 OK\n\n'
			connectionSocket.send(result.encode('utf-8'))
			print('Status: 200 OK. ')
			#Fill in end
			#Send the content of the requested file to the client
			connectionSocket.send(outputdata.encode('utf-8'))
			connectionSocket.close()
			print ('Next Request...')
		except IOError:
			#Send response message for file not found
			#Fill in start
			result = '\nHTTP/1.1 404 Not Found\n\n'
			connectionSocket.sendall(result.encode('utf-8'))
			print('Status: 404 Not Found. File not found.\n')
			#Fill in end
			#Close client socket
			#Fill in start
			connectionSocket.close()
			#Fill in end
		break
while True:
    # Threading Part
    connectionSocket, addr =  serverSocket.accept()
    threadsnew = threading.Thread(target = Main, args = (connectionSocket, addr))
    threadsclient.append(threadsnew)
    threadsnew.start()