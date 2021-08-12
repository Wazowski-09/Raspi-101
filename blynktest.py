import blynklib
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D24)

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
        blynk.virtual_write(1, temperature_c)
        blynk.virtual_write(2, humidity)
        print(
            "Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

#     time.sleep(2.0)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)

