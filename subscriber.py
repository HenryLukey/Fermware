import paho.mqtt.client as mqttClient
import time
import RPi.GPIO as GPIO

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected to broker")
        client.subscribe("ispindel/ispindel09/temperature")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)

    else:
        print(f"connection failed with code {rc}")
   
def on_message(client, userdata, message):
    if message.topic == "ispindel/ispindel09/temperature":
        tempRangesFile = open("/home/Rasp09/Fermware/tempRanges.txt", "r")
        contents = tempRangesFile.readline()
        contents = contents.replace("\n", "")
        minMax = contents.split(",");
        if float(message.payload) > (float(minMax[1])+0.5):
            print("TURNING ON PUMP")
            GPIO.output(18, GPIO.HIGH)
        else:
            print("TURNING OFF PUMP")
            GPIO.output(18, GPIO.LOW)
        tempRangesFile.close()

broker_address = "127.0.0.1"
port = 1883

client = mqttClient.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("mosq", "Rasp1234")
client.connect(broker_address, port=port)
client.loop_forever()