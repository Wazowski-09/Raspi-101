import blynklib
import Adafruit_DHT
import board
#import Adafruit_BMP.BMP085 as BMP085


class Counter:
    cycle = 0


BLYNK_AUTH = 'M4TAGcXrZagnkT_mxQoXR4H-YCtsCTfZ'
#blynk = blynklib.Blynk(BLYNK_AUTH, heartbeat=15, max_msg_buffer=512)
blynk = blynklib.Blynk(BLYNK_AUTH)

T_CRI_VALUE = 20.0  # 20.0°C
T_CRI_MSG = 'Low TEMP!!!'
T_CRI_COLOR = '#c0392b'

T_COLOR = '#f5b041'
H_COLOR = '#85c1e9'
P_COLOR = '#a2d9ce'
A_COLOR = '#58d68d'
ERR_COLOR = '#444444'

T_VPIN = 7
H_VPIN = 8
P_VPIN = 9
A_VPIN = 10
GPIO_DHT22_PIN = 17


@blynk.handle_event('read V{}'.format(T_VPIN))
def read_handler(vpin):
    # DHT22
    dht22_sensor = Adafruit_DHT.DHT22(board.D18)  # possible sensor modifications .DHT11 .DHT22 .AM2302. Also DHT21 === DHT22
    #humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, GPIO_DHT22_PIN, retries=5, delay_seconds=1)
    #Counter.cycle += 1
    # check that values are not False (mean not None)
    temperature_c = dht22_sensor.temperature
    #temperature_f = temperature_c * (9 / 5) + 32
    humidity = dht22_sensor.humidity
    print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
    if all([humidity, temperature]):
        print('temperature={} humidity={}'.format(temperature, humidity))
        if temperature <= T_CRI_VALUE:
            blynk.set_property(T_VPIN, 'color', T_CRI_COLOR)
            # send notifications not each time but once a minute (6*10 sec)
            if Counter.cycle % 6 == 0:
                blynk.notify(T_CRI_MSG)
                Counter.cycle = 0
        else:
        blynk.set_property(T_VPIN, 'color', T_COLOR)
        blynk.set_property(H_VPIN, 'color', H_COLOR)
        blynk.virtual_write(T_VPIN, temperature)
        blynk.virtual_write(H_VPIN, humidity)
    else:
        print('[ERROR] reading DHT22 sensor data')
        blynk.set_property(T_VPIN, 'color', ERR_COLOR)  # show aka 'disabled' that mean we errors on data read
        blynk.set_property(H_VPIN, 'color', ERR_COLOR)



###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()