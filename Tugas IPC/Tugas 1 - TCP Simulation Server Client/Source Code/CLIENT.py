import socket

HOST = '10.30.40.46'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    print (data.decode('utf-8'))

s.close()
