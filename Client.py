
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Conectando con el servidor aritmetico…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Enviando operación %s …" % request)
    op = b'3 * 2'
    #socket.send(b'3')
    socket.send(op)

    #  Get the reply.1
    message = socket.recv()
    print("Respuesta recibida %s [ %s ]" % (request, message))
