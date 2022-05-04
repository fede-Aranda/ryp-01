import socket
from turtle import delay
IP = socket.gethostbyname(socket.gethostname())
GRSIZE = 1024
PORT = 8000
client = socket.socket()
client.connect((IP,PORT))
while True:
    msg = input ("ingrese un mensaje : ")
    msg = msg.encode('utf-8')
    lenmsg = str(len(msg)).encode('utf-8')
    llenmsg = len(lenmsg)
    msg2 = str (lenmsg + b" " * (GRSIZE-llenmsg))
    msg2 = msg2.encode('utf-8')
    client.send(msg2)
    client.send(msg)
