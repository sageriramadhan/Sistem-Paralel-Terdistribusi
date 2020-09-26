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

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
total = comm.reduce(angka, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank==0:
    print(total)

