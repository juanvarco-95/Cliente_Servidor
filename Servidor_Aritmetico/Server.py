

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

resultado = 0
while True:
    #  Wait for next request from client
    message = socket.recv()
    message = message.decode('utf-8')
    res = message.split()

    if(res[1] == '+'):
        resultado = int(res[0]) + int(res[2])
        print(resultado)
    if(res[1] == '-'):
        resultado = int(res[0]) - int(res[2])
        print(resultado)
    if(res[1] == '*'):
        resultado = int(res[0]) * int(res[2])
        print(resultado)
    if(res[1] == '/'):
        resultado = int(res[0]) / int(res[2])
        print(resultado)
    resultado = str(resultado)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(resultado.encode('utf-8'))
    print("Recibiendo operacion: %s" % message)
