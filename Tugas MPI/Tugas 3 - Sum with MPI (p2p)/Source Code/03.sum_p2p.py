# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random as rd

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
angka = rd.randint(1,100)
print("Hasil Random: ",angka)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    total = angka    
    for i in range(1,size):
        total += comm.recv(source=i)
    print("Total jumlah yang didapat rank %s adalah %d: " %(rank,total))
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    print("Sending %s dari %d" % (angka,rank))
    comm.send(angka,dest=0)
	
