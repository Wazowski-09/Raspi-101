import time
import board
import adafruit_dht
import BlynkLib

BLYNK_AUTH = 'bWfLDHiXQi5aINaBknNkJQprSmWoIjza'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

dhtDevice = adafruit_dht.DHT22(board.D18)

while True:
    blynk.run()
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        blynk.virtual_write(10, "Temp : " + str(temperature_c))
        blynk.virtual_write(11, "Humidity : " + str(humidity))
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)