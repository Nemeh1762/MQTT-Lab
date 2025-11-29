import paho.mqtt.client as mqtt

def onMessage(client, userdata, msg):
    print("temp received:", msg.payload.decode())

sub = mqtt.Client("tempSub")
sub.on_message = onMessage
sub.connect("localhost", 1883)
sub.subscribe("lab/temperature")
sub.loop_forever()
