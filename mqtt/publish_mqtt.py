import paho.mqtt.publish as publish
hostname = "Your_hostname"
port = Your_port
auth = {
 'username':'Your_username',
 'password':'Your_password'
}

publish.single("MQTT/test", "Hello", hostname=hostname, port=port, auth=auth)
publish.single("MQTT/topic", "World!", hostname=hostname, port=port, auth=auth)
print("Done")
