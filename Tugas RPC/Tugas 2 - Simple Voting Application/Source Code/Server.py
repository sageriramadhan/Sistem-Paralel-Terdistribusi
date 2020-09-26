# import SimpleXMLRPCServer
# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Buat server
with SimpleXMLRPCServer(("10.30.40.72", 8008), requestHandler=RequestHandler, allow_none=True) as server_side:
    server_side.register_introspection_functions()

    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    data = []
    data.append(dict({'name': 'Jokowi', 'vote': 0}))
    data.append(dict({'name': 'Prabowo', 'vote': 0}))

    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()

    #  buat fungsi bernama vote_candidate()
    def vote_candidate(x):

        # critical section dimulai harus dilock
        lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan  nilai votenya
        n = [n for n in data if n['name'] == x]
        if (n != []): n[0]['vote'] += 1
        # critical section berakhir, harus diunlock
        lock.release()
    # register fungsi vote_candidate() sebagai vote
    server_side.register_function(vote_candidate, 'vote')
    # buat fungsi bernama querry_result
    def querry_result():
        # critical section dimulai/
        lock.acquire()
        # hitung total vote yang ada
        total = 0
        for x in data:
            total += x['vote']
        # hitung hasil persentase masing-masing kandidat
        hasil = []
        for x in data:
            percent = str(x['vote'] / total * 100) + '%'
            hasil.append(dict({'name': x['name'], 'percentage': percent}))
        # critical section berakhir
        lock.release()
        return hasil
    # register querry_result sebagai querry
    server_side.register_function(querry_result, 'querry')
    print("Server voting sedang berjalan...")
    # Jalankan server
    server_side.serve_forever()
