import paho.mqtt.client as mqtt
import datetime
import json
import sys
import simpleaudio as sa
from mqttconfig import MQTT_SERVER_ADDR, MQTT_USERNAME, MQTT_PASSWORD

fn = sys.argv[1]
wave_obj = sa.WaveObject.from_wave_file(fn)
# sa.WaveObject.from_wave_read()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg_data = json.loads(msg.payload.decode('utf-8'))
    now = datetime.datetime.utcnow()
    msg_data['timestamp'] = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    #print(msg_data)
    print(msg.topic+" "+str(msg.payload))
    play_obj = wave_obj.play()



client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER_ADDR, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("bye bye")
