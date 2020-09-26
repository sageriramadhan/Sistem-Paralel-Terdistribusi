import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.1.1:8001')
with open("hasil_download.txt", "wb") as handle:
    filedata = s.download()
    handle.write(filedata.data)

