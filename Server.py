from audioop import ratecv
import socket
IP = socket.gethostbyname(socket.gethostname())
GRSIZE = 1024
print ("la ip es: ",IP)
Port = 8000
Server = socket.socket()
Server.bind((IP,Port))
Server.listen()
print ("Server en linea")
conn,addr = Server.accept()
print (f"cliente conectado en {addr}")
while True:
   
    msgprev = conn.recv (1024).decode('utf-8')
    msgprevlen = int(len(msgprev))
    msgref = conn.recv (msgprevlen)
    msgref = msgref.decode('utf-8')
    
    print ("el cliente dice : ",msgref)
    