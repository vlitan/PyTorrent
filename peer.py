# peer.py
import socket
import json
import time

class serverSocket(object):
    """docstring for serverSocket."""

    def bind(self):
        self.socket.bind((self.host, self.port))
        pass

    def listen(self, reqNb):
        self.socket.listen(reqNb)
        pass

    def accept(self, requestHandler):
        clientsocket,addr = self.socket.accept()
        req = clientsocket.recv(1024)
        clientsocket.send
        clientsocket.send(requestHandler(addr, req))
        clientsocket.close()
        pass

    def __init__(self, port):
        super(serverSocket, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port

class clientSocket(object):
    """docstring for clientSocket."""
    def connect(self, arg):
        self.socket.connect((self.host, self.port))
        pass

    def makeRequest(self, request):
        self.socket.send(request)
        return self.socket.recv(1024)

    def close(self):
        self.socket.close()
        pass

    def __init__(self, host, port):
        super(clientSocket, self).__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#load config
with open('sysConfig.json') as data_file:
    sysConfig = json.load(data_file)

server = serverSocket(sysConfig["serverPort"])
server.bind()
server.listen(2)

def requestHandler(addr, req):
    print("[serverSocket] accepted request from %s: %s" % (str(addr), str(req)))
    return ("response")

while True:
    server.accept(requestHandler)
