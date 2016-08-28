# Proyecto demo: Termostato control analogico

import pyb

DELTA = 0.25

led1 = pyb.LED(1)

adcSensor = pyb.ADC(3) # Entrada analogica CH3
adcPot = pyb.ADC(2) # Entrada analogica CH2

releOut = pyb.Pin(0) #GPIO0
releOut.init(pyb.Pin.OUT_PP,pyb.Pin.PULL_NONE)

def readSensorTemp():
    v1 = adcSensor.read()
    print("v sensor:"+str(v1))
    k = 100 # 10mV -> 1 grado, escala
    temp = (v1*3.3/1023.0)*k
    print("temperature sensor:"+str(temp))
    return temp

def readPotTemp():
    v1 = adcPot.read()
    print("v pot:"+str(v1))
    k = 15.15 # 3.3V -> 50 grados, escala
    temp = (v1*3.3/1023.0)*k
    print("temperature pot:"+str(temp))
    return temp
                    

def setReleOn():
    releOut.high() # enciendo rele
    led1.on()
    print("enciendo rele")

def setReleOff():
    releOut.low() # apago rele
    led1.off()
    print("apago rele")

setReleOff()
while True:

    pyb.delay(1000)
    
    currentTemp = readSensorTemp()
    compareTemp = readPotTemp()
    
    if releOut.value():                    
        if currentTemp < (compareTemp-DELTA):
            setReleOff()
    else:
        if currentTemp > (compareTemp+DELTA):
            setReleOn()
        

        