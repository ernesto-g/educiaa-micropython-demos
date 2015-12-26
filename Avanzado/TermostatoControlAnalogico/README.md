# Proyecto demo: Termostato con setpoint anal�gico
Se utilizan dos entradas anal�gicas (una conectada a un sensor de temperatura LM35 y la otra a un potenci�metro) y una GPIO como salida para comandar un rel�.
Se medir� el valor de la temperatura entregada por el sensor y se comparar� con el setpoint fijado con el potenci�metro para determinar si la salida (rel�) permanece
encendida o apagada. Se utiliza un rango de hist�resis en la comparaci�n determinado por una variable del programa.

### Clases utilizadas
  - LED : Se utiliza un led para indicar el estado de la salida a rel�.
  - ADC : Se utiliza el CHN3 para leer el valor del sensor (10mv/�C) y el CHN2 para medir una tensi�n entregada por el potenci�metro.
  - Pin : Se utiliza la GPIO 0 para comandar un rel�.

### El c�digo
Se define una constante utilizada para la hist�resis en la comparaci�n entre la temperatura medida con el sensor y la determinada por el potenci�metro.

```python
DELTA = 0.25
```
  
Luego creamos los objetos que poseen interacci�n con el hardware: el led, las entradas anal�gica y la GPIO0 para comandar el rel�.

```python
led1 = pyb.LED(1)
adcSensor = pyb.ADC(3) # Entrada analogica CH3
adcPot = pyb.ADC(2) # Entrada analogica CH2
releOut = pyb.Pin(0) #GPIO0
releOut.init(pyb.Pin.OUT_PP,pyb.Pin.PULL_NONE)
```
  
Definimos una funci�n para leer la temperatura del sensor y devolverla:

```python
def readSensorTemp():
    v1 = adcSensor.read()
    print("v sensor:"+str(v1))
    k = 100 # 10mV -> 1 grado, escala
    temp = (v1*3.3/1023.0)*k
    print("temperature sensor:"+str(temp))
    return temp
```

En esta funci�n leemos el valor de la conversi�n anal�gica/digital, la cual nos devuelve un valor de 0 a 1023 (guardado en "v1") y lo transformamos en un valor de tensi�n (multiplicando por
3.3V y dividiendo por 1023) para luego multiplicarlo por la escala del sensor (10mV por cada �C) y de esta manera obtenemos en la variable "temp" el valor de la temperatura en grados.


De la misma manera, definimos una funci�n que obtenga la temperatura fijada por el potenci�metro:

```python
def readPotTemp():
    v1 = adcPot.read()
    print("v pot:"+str(v1))
    k = 15.15 # 3.3V -> 50 grados, escala
    temp = (v1*3.3/1023.0)*k
    print("temperature pot:"+str(temp))
    return temp
```

La �nica diferencia con la funci�n que lee la temperatura del sensor, es la escala. En este caso, el potenci�metro entregar� una tensi�n de 0 a 3.3V, y supondremos que 3.3V representan 50�C
por lo que el valor de la constante ser� 50/3.3 = 15.15

Para el control del rel�, creamos las funciones que activan y desactivan la GPIO

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

#### L�gica del programa

La l�gica del programa se basa en realizar una medici�n del sensor y del potenci�metro cada un segundo (se utiliza un delay con pyb.delay(1000)). 
Luego se compara la temperatura medida (sensor) con la fijada (potenci�metro) con una diferencia de DELTA, para provocar la hist�resis entre el valor del comparaci�n cuando la salida
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

En el caso de que la salida est� activa, se comparar� si la temperatura del sensor es menor a la fijada menos DELTA para decidir apagar la salida.
En el caso de que la salida est� desactivada, se comparar� si la temperatura del sensor es mayor a la fijada m�s DELTA para decidir encender la salida.



