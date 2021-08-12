import time
import board
import adafruit_dht
import BlynkLib

BLYNK_AUTH = 'j1N4LMcpA-eoW6VdbCqdwrtwPpXz3NO1'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

tmr_start_time = time.time()

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D24)

while True:
    blynk.run()
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        blynk.virtual_write(1, "temp:" + str(temperature_c))
        blynk.virtual_write(2, "temp:" + str(humidity))
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
    
    t = time.time()
    if t - tmr_start_time > 1:
        print("1 sec elapsed, sending data to the server...")
        blynk.virtual_write(0, "time:" + str(t))
        tmr_start_time += 1
    
    time.sleep(2.0)
