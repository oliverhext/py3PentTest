# https://asecuritysite.com/encryption/aes_modes
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

command='hello'
password='hello'
#ival=10


plaintext=command

def encrypt(plaintext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()
	
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)
print ("Input data (CMS): "+binascii.hexlify(plaintext.encode()).decode())

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
#ciphertext = binascii.hexlify(bytearray(ciphertext)).decode()
print("Cipher TExt",ciphertext)
#print ("Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext)).decode())

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
print("Before we remove the padding",plaintext)

plaintext = Padding.removePadding(plaintext.decode(),mode=0)
print ("  decrypt: "+plaintext)


