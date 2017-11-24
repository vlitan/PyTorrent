# scSocket.py
import socket
import json
import time
import threading

class serverSocket(threading.Thread):
    """docstring for serverSocket."""

    def bind(self):
        print ("[serverSocket] bind")
        self.socket.bind((self.host, self.port))
        pass

    def listen(self, reqNb):
        print("[serverSocket] listen")
        self.socket.listen(reqNb)
        pass

    def accept(self, requestHandler):
        print("[serverSocket] accept")
        req = self.clientsocket.recv(1024)
        self.clientsocket.send(requestHandler(self.clientaddr, req))
        #self.clientsocket.close()
        pass

    def run(self):
        self.listen(self.reqNb)
        self.running = True
        print("[serverSocket] started running")
        self.clientsocket,self.clientaddr = self.socket.accept()
        while self.running == True:
            self.accept(self.requestHandler)
            time.sleep(0)
        pass
    def kill(self):
        self.running = False
        print("[serverSocket] killed")
        pass
    def __init__(self, port, requestHandler, reqNb):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = socket.gethostname()
        self.port = port
        self.requestHandler = requestHandler
        self.reqNb = reqNb
        self.bind()
        print("[serverSocket] created!")


class clientSocket(object):
    """docstring for clientSocket."""
    def connect(self, host, port):
        errno = self.socket.connect_ex((host, port))
        print("[clientSocket] connected to host: %s\tport: %s\terrno:%s" % (str(host), str(port), str(errno)) )
        pass

    def makeRequest(self, request):
        print("[clientSocket] makeRequest")
        self.socket.send(request)
        return self.socket.recv(1024)

    def close(self):
        print("[clientSocket] close")
        self.socket.close()
        pass

    def __init__(self):
        super(clientSocket, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[clientSocket] created!")
