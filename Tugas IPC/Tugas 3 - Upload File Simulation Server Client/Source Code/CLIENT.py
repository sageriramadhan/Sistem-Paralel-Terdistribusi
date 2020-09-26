import socket
port = 50000
s = socket.socket()
host = "10.30.40.46"
s.bind((host, port))
s.listen(5)

print ('Server listening....')
while True:
    conn, addr = s.accept()
    print ('Mendapatkan Koneksi dari', addr)
    data = conn.recv(1024)
    print(b'Server menerima data : ' ,repr(data))
    filename='file_diupload.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Mengunggah Data : ',repr(l))
       l = f.read(1024)
    f.close()
    print('Unggah Berhasil')
    conn.close()