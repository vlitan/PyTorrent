# peer.py
import socket
import json

class serverSocket(object):
    """docstring for serverSocket."""
    def host():
        doc = "The host property."
        def fget(self):
            return self._host
        def fset(self, value):
            self._host = value
        def fdel(self):
            del self._host
        return locals()
        host = property(**host())
    def port():
        doc = "The port property."
        def fget(self):
            return self._port
        def fset(self, value):
            self._port = value
        def fdel(self):
            del self._port
        return locals()
        port = property(**port())
    def socket():
        doc = "The socket property."
        def fget(self):
            return self._socket
        def fset(self, value):
            self._socket = value
        def fdel(self):
            del self._socket
        return locals()
        socket = property(**socket())

    def bind(self):
        socket.bind((host, port))
        pass

    def listen(self, reqNb):
        socket.listen(reqNb)
        pass

    def accept(self):
        clientsocket,addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        req = json.loads(clientsocket.recv(1024))
        print("got a request from %s : %s from %s to %s" % (str(addr), str(req['request']), str(req['sender']), str(req['reveicer'])))
        currentTime = time.ctime(time.time()) + "\r\n"
        clientsocket.send(currentTime.encode('ascii'))
        clientsocket.close()

        pass

    def __init__(self, port):
        super(serverSocket, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port

#load config
with open('sysConfig.json') as data_file:
    sysConfig = json.load(data_file)

server = serverSocket(sysConfig["serverPort"])
server.bind()
server.listen(5)

while True:
    server.accept()
