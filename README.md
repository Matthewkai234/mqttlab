# mqttlab
### Features:
- Mosquitto MQTT Broker installed and configured locally
- Three publishers simulating sensor data:
  - Temperature sensor
  - Humidity sensor
  - People counter sensor
- Three subscribers, each subscribing to a specific topic and displaying messages
- Each message includes my **Student ID: 12221042**

## How to Run

1. **Start the Mosquitto broker using the configuration file**:
    mosquitto -c <path-to-your-mosquitto.conf> -v   
   
2. **Run the publishers (open separate CMD windows for each)**:
   cd mqtt-lab\publishers
   python temp_pub.py
   python humidity_pub.py
   python peoplecounter_pub.py
   
3. **Run the subscribers (open separate CMD windows for each)**:
   cd mqtt-lab\subscribers
   python temp_sub.py
   python humidity_sub.py
   python peoplecounter_sub.py
