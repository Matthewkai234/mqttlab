import paho.mqtt.client as mqtt

BROKER = "localhost"
topic = "sensor/peoplecounter"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)
    print(f"Subscribed to {topic}")

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {str(msg.payload.decode())}")

client = mqtt.Client("PeopleCounterSubscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER)
client.loop_forever()
