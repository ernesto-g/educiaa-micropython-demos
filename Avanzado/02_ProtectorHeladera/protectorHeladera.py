# Proyecto demo: Protector de tension para heladera

import pyb

RED=0
YELLOW=1
GREEN=2

LEVEL_HIGH = 230
LEVEL_LOW = 210

FAILURE_TIMEOUT=10

led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
channel1 = pyb.ADC(3) # Entrada analogica CH3
releOut = pyb.Pin(0) #GPIO0
releOut.init(pyb.Pin.OUT_PP,pyb.Pin.PULL_NONE)

def setLamp(color):   
    if color==YELLOW:
        led1.on()
        led2.off()
        led3.off()
    elif color==RED:
        led1.off()
        led2.on()
        led3.off()
    elif color==GREEN:
        led1.off()
        led2.off()
        led3.on()


def checkVoltageLevel():
    v1 = channel1.read()
    print("v1:"+str(v1))
    k = 72.72 # 3.3V -> 240V, escala
    voltage = (v1*3.3/1023.0)*k
    print("voltage:"+str(voltage))    
    if voltage >= LEVEL_HIGH:
        return RED
    if voltage <=LEVEL_LOW:
        return YELLOW
    return GREEN

def setReleOn():
    releOut.high() # enciendo rele
    print("enciendo rele")

def setReleOff():
    releOut.low() # apago rele
    print("apago rele")

setReleOff() # apago rele
failureCounter=10
while True:

    pyb.delay(1000)
    
    color = checkVoltageLevel()
    setLamp(color)
    if color!=GREEN:
        failureCounter+=1
    else:
        if failureCounter>0:
            failureCounter-=1

    if failureCounter>=FAILURE_TIMEOUT:
        setReleOff() # apago rele
        failureCounter=FAILURE_TIMEOUT

    if failureCounter==0:
        setReleOn() # enciendo rele
        

        