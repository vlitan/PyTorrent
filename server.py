# server.py
import socket
import time
import json

#load config
with open('sysConfig.json') as data_file:
    sysConfig = json.load(data_file)

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = sysConfig['serverPort']

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    req = json.loads(clientsocket.recv(1024))
    print("got a request from %s : %s from %s to %s" % (str(addr), str(req['request']), str(req['sender']), str(req['reveicer'])))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
