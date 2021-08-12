import socket
import time
import blynklib
from gpiozero import CPUTemperature

#cmsensor1
BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'

#cmsensor2
#BLYNK_AUTH = 'JFDPBMufAg2aRnHmO5ITI9H29aUbZmA1'
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    testIP = "8.8.8.8"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((testIP, 0))
    ipaddr = s.getsockname()[0]
    host = socket.gethostname()
    cpu = CPUTemperature()
    blynk.virtual_write(5, str(ipaddr))
    blynk.virtual_write(6, str(host))
    blynk.virtual_write(7, "Temp CPU : " + str(cpu.temperature) + " ํC")
    blynk.virtual_write(8, cpu.temperature)
    print(cpu.temperature)
    print ("IP:", ipaddr, " Host:", host)
    time.sleep(5)

