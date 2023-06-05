import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt			# Import the MQTT library
import time

# MQTT broker details
broker_address = "broker.emqx.io"
topic = "SIT210/Project"

# Raspberry pi details
enb = 17
ena = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)


def on(pump_num):
    if (pump_num == 0):
        GPIO.output(enb, GPIO.HIGH)
    elif (pump_num == 1):
        GPIO.output(ena, GPIO.HIGH)


def off(pump_num):
    if (pump_num == 0):
        GPIO.output(enb, GPIO.LOW)
    elif (pump_num == 1):
        GPIO.output(ena, GPIO.LOW)

# MQTT client callbacks


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic)
    else:
        print("Failed to connect, return code:", rc)


def on_message(client, userdata, msg):
    received_data = str(msg.payload.decode("utf-8"))
    print("Received data:", received_data)

    # Process the received data
    integer_values = [int(value) for value in received_data.split(",")]
    capture_data(integer_values, 0)
    capture_data(integer_values, 1)


# Create MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(broker_address, 1883)

# Start MQTT loop
client.loop_start()


def capture_data(data_captured, pump_num):  # pump_num start from 0
    if (data_captured[2] < 20):  # tempreture
        if (data_captured[pump_num] < 400):
            print("on")
            on(pump_num)
        elif (data_captured[pump_num] > 1000):
            off(pump_num)
            print("off")

    elif (data_captured[2] > 30):
        if (data_captured[pump_num] < 700):
            print("on")
            on(pump_num)
        elif (data_captured[pump_num] > 1500):
            off(pump_num)
            print("off")

    else:
        if (data_captured[pump_num] < 550):
            print("on")
            on(pump_num)
        elif (data_captured[pump_num] > 1300):
            off(pump_num)
            print("off")


# Keep the script running if server is connected
while True:
    if client.is_connected():
        pass
