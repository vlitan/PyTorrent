#!/usr/bin/python
# peer.py
import socket
import json
import time
import sys

from scSocket import serverSocket
from scSocket import clientSocket

#load config
with open('sysConfig.json') as data_file:
    sysConfig = json.load(data_file)

def requestHandler(addr, req):
    print("[serverSocket] accepted request from %s: %s" % (str(addr), str(req)))
    return ("Got request")

if (len(sys.argv) > 1):
    if (sys.argv[1] == "server"):
        server = serverSocket(sysConfig["serverPort"])
        server.run(requestHandler, 1)
    elif (sys.argv[1] == "client"):
        client = clientSocket(socket.gethostname(), sysConfig["serverPort"])
    #    client.connect()
        print (client.makeRequest("biiiaitch"))
        client.close()
else:
    print (sysConfig["usage"])
