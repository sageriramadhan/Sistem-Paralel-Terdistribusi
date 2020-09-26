#!/usr/bin/env python3.7

# rpc_server.py

# Fix missing module issue: ModuleNotFoundError: No module named 'SimpleXMLRPCServer'
#from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

import os

# Put in your server IP here
IP='127.0.0.1'
PORT=64001

server = SimpleXMLRPCServer((IP, PORT))

def server_receive_file(arg, filename):
    curDir = os.path.dirname(os.path.realpath(__file__))
    output_file_path = curDir + '/' + filename
    print('output_file_path -> ({})'.format(output_file_path))
    with open("hasil_diupload.txt", "wb") as handle:
        handle.write(arg.data)
        print('Output file: {}'.format(output_file_path))
        return True

server.register_function(server_receive_file, 'server_receive_file')
print('Control-c to quit')
server.serve_forever()