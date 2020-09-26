# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime


def on_publish(client, userdata, result):  # create function for callback
    print("data sudah ter-publish \n")
    pass


broker_name = "kelompok5"
# definisikan nama broker yang akan digunakan
broker_address = "10.30.40.87"

# buat client baru bernama P2
print("menyiapkan instance")
client = mqtt.Client("P2")

client.on_publish = on_publish


# koneksi ke broker
print("terhubung ke broker")
client.connect(broker_address, port=8080)

# mulai loop client
client.loop_start()

# lakukan 20x publish waktu dengan topik 1
print("publish data")
for i in range(20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    x = str(datetime.datetime.now())
    client.publish(broker_name, x)
    # stop loop
    client.loop_stop()
