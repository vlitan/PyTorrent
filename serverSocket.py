# serverSocket.py

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
        #clientsocket.close()
        pass

    def __init__(self, port):
        super(serverSocket, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port
