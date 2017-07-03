import socket
import threading

class ThreadedClient(object):
    def __init__(self, host, port):
            self.host = host
            self.port = port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        try:
            self.sock.connect((self.host, self.port))
            threading.Thread(target=self.listenServer()).start()
        except ConnectionRefusedError:
            print("Couldn't connect to the specified server!")
            self.sock.close()
            # TODO Open a popup here.


    def listenServer(self):
        size = 1024
        while True:
            try:
                data = self.sock.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    response = response.decode()
                    print("data: "+response)
                else:
                    raise ConnectionAbortedError('Client disconnected')
            except:
                self.sock.close()
                print("error, disconnecting.")
                return False