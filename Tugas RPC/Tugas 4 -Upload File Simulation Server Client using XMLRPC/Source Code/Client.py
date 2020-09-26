### rpc_client.py
#!/usr/bin/env python3.7

import os


# client.py
import sys

# The answer is that the module xmlrpc is part of python3

import xmlrpc.client

#Put your server IP here
IP='10.30.40.15'
PORT=64001


url = 'http://{}:{}'.format(IP, PORT)
###server_proxy = xmlrpclib.Server(url)
client_server_proxy = xmlrpc.client.ServerProxy(url)

curDir = os.path.dirname(os.path.realpath(__file__))
filename = "file_diupload.txt"
filename_fortarget = "hasil_diupload.txt"
fpn = curDir + '/' + filename
print(' filename -> ({})'.format(filename))
print(' fpn -> ({})'.format(fpn))
if not os.path.exists(fpn):
    print('Missing file -> ({})'.format(fpn))
    sys.exit(1)

with open(fpn, "rb") as handle:
    binary_data = xmlrpc.client.Binary(handle.read())
    client_server_proxy.server_receive_file(binary_data, filename)