import zmq
import os
import hashlib

#Contadores
c1 = 0
c2 = 0
c3 = 0


#Socket Servidor 1
contextS1 = zmq.Context()
socketS1 = contextS1.socket(zmq.REP)
socketS1.bind("tcp://*:5555")

#Socket Cliente 1 Servidor 1
contextC11 = zmq.Context()
socketC11 = contextC11.socket(zmq.REQ)
socketC11.connect("tcp://localhost:5558")

#Socket Cliente 1 Servidor 2
contextC12 = zmq.Context()
socketC12 = contextC12.socket(zmq.REQ)
socketC12.connect("tcp://localhost:5559")

#Socket Cliente 1 Servidor 3
contextC13 = zmq.Context()
socketC13 = contextC13.socket(zmq.REQ)
socketC13.connect("tcp://localhost:5560")


#Socket Servidor 2
contextS2 = zmq.Context()
socketS2 = contextS2.socket(zmq.REP)
socketS2.bind("tcp://*:5556")

#Socket Cliente 2 Servidor 1
contextC21 = zmq.Context()
socketC21 = contextC21.socket(zmq.REQ)
socketC21.connect("tcp://localhost:5558")

contextC22 = zmq.Context()
socketC22 = contextC22.socket(zmq.REQ)
socketC22.connect("tcp://localhost:5559")

contextC22 = zmq.Context()
socketC22 = contextC22.socket(zmq.REQ)
socketC22.connect("tcp://localhost:5560")


#Socket Servidor 3
contextS3 = zmq.Context()
socketS3 = contextS3.socket(zmq.REP)
socketS3.bind("tcp://*:5557")



ps = (1024*1024)
mensaje = "Recibido correctamente"
file = 'File'
c1 = 0
nf1 = 0

#Imprime el Hash del archivo
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



def proxy(socket_c,name):
    c1 = 0
    nf1 = 0
    while True:
        message = socket_c.recv()
        nombre = name + str(c1) + ".part"
        f = open(nombre, "wb+")
        f.write(message)
        f.close()
        socket_c.send(mensaje.encode("utf-8"))
        c1 = c1 + 1
        nf1 = c1 - 1
        if nf1 % 3 == 0:
            print(nf1)
            nombre = name + str(nf1) + ".part"
            a = open(nombre,'rb')
            while True:
                arc = a.read(ps)
                if not arc:
                    break
                socketC11.send(arc)
            #    hash(arc)
                print("Se envió archivo correctamente al servidor 1")
                message = socketC11.recv()
            a.close()
        if nf1 % 3 == 1:
            print(nf1)
            nombre = name + str(nf1)+".part"
            a = open(nombre,'rb')
            while True:
                arc = a.read(ps)
                if not arc:
                    break
                socketC12.send(arc)
            #    hash(arc)
                print("Se envió archivo correctamente al servidor 2")
                message = socketC12.recv()
            a.close()
        if nf1 % 3 == 2:
            print(nf1)
            nombre = name + str(nf1) + ".part"
            a = open(nombre,'rb')
            while True:
                arc = a.read(ps)
                if not arc:
                    break
                socketC13.send(arc)
            #    hash(arc)
                print("Se envió archivo correctamente al servidor 3")
                message = socketC13.recv()
            a.close()

proxy(socketS1, "Mi_archivo")
proxy(socketS2, "Segundo")
##########################################################################
