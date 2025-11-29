#MQTT Lab#
#Student ID:"12114863"#

This project shows a basic MQTT setup using Mosquitto Broker & Paho MQTT in Python.
The program includes three publishers and two subscribers.

#Topics:

lab/temperature
lab/humidity
lab/people
lab/# (all topics)

#Publishers:

temp_pub.py — sends temperature values
hum_pub.py — sends humidity values
people_pub.py — sends people count

#Each message includes:

value | ID: 12114863

#Subscribers:

temp_sub.py — receives only temperature
all_sub.py — receives all topics under lab/#

#How to Run?

Start Mosquitto Broker
Activate the virtual environment
Run the three publishers
Run the two subscribers

#Status:

All scripts tested and working.
