# scSocket.py
import socket
import json
import time
import threading

class serverSocket(threading.Thread):
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

    def run(self, requestHandler, reqNb):
        self.listen(reqNb)
        while True:
            self.accept(requestHandler)
        pass
    def __init__(self, port):
        super(serverSocket, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port
        self.bind()

class clientSocket(object):
    """docstring for clientSocket."""
    def connect(self):
        self.socket.connect((self.host, self.port))
        print("[clientSocket] connected to host: %s\tport: %s" % (str(self.host), str(self.port)) )
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
        print("[clientSocket] created!")
