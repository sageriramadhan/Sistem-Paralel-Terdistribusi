# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################


def on_message(client, userdata, message):
    # print pesan
    print("pesan diterima : ", str(message.payload.decode("utf-8")))


########################################

# buat definisi nama broker yang akan digunakan
broker_name1 = "kelompok5"
broker_name2 = "sageri_elsa_riyan_aji"
broker_address = "10.30.40.87"
# buat client baru bernama P1
print("menyiapkan instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("terhubung broker")
client.connect(broker_address, port=8080)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1 dan topik 2
print("Subscripe ke topic :")
client.subscribe(broker_name1)
client.subscribe(broker_name2)

# loop forever
while True:
    # berikan waktu tunggu 1 detik
    time.sleep(1)
    # stop loop
client.loop_stop()
