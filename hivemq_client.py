import paho.mqtt.client as paho
from paho import mqtt
import matplotlib.pyplot as plt
from collections import deque
import time

# MQTT Broker Details
broker_address = "broker.hivemq.com"
port = 8883
# TODO!

# Initialize lists for time and temperature values
time_values = []
temperature_values = []


# Function called when a message is received
def on_message(client, userdata, message):
    global time_values, temperature_values
    # TODO!


# Set up the MQTT client
client = paho.Client(client_id="Fabian", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.on_message = on_message
client.connect(broker_address, port)
client.subscribe(topic)
client.loop_start()

# Listen for 10 seconds
timeout = time.time() + 10  # Listen for 10 seconds
while time.time() < timeout:
    pass

# Disconnect MQTT client
client.loop_stop()
client.disconnect()

# Plot the received data
# TODO!
