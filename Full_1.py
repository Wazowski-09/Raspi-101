import time
import board
import adafruit_dht
import glob
import RPi.GPIO as GPIO
import adafruit_bh1750
import BlynkLib

BLYNK_AUTH = 'vyL2uhXPKm6SoAccFXQRQd96gbrfUKNS'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

dhtDevice = adafruit_dht.DHT22(board.D24)

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
   if GPIO.input(channel):
     print("No Water Detected!")
     blynk.virtual_write(0, "No Water Detected!")
     blynk.virtual_write(1, 0)
   else:
     print("Water Detected!")
     blynk.virtual_write(0, "Water Detected!")
     blynk.virtual_write(1, 255) 

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

i2c = board.I2C()
 
sensor = adafruit_bh1750.BH1750(i2c)

while True:
    blynk.run()

    print("%.2f Lux" % sensor.lux)
    blynk.virtual_write(2, "Lux :" + str(sensor.lux))

try:
    temperature_c = dhtDevice.temperature
    temperature_f = temperature_c * (9 / 5) + 32
    humidity = dhtDevice.humidity
    blynk.virtual_write(3, str(temperature_c))
    blynk.virtual_write(4, str(humidity))
    print(
    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
    temperature_f, temperature_c, humidity
         )
    )

except RuntimeError as error:
    print(error.args[0])
    time.sleep(2.0)
except Exception as error:
    dhtDevice.exit()
raise error

time.sleep(2.0)

