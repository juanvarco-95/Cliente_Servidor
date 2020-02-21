#Basado en: https://recursospython.com/codigos-de-fuente/enviar-archivo-via-socket/
#Import
import zmq
import hashlib
import os

#Socket
context = zmq.Context()
print("Conectando con el servidor de archivos…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

ps = 12*1024
file = "File"
len = os.path.getsize(file)

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
#Enviar Archivo
for i in range(ps,len,ps):

    a = open("File", "rb") #rb = Leer binario
    arc = a.read(i)

    #while arc:
    socket.send(arc)
    #arc = a.read(Chunk)

    message = socket.recv()
    print("Completando... ", i,  "de" , len)
print("Respuesta recibida [ %s ]" % (message))
hash(file)


    #a.close()
