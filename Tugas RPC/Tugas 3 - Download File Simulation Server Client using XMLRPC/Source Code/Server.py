from xmlrpc.server import SimpleXMLRPCServer

# import xmlrpc bagian client
import xmlrpc.client

def file_download():
    with open("file_didownload.txt", 'rb') as handle:
        return xmlrpc.client.Binary(handle.read())

with SimpleXMLRPCServer(("10.30.40.72", 8001)) as server:
    server.register_introspection_functions()
    print("Server mendengarkan port 8001")
    server.register_function(file_download, 'download')
    server.serve_forever()
