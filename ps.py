import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(4)

host = input("enter ip: ")
port = int(input("enter port number: "))

print ("Scanning the port..")

def portScanner(port):
	if s.connect_ex((host,port)):
		print ("the port " + str(port) + " in ip: " + str (host) + " is closed")
	else:
		print("the port " + str(port) + " in ip: " + str(host) + " is open")

portScanner(port)

