#Import
import zmq
import hashlib
import os

#Socket
context = zmq.Context()
print("Conectando con el servidor de archivos…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

ps = (1024*1024)
file = "File"
len = os.path.getsize(file)

cont=0
#Imprime el Hash


print("Enviando archivo …")
a = open("File", "rb") #rb = Leer binario
#Enviar Archivo
while True:
    arc = a.read(ps)
    if not arc:
        break
    socket.send(arc)
    message = socket.recv()

print("Respuesta recibida [ %s ]" % (message))
#hash(file)


    #a.close()
