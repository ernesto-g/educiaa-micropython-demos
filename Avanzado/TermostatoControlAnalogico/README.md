# Proyecto demo: Termostato con setpoint analógico
Se utilizan dos entradas analógicas (una conectada a un sensor de temperatura LM35 y la otra a un potenciómetro) y una GPIO como salida para comandar un relé.
Se medirá el valor de la temperatura entregada por el sensor y se comparará con el setpoint fijado con el potenciómetro para determinar si la salida (relé) permanece
encendida o apagada. Se utiliza un rango de histéresis en la comparación determinado por una variable del programa.

### Clases utilizadas
  - LED : Se utiliza un led para indicar el estado de la salida a relé.
  - ADC : Se utiliza el CHN3 para leer el valor del sensor (10mv/ºC) y el CHN2 para medir una tensión entregada por el potenciómetro.
  - Pin : Se utiliza la GPIO 0 para comandar un relé.

### El código
Se define una constante utilizada para la histéresis en la comparación entre la temperatura medida con el sensor y la determinada por el potenciómetro.

```python
DELTA = 0.25
```
  
Luego creamos los objetos que poseen interacción con el hardware: el led, las entradas analógica y la GPIO0 para comandar el relé.

```python
led1 = pyb.LED(1)
adcSensor = pyb.ADC(3) # Entrada analogica CH3
adcPot = pyb.ADC(2) # Entrada analogica CH2
releOut = pyb.Pin(0) #GPIO0
releOut.init(pyb.Pin.OUT_PP,pyb.Pin.PULL_NONE)
```
  
Definimos una función para leer la temperatura del sensor y devolverla:

```python
def readSensorTemp():
    v1 = adcSensor.read()
    print("v sensor:"+str(v1))
    k = 100 # 10mV -> 1 grado, escala
    temp = (v1*3.3/1023.0)*k
    print("temperature sensor:"+str(temp))
    return temp
```

En esta función leemos el valor de la conversión analógica/digital, la cual nos devuelve un valor de 0 a 1023 (guardado en "v1") y lo transformamos en un valor de tensión (multiplicando por
3.3V y dividiendo por 1023) para luego multiplicarlo por la escala del sensor (10mV por cada ºC) y de esta manera obtenemos en la variable "temp" el valor de la temperatura en grados.


De la misma manera, definimos una función que obtenga la temperatura fijada por el potenciómetro:

```python
def readPotTemp():
    v1 = adcPot.read()
    print("v pot:"+str(v1))
    k = 15.15 # 3.3V -> 50 grados, escala
    temp = (v1*3.3/1023.0)*k
    print("temperature pot:"+str(temp))
    return temp
```

La única diferencia con la función que lee la temperatura del sensor, es la escala. En este caso, el potenciómetro entregará una tensión de 0 a 3.3V, y supondremos que 3.3V representan 50ºC
por lo que el valor de la constante será 50/3.3 = 15.15

Para el control del relé, creamos las funciones que activan y desactivan la GPIO

```python
def setReleOn():
    releOut.high() # enciendo rele
    led1.on()
    print("enciendo rele")

def setReleOff():
    releOut.low() # apago rele
    led1.off()
    print("apago rele")
```

#### Lógica del programa

La lógica del programa se basa en realizar una medición del sensor y del potenciómetro cada un segundo (se utiliza un delay con pyb.delay(1000)). 
Luego se compara la temperatura medida (sensor) con la fijada (potenciómetro) con una diferencia de DELTA, para provocar la histéresis entre el valor del comparación cuando la salida
se encuentra activa y cuando no.

```python
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
```

En el caso de que la salida esté activa, se comparará si la temperatura del sensor es menor a la fijada menos DELTA para decidir apagar la salida.
En el caso de que la salida esté desactivada, se comparará si la temperatura del sensor es mayor a la fijada más DELTA para decidir encender la salida.



