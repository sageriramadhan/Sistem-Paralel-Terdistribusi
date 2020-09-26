import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://127.0.0.1:8008')

print("Uji Voting Pertama")
print("==================")
s.vote('Jokowi')
s.vote('Prabowo')
print(s.querry())
print("")

print ("Uji Voting Kedua")
print("==========")
s.vote('Jokowi')
s.vote('Jokowi')
s.vote('Prabowo')
s.vote('Prabowo')
print(s.querry())
print("")

