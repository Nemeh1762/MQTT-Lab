import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client("tempPublisher")
client.connect("localhost", 1883)

while True:
    tempVal = random.randint(20, 35)
    message = f"{tempVal} | ID: 12114863"
    client.publish("lab/temperature", message)
    print("temperature:", message)
    time.sleep(1.5)
