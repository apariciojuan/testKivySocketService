import socketserver
import threading
import time

class MiTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data= ""
        while data != "salir":

            print(self.request.recv(1024))
            data = input("Semi_Shell>> ")
            print(data)
            self.request.send(data.encode('utf-8'))

class ThreadServer(socketserver.ThreadingMixIn, socketserver.ForkingTCPServer):
    pass

def main():
    host = ""
    port= 33423
    server = ThreadServer((host,port), MiTcpHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print("corriendo")

main()



