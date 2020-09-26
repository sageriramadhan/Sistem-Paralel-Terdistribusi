# import os, re dan threading
import os
import re
import threading

# import time
import time

# buat kelas ip_check
class ip_check(threading.Thread):
    
    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__ (self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.statusPing = -1
    
    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        ping_out = os.popen("ping -n 2 "+self.ip,"r")
        
        # loop forever
        while True:
            # baca hasil respon setiap baris
            line = ping_out.readline()
            
            # break jika tidak ada line lagi
            if not line: break
            
            # baca hasil per line dan temukan pola Received = x
            getLine = re.findall(received_pack,line)
            
            # tampilkan hasilnya
            if getLine:
                self.statusPing = int(getLine[0])


    # fungsi untuk mengetahui status; 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def status(self):
        if self.statusPing == 0:
            return 'tidak ada respon'           # 0 = tidak ada respon
        elif self.statusPing == 1:
            return 'ada loss'                   # 1 = ada loss
        elif self.statusPing == 2:
            return 'hidup'                      # 2 = hidup
        elif self.statusPing == -1:
            return 'seharusnya tidak terjadi'   # -1 = seharusnya tidak terjadi
        
# buat regex untuk mengetahui isi dari r"Received = (\d)"
received_pack = re.compile(r"Received = (\d)")
    

# catat waktu awal
time_start = time.time()

# buat list untuk menampung hasil pengecekan
result = []

# lakukan ping untuk 20 host
for suffix in range(24,50):
    # tentukan IP host apa saja yang akan di ping
    ip = "10.20.32."+str(suffix)
    
    # panggil thread untuk setiap IP
    test_thread = ip_check(ip)
    
    # masukkan setiap IP dalam list
    result.append(test_thread)
    
    # jalankan thread
    test_thread.start()

# untuk setiap IP yang ada di list
for el in result:
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya
    print('status from',el.ip,'is',el.status())

# catat waktu berakhir
time_last = time.time()

# tampilkan selisih waktu akhir dan awal
print('Durasi :', time_last-time_start)
