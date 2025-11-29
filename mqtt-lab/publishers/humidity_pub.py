import paho.mqtt.client as mqtt
import time
import random

STUDENT_ID = "12221042"
BROKER = "localhost"

client = mqtt.Client("HumidityPublisher")
client.connect(BROKER)

topic = "sensor/humidity"

while True:
    humidity = round(random.uniform(30.0, 70.0), 2)
    message = f"StudentID:{STUDENT_ID} Humidity:{humidity} %"
    client.publish(topic, message)
    print(f"Published to {topic}: {message}")
    time.sleep(5)
