import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client("humPublisher")
client.connect("localhost", 1883)

while True:
    humVal = random.randint(30, 80)
    message = f"{humVal} | ID: 12114863"
    client.publish("lab/humidity", message)
    print("humidity:", message)
    time.sleep(1.5)
