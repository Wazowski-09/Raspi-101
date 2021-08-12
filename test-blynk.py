import blynklib
import RPi.GPIO as GPIO
import time
# import blynklib_mp as blynklib # micropython import

BLYNK_AUTH = 'M4TAGcXrZagnkT_mxQoXR4H-YCtsCTfZ' #insert your Auth Token here
# base lib init
blynk = blynklib.Blynk(BLYNK_AUTH)

define R1 22
define R2 27
define R3 17
define R4 18
define R5 10
define R6 9
define R7 20
define R8 21

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(R1,GPIO.OUT)
GPIO.setup(R2,GPIO.OUT)
GPIO.setup(R3,GPIO.OUT)
GPIO.setup(R4,GPIO.OUT)
GPIO.setup(R5,GPIO.OUT)
GPIO.setup(R6,GPIO.OUT)
GPIO.setup(R7,GPIO.OUT)
GPIO.setup(R8,GPIO.OUT)
while True:
    blynk.run()
    GPIO.output(R1,GPIO.HIGH)
	GPIO.output(R2,GPIO.HIGH)
	GPIO.output(R3,GPIO.HIGH)
	GPIO.output(R4,GPIO.HIGH)
	GPIO.output(R5,GPIO.HIGH)
	GPIO.output(R6,GPIO.HIGH)
	GPIO.output(R7,GPIO.HIGH)
	GPIO.output(R8,GPIO.HIGH)
while False:
	GPIO.output(R1,GPIO.LOW)
	GPIO.output(R2,GPIO.LOW)
	GPIO.output(R3,GPIO.LOW)
	GPIO.output(R4,GPIO.LOW)
	GPIO.output(R5,GPIO.LOW)
	GPIO.output(R6,GPIO.LOW)
	GPIO.output(R7,GPIO.LOW)
	GPIO.output(R8,GPIO.LOW)