#!/usr/bin/python
# Author: Frank Moreno <frankmoreno1993gmail.com>

import Adafruit_DHT
import sys
import Adafruit_BMP.BMP085 as BMP180

bmp = BMP180.BMP085()

dht_args = { '11': Adafruit_DHT.DHT11,
             '22': Adafruit_DHT.DHT22,
           '2302': Adafruit_DHT.AM2302 }


#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#    sensor = sensor_args[sys.argv[1]]
#    pin = sys.argv[2]
#else:
#    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
#    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO 4')
#    sys.exit(1)
dhtsensor = 11
dhtpin = 4


humidity, temperature = Adafruit_DHT.read_retry(dhtsensor, dhtpin)
pressure = bmp.read_pressure()

if humidity is not None and temperature is not None:
    print('{'+'"Temp":{0:0.1f},"Humidity":{1:0.1f}, "Pressure":{2:0.2f}'.format(temperature, humidity,pressure) + '}')
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

