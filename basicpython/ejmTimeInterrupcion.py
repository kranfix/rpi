import time

a = 0
led = True # Boolean: True o False
isRunning = True # esta corriendo o ejecutandose

while isRunning:
    try:
        if led == True:
            print "Led encendido"
        else:
            print "Led apagado"
        time.sleep(2)

        led = not led
        a = a + 1
    except KeyboardInterrupt:
        isRunning = False
        led = False
        print "Interrupcion de teclado"
