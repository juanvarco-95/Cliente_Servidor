#Import
import zmq
import hashlib
import os

#Socket
context = zmq.Context()
print("Conectando con el servidor de archivos…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

ps = (1024*4096)
file = "File"
len = os.path.getsize(file)

cont=0
#Imprime el Hash
def hash(files):
    files_hash = hashlib.sha1()
    with open(files, 'rb') as f:
        fb = f.read()
        while len(fb) > 0:
            files_hash.update(fb)
            fb = f.read()
    print (files_hash.hexdigest())



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
