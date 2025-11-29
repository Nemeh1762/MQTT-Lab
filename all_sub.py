import paho.mqtt.client as mqtt

def onMessage(client, userdata, msg):
    print(msg.topic, "->", msg.payload.decode())

sub = mqtt.Client("allSub")
sub.on_message = onMessage
sub.connect("localhost", 1883)
sub.subscribe("lab/#")
sub.loop_forever()
