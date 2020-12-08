import http.server
import socketserver

# https://https://www.afternerd.com/blog/python-http-server/#what-is-web-server
# Display the webpage http://localhost:8080/index.html
PORT = 8080

#This handler serves files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

#The socket.server.TCPServer class
#Listens for any ip address "" on port 8080

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
