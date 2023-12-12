# HiveMQ Client



## Project information

This Python script allows you to connect to the HiveMQ Broker, 
subscribe to a topic, listen for a specific time and 
afterwards display the data in a graph.

## Before you start

Create a virtual environment and install packages
```
conda create --name hivemq python=3.9
conda activate hivemq
python -m pip install --upgrade pip
python -m pip install paho-mqtt
python -m pip install matplotlib
```

## Test
The script can easily be tested via the HiveMQ Websocket:
https://www.hivemq.com/demos/websocket-client/
