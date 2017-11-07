import socket
import os
#va a mandar mensajes al servidor
import time



def main():

    msj =""
    host, port = "remplazar por ip del servidor" , 33423

    #creo un socket y me conecto
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    sock.send("aca estoy")


    while True:
        sock.recv(1024)
        dato = "recibido"
        sock.send (dato.encode('utf-8'))
        time.sleep(1)

    sock.close() #recuerden cerrar el socket

if __name__ == '__main__':
    main()


