import socket
port = 50000
s = socket.socket()
host = "10.30.40.46"
s.bind((host, port))
s.listen(5)

while True:
    conn, addr = s.accept()
    print ('Mendapatkan Koneksi dari', addr)
    data = conn.recv(1024)
    print(b'Client mengirim pesan ke server : ' ,repr(data))
    filename='file_didownload.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Client Sedang Download Data : ',repr(l))
       l = f.read(1024)
    f.close()
    print('Client Berhasil Download')
    conn.close()