import paho.mqtt.client as mqtt
import time
import random

STUDENT_ID = "12221042"
BROKER = "localhost"

client = mqtt.Client("TempPublisher")  
client.connect(BROKER)

topic = "sensor/temperature"

while True:
    temp = round(random.uniform(20.0, 30.0), 2)
    message = f"StudentID:{STUDENT_ID} Temperature:{temp} C"
    client.publish(topic, message)
    print(f"Published to {topic}: {message}")
    time.sleep(5)