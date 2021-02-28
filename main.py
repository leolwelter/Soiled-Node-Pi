# VERY slightly modified from the Adafruit Stemma example usage
import time
from adafruit_seesaw.seesaw import Seesaw
from board import SCL, SDA
import busio
import os
import datetime

i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)

with open(os.getcwd() + '/sensor-logs.log', 'a') as logfile:
    while True:
        # read moisture level through capacitive touch pad
        touch: int = ss.moisture_read()

        # read temperature from the temperature sensor
        temp: float = ss.get_temp()
        logfile.write("{}\tTemp:{:4.2f}\tMoisture:{:4d}\n".format(datetime.datetime.now(), temp, touch))
        time.sleep(1)
