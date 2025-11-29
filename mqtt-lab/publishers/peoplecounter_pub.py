import paho.mqtt.client as mqtt
import time
import random

STUDENT_ID = "12221042"
BROKER = "localhost"

client = mqtt.Client("PeopleCounterPublisher")
client.connect(BROKER)

topic = "sensor/peoplecounter"

while True:
    count = random.randint(0, 10)
    message = f"StudentID:{STUDENT_ID} PeopleCount:{count}"
    client.publish(topic, message)
    print(f"Published to {topic}: {message}")
    time.sleep(5)
