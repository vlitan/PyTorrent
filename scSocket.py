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

    def run(self):
        self.listen(self.reqNb)
        self.running = True
        print("[serverSocket] started running")
        while self.running == True:
            self.accept(self.requestHandler)
        pass
    def kill(self):
        self.running = False
        pass
    def __init__(self, port, requestHandler, reqNb):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port
        self.requestHandler = requestHandler
        self.reqNb = reqNb
        self.bind()
        print("[serverSocket] created!")


class clientSocket(object):
    """docstring for clientSocket."""
    def connect(self, host, port):
        self.socket.connect((host, port))
        print("[clientSocket] connected to host: %s\tport: %s" % (str(host), str(port)) )
        pass

    def makeRequest(self, request):
        self.socket.send(request)
        return self.socket.recv(1024)

    def close(self):
        self.socket.close()
        pass

    def __init__(self):
        super(clientSocket, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[clientSocket] created!")
