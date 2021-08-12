import time
import blynklib
import RPi.GPIO as GPIO

# cmsensor1
BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'

# cmsensor2
#BLYNK_AUTH = 'JFDPBMufAg2aRnHmO5ITI9H29aUbZmA1'
blynk = blynklib.Blynk(BLYNK_AUTH)

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    blynk.run()
    if GPIO.input(channel):
        print("No Water Detected!")
        blynk.virtual_write(9, "No Water Detected!")
        blynk.virtual_write(10, 0)
    else:
        print("Water Detected!")
        blynk.virtual_write(9, "Water Detected!")
        blynk.virtual_write(10, 255)

time.sleep(500)

