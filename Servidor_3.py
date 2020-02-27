#Basado en: https://recursospython.com/codigos-de-fuente/enviar-archivo-via-socket/
#import
import zmq
import os
import hashlib

#Socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5560")
c1 = 2
nf1 = c1 - 1
m1 = "Recibido correctamente"
#file = 'File'

def hash(filename):
    sha1 = hashlib.sha1()
    with open (filename, 'rb') as f:
        while True:
            data = f.read(Size)
            if not data:
                break
                sha1.update(data)
    return sha1.hexdigest()

def hashPart(bytes):
    sha1 = hashlib.sha1()
    sha1.update(bytes)
    return sha1.hexdigest()

def splitFile(filename):
    with open(filename, 'rb') as f:
        while True:
            data = f.read(ps)
            if not data:
                break
            partName = hashPart(data)
            with open(partName, 'wb') as p:
                p.write(data)

while True:

    message = socket.recv()
    nombre = "archivo" + str(c1) + ".part"
    f = open(nombre, "wb+")
    f.write(message)
    print("Se recibió archivo correctamente")
    #hash(file)
    f.close()
    socket.send(m1.encode("utf-8"))
    #c1=c1+3
    c1 = c1 + 3
