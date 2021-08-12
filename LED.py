import RPi.GPIO as GPIO             
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
for x in range(0,3):
    GPIO.output(4,True)
    time.sleep(3)
    GPIO.output(4,False)
    time.sleep(1)
GPIO.cleanup()
