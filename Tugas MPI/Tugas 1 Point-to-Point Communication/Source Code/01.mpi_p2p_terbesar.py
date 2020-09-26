# import mpi4py
from mpi4py import MPI
# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()


temp = 0
# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == (size-1):
	data = "Hai Rank : "
	j = 1
	for i in range(size-1):
		temp = rank-j
		#print(temp)
		comm.send(data, dest=temp)
		j += 1 

# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
	data = comm.recv(source=4)
	print(data,rank)
	
