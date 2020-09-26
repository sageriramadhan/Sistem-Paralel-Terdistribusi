# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# import re (regular expression) untuk filter
import re

import os

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # filter pesan yang masuk 
	pesan = str(message.payload.decode("utf-8"))
	match = re.findall("A{3}", pesan)
	print (match)
    #jika ada pola AAA tulis ke result_a.txt
	if match:
		print ('match')
		if os.path.exists("result_a.txt"):
			append_write = 'a' # append if already exists
		else:
			append_write = 'w' # make a new file if not
		print(append_write)
		with open("result_a.txt",append_write) as handle:
			handle.write(pesan + '\n')
    # lainnya tulis ke result_b.txt
	else:
		print ('not')
		if os.path.exists("result_b.txt"):
			append_write = 'a' # append if already exists
		else:
			append_write = 'w' # make a new file if not
		print(append_write)
		with open("result_b.txt",append_write) as handle:
			handle.write(pesan + '\n')

    
########################################
    
# buat definisi nama broker yang akan digunakan
broker_name1 = "K5"
broker_name2 = "RAYS"
broker_address = "10.30.40.87"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=8080)
# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic")
client.subscribe(broker_name1)
client.subscribe(broker_name2)

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

#stop loop
client.loop_stop()