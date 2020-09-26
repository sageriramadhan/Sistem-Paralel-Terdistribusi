# import paho
import paho.mqtt.client as mqtt
import numpy


# definsi broker yang digunakan
broker_name = "Photo"
broker_address = "10.30.40.87"

# buat client bernama P1
print("menyiapkan instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("terhubung ke broker")
client.connect(broker_address, port=8080)

# print "baca file"
print("baca file")

# buka file surf.jpg
file = open("surf.jpg", "rb")

# baca semua isi file
gambar = file.read()
# ubah file dalam bentuk byte gunakan fungsi byte()


# publish dengan topik photo dan data dipublish adalah file
print("publish berkas")
client.publish(broker_name, gambar)

# client loop mulai
client.loop_stop()

# tutup file
