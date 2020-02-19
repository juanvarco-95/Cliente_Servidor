#Basado en: https://recursospython.com/codigos-de-fuente/enviar-archivo-via-socket/
#import
import zmq
import os
import hashlib

#Socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

mensaje = "Recibido correctamente"
file = 'File'

#Imprime el Hash del archivo
def hash(files):
    files_hash = hashlib.sha1()
    with open(files, 'rb') as f:
        fb = f.read()
        while len(fb) > 0:
            files_hash.update(fb)
            fb = f.read()
    print (files_hash.hexdigest())

while True:
    message = socket.recv()

    f = open("File", "wb")
    f.write(message)
    print("Se recibió archivo correctamente")
    hash(file)
    f.close()

    socket.send(mensaje.encode("utf-8"))
