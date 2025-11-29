import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client("peoplePublisher")
client.connect("localhost", 1883)

while True:
    peopleVal = random.randint(0, 15)
    message = f"{peopleVal} | ID: 12114863"
    client.publish("lab/people", message)
    print("people:", message)
    time.sleep(1.5)
