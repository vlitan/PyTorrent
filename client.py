# client.py
import socket
import json
from pprint import pprint

#load config
with open('sysConfig.json') as data_file:
    sysConfig = json.load(data_file)

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "10.142.0.3"

port = sysConfig['serverPort']

# connection to hostname on the port.
s.connect((host, port))
s.send('{"request":"send","sender":"me","reveicer":"him"}');
# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
