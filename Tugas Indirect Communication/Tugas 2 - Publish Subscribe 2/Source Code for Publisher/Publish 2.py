# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime


# definisikan nama broker yang akan digunakan
broker_name = "sageri_elsa_riyan_aji"
broker_address = "10.30.40.87"

# buat client baru bernama P3
print("menyiapkan instance")
client = mqtt.Client("P3")

# koneksi ke broker
print("terhubung ke broker")
client.connect(broker_address, port=8080)

# mulai loop client
client.loop_start()

# lakukan 20x publish topik 2
print("publish data")
for i in range(20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang topik 2
    x = str(datetime.datetime.now())
    client.publish(broker_name, x)
    # stop loop
    client.loop_stop()
