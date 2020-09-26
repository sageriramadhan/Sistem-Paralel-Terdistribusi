# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################


def on_message(client, userdata, message):
    # print pesan
    print("pesan diterima ", str(message.payload.decode("utf-8")))

########################################


broker_name = "kelompok5"
# buat definisi nama broker yang akan digunakan
broker_address = "10.30.40.87"


# buat client baru bernama P1
print("menyiapkan instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("terhubung ke broker")
client.connect(broker_address, port=8080)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1
print("Subscribing kepada topik berikut :", "kelompok5")

client.subscribe(broker_name)

# loop forever
while True:
    # berikan waktu tunggu 1 detik
    time.sleep(1)

# stop loop
client.loop_stop()
