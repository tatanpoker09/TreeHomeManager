import socket
import threading

import time

from kivy.app import App

from main.GUI.loginscreen.LoginScreen import LoginScreen


class ThreadedClient(object):
    def __init__(self, host, port):
            self.host = host
            self.port = port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        try:
            self.sock.connect((self.host, self.port))
            thread1 = threading.Thread(target=self.listenServer(), args=[self])
            thread1.start()
        except ConnectionRefusedError:
            print("Couldn't connect to the specified server!")
            self.sock.close()


    def listenServer(self):
        chunks = []
        MSGLEN = 1024
        bytes_recd = 0
        data = self.sock.recv(1024)
        print("Data: '"+data.decode()+"'")

    def parseResponse(self, response):
        if(response=="connected"):
            App.get_running_app().sm.switch_to(LoginScreen(name="loginscreen"))