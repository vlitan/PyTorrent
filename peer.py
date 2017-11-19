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

class peer(object):
    """docstring for peer."""
    def startServer(self):
        self.server.start()
        pass
    def connect(self, host, port):
        self.client.connect(host, port)
        pass
    def makeRequest(self, request):
        self.client.makeRequest(request)
        pass
    def __init__(self, serverHost, serverPort, requestHandler, nbReq):
        super(peer, self).__init__()
        self.server = serverSocket(serverPort, requestHandler, nbReq)
        self.client = clientSocket()


def requestHandler(addr, req):
    print("SHE SAID > %s" % (str(req)))
    return ("(ac) if you say so")


if (len(sys.argv) > 2):
    hostPort = int(sys.argv[1])
    destPort = int(sys.argv[2])
    peer = peer(socket.gethostname(), hostPort, requestHandler, 1)
    peer.startServer()
    while True:
        text = raw_input("I SAY > ")
        peer.connect(socket.gethostname(), destPort)
        print ("SHE SAID > %s" % (peer.makeRequest(text)))
else:
    print (sysConfig["usage"])
