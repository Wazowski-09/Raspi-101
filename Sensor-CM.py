#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_am2320
import adafruit_dht
import glob
import adafruit_bh1750
import blynklib

BLYNK_AUTH = '<M4TAGcXrZagnkT_mxQoXR4H-YCtsCTfZ>'
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('read V22')
def read_virtual_pin_handler(V22):


#DHT22
dhtDevice = adafruit_dht.DHT22(board.D18)
# create the I2C shared bus
#AM2315
i2c = busio.I2C(board.SCL, board.SDA)
#am = adafruit_am2320.AM2320(i2c)
#DS18B20
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

#moisture
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print("no Water Detected!")
                blynk.virtual_write(V5,0)
        else:
                print("Water Detected!")
                blynk.virtual_write(V5,1)
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
 #bh1750
 #i2c = board.I2C()
 
sensor = adafruit_bh1750.BH1750(i2c)

#sensor_data = '<read_temp()>'
blynk.virtual_write(V4, read_temp())

while True:
    blynk.run()
    #print("Temperature: ", am.temperature)
    #print("Humidity: ", am.relative_humidity)
    print(read_temp())
    print("%.2f Lux" % sensor.lux)

    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        #temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2.0)