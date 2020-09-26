import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "127.0.0.1"
hostPort = 8080

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		self.path = '/index.html'
		file_to_open = open(self.path[1:]).read()
		self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, "utf-8"))

	#	POST is for submitting data.
	def do_POST(self):
		print( "incomming http: ", self.path )
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		client.close()
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
myServer.serve_forever()