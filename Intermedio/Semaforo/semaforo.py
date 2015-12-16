# Semaforo con Micropython sobre EDUCIAA
import pyb

RED=0
YELLOW=1
GREEN=2

TIME_RED=10000
TIME_YELLOW=1000
TIME_GREEN=5000

led1 = pyb.LED(2)
led2 = pyb.LED(1)
led3 = pyb.LED(3)
timer = pyb.Timer(1)

status=0

def setLamp(color):   
    if color==RED:
        led1.on()
        led2.off()
        led3.off()
    elif color==YELLOW:
        led1.off()
        led2.on()
        led3.off()
    elif color==GREEN:
        led1.off()
        led2.off()
        led3.on()

def callbackTimer(timer):
    global status

    print(status)
    if status==0:
        #paso a amarillo        
        setLamp(YELLOW)
        status=1
        timer.timeout(TIME_YELLOW,callbackTimer)   
    elif status==1:
        #paso a verde
        setLamp(GREEN)
        status=2
        timer.timeout(TIME_GREEN,callbackTimer)
    elif status==2:
        #paso a rojo
        setLamp(RED)
        status=0
        timer.timeout(TIME_RED,callbackTimer)


#inicio del programa
setLamp(RED)
timer.timeout(TIME_RED,callbackTimer)


while(True):
    pyb.delay(1000)
            
                