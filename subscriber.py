# Import required libraries
import paho.mqtt.client as mqttClient
import time
import RPi.GPIO as GPIO

# Function for what to do when mqtt client connects to broker
def on_connect(client, userdata, flags, rc):
    # If there are no errors
    if rc == 0:
        # Print a message saying connection was successful
        print("connected to broker")
        # Subscribe to the temperature topic
        client.subscribe("ispindel/ispindel09/temperature")
        # Set up GPIO settings
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Pin 18 is being used for the LED
        GPIO.setup(18, GPIO.OUT)
    # Otherwise say there was an error connecting to broker
    else:
        print(f"connection failed with code {rc}")

#Function for what to do when receiving an mqtt message from the broker
def on_message(client, userdata, message):
    # If the topic is the temperature
    if message.topic == "ispindel/ispindel09/temperature":
        # Open the temperature ranges file (to find min and max temperature)
        tempRangesFile = open("/home/Rasp09/Fermware/tempRanges.txt", "r")
        # Read the content of the file and remove any new lines
        contents = tempRangesFile.readline()
        contents = contents.replace("\n", "")
        # Put the min and max value into an array
        minMax = contents.split(",");
        # If the current temperature is bigger than the desired max temperature
        if float(message.payload) > (float(minMax[1])+0.5):
            # Print that the pump is being turned on and turn on the LED to represent this
            print("TURNING ON PUMP")
            GPIO.output(18, GPIO.HIGH)
        # Otherwise print a message saying the pump is turning off and turn off the LED
        else:
            print("TURNING OFF PUMP")
            GPIO.output(18, GPIO.LOW)
        # Close the file
        tempRangesFile.close()

# The broker address is simply the localhost ip
broker_address = "127.0.0.1"
# Port used is 1883
port = 1883

# Setup the client variable
client = mqttClient.Client()
# Tell client what to do when it connects and when it receives a message
client.on_connect = on_connect
client.on_message = on_message
# Pass in the username and password for the mosquitto server
client.username_pw_set("mosq", "Rasp1234")
# Connect the client to the broker
client.connect(broker_address, port=port)
# Loop infinitely
client.loop_forever()