import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [17, 27, 22]
GPIO.setup(pins, GPIO.OUT, initial = GPIO.HIGH)
time.sleep(1)
for pin in pins :
 GPIO.output(pin,  GPIO.LOW)
 print("PIN: " + str(pin) + " is 0 (GPIO.LOW)")
 time.sleep(5)
 GPIO.output(pin,  GPIO.HIGH)
 print("PIN: " + str(pin) + " is 1 (GPIO.HIGH)")
 time.sleep(1)
 GPIO.cleanup()
 print"Cleaned up relays"
