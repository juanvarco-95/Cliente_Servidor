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

ps = (1024*1024)
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
    nombre = "filepart"+str(cont)+".hash"
    if not arc:
        break

    socket.send(arc)
    message = socket.recv()
    archivo2=open(nombre,"wb+")
    archivo2.write(arc)
    archivo2.close
    cont=cont+1
print("Respuesta recibida [ %s ]" % (message))
#hash(file)


    #a.close()
