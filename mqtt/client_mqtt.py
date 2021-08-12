import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("MQTT/test")
    client.subscribe("MQTT/topic")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
if msg.payload == "Hello":
        print("Received message #1, do something")
        # Do something
if msg.payload == "World!":
        print("Received message #2, do something else")
        # Do something else
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("Your_username", "Your_password")
client.connect("Your_hostname", Your_port)
client.loop_forever()
