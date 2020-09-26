# gunakan library paho
import paho.mqtt.client as mqtt
import numpy

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################


def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
    file = open("iris.jpg", "wb")
    file.write(message.payload)
    file.close()
    ##########################################


    # definisikan broker yang akan digunakan
broker_name = "Photo"
broker_address = "127.0.0.1"
# buat client P2
print("menyiapkan instance")
client = mqtt.Client("P2")

# koneksi P2 ke broker
print("terhubung ke broker")
client.connect(broker_address, port=8080)

# P2 subcribe ke topik "photo"
print("Subscribing ke topik:", "photo")
client.subscribe(broker_name)

# callback diaktifkan
client.on_message = on_message

# client.loop_forever()
while True:
    client.loop(15)
    time.sleep(2)
