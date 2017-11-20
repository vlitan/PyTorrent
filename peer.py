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
        connected = False
        pass
    def killServer(self):
        self.server.kill()
        pass
    def connect(self, host, port):
        self.client.connect(host, port)
        self.connected = True
        pass
    def makeRequest(self, request):
        if (self.connected == False):
            self.connect(self.destHost, destPort)
        return self.client.makeRequest(request)

    def __init__(self, destHost, serverPort, requestHandler, nbReq):
        super(peer, self).__init__()
        self.server = serverSocket(serverPort, requestHandler, nbReq)
        self.destHost = destHost
        self.client = clientSocket()
        self.connected = False


def requestHandler(addr, req):
    print("I GOT AS REQUEST > %s\n" % (str(req)))
    return ("RESPONSE")


if (len(sys.argv) > 2):
    hostPort = int(sys.argv[1])
    destPort = int(sys.argv[2])
    peer = peer(socket.gethostname(), hostPort, requestHandler, 5)
    peer.startServer()
    stop = 0
    while stop != 1:
        text = raw_input("I SAY > ")
        if (text == "stop"):
            stop = 1
            peer.killServer()
        else:
            print ("I GOT AS RESPONSE > %s\n" % (peer.makeRequest(text)))
else:
    print (sysConfig["usage"])
