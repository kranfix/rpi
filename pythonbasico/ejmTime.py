import time

a = 0
led = True # Boolean: True o False
while a < 6:
    #print "Intento num.{0}".format(a+1)
    #print "Intento num.", a+1
    if led == True:
        print "Led encendido"
    else:
        print "Led apagado"
    time.sleep(2)

    led = not led
    a = a + 1
