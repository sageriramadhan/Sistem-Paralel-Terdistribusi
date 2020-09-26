import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "10.30.40.46"  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send(b"HALO SERVER!")

with open('hasil_didownload.txt', 'wb') as f:
    print ('Berkas Terbaca')
    while True:
        print('Menerima Data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)
f.close()
print('Unduhan Berhasil')
s.close()
print('Koneksi ditutup')