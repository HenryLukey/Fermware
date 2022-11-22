import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected to broker")
        client.subscribe("ispindel/ispindel09/temperature")
        client.subscribe("ispindel/ispindel09/tilt")
        client.subscribe("ispindel/ispindel09/battery")
        client.subscribe("ispindel/ispindel09/RSSI")
        client.subscribe("ispindel/ispindel09/gravity")
    else:
        print(f"connection failed with code {rc}")
   
def on_message(client, userdata, message):
    print("Message received: " + str(message.payload) + " on " + message.topic)

broker_address = "localhost"
port = 1883

client = mqttClient.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("mosq", "Rasp1234")
client.connect(broker_address, port=port)
client.loop_forever()