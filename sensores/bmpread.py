#!/usr/bin/python
# Author: Frank Moreno <frankmoreno1993@gmail.com>

import Adafruit_BMP.BMP085 as BMP180

sensor = BMP180.BMP085()

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)

# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER,
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
#sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

s = '{'
#s += '"Temp":{0:0.2f},'.format(sensor.read_temperature())  # Celsius
s += '"Pressure":{0:0.2f}'.format(sensor.read_pressure())  # Pa
#s += '",Altitude":{0:0.2f}'.format(sensor.read_altitude())  # metros
#s += '",SealevelPressure":{0:0.2f}'.format(sensor.read_sealevel_pressure())) #Pa
s += '}'
print s

