# Juego Adivinar el color  con Micropython sobre EDUCIAA
# TEC1: Frena el juego de luces. TEC2: Vuelve a empezar
import pyb

RED=0
YELLOW=1
GREEN=2

led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
switch1 = pyb.Switch(1) # TEC1: stop
switch2 = pyb.Switch(2) # TEC2: restart


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

def checkStop(currentColor):
    # pregunta estado pulsador
    val = switch1.switch()
    if val==1:
        while switch2.switch()==0:
            setLamp(currentColor)
        

while True:

    setLamp(RED)
    pyb.delay(80)
    checkStop(RED)
    setLamp(YELLOW)
    pyb.delay(80)
    checkStop(YELLOW)
    setLamp(GREEN)
    pyb.delay(80)
    checkStop(GREEN)
       
            
   
    
    