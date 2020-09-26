import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.30.40.46', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = ('MENERIMA INFORMASI DARI SEVER\n')
    if not data:
        break
    conn.sendall(data.encode('utf-8'))
    print ('DATA TELAH TERKIRIM KE CLIENT')
conn.close()