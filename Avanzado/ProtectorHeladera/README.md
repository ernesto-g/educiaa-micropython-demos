# Proyecto demo: Protector de tensión para heladera
Se utiliza una entrada analógica y una GPIO como salida para comandar un relé, y de esta manera monitorear la tensión analógica de entrada para decidir si se activa el relé mencionado.

### Clases utilizadas
  - LED : Se utilizan los 3 leds rojo, verde y amarillo para la indicación del nivel de tensión.
  - ADC : Se utiliza el CHN3 para leer un valor entre 0 y 3.3V representativo de la tensión de línea.
  - Pin : Se utiliza la GPIO 0 para comandar un relé, el cual alimentará el motor que se quiere proteger.
  
  
### El código
Se definen constantes para los niveles de comparación contra la tensión de línea medida por al entrada analógica (LEVEL_HIGH en 230V y LEVEL_LOW en 210V). También se define un timeout
que será el tiempo que debe durar la falla (consideraremos falla a tensión mayor a LEVEL_HIGH o menor a  LEVEL_LOW) para que se modifique la salida a relé.

```python
LEVEL_HIGH = 230
LEVEL_LOW = 210

FAILURE_TIMEOUT=10
```

Luego creamos los objetos que poseen interacción con el hardware: los 3 leds, la entrada analógica y la GPIO0 para comandar el relé.

```python
led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
channel1 = pyb.ADC(3) # Entrada analogica CH3
releOut = pyb.Pin(0) #GPIO0
releOut.init(pyb.Pin.OUT_PP,pyb.Pin.PULL_NONE)
```

Para el manejo de los 3 leds de colores, creamos la función setLamp, la cual recibe por parámetro el led que debe encenderse:

```python
RED=0
YELLOW=1
GREEN=2

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
```

Para el control del relé, creamos las funcinoes que activan y desactivan la GPIO

```python
def setReleOn():
    releOut.high() # enciendo rele
    print("enciendo rele")

def setReleOff():
    releOut.low() # apago rele
    print("apago rele")
```

#### Chequeo de tensión

Crearemos una función que se encargue de chequear el nivel de tensión comparándolo contra LEVEL_HIGH y LEVEL_LOW y devolver un valor numérico según el resultado. El valor numérico
devuelto será alguna de las constantes RED (sobre tensión), YELLOW (baja tensión) o GREEN (tensión normal)

Luego de leer la conversión de la entrada analógica, deberemos convertir dicho valor (0 a 1023) a el valor de tensión de línea que representa. Para ello primero convertimos el resultado
del ADC a un número de 0 a 3.3V simplemente multiplicando el valor devuelto (v1) por 3.3 y dividiéndolo por 1023. Suponemos que existirá un circuito en donde cuando la tensión de línea sea
240V AC, entregará 3.3V a la entrada analógica, de modo que para obtener el valor de tensión de línea que representa la tensión medida, multiplicamos por una constante "k" = 240/3.3 = 72.72
De esta manera almacenamos el la variable "voltage" el valor de tensión de línea "medido" por la entrada analógica.

```python
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
```
Por último el valor es comparado por las constantes LEVEL_HIGH y LEVEL_LOW y se devuelve RED, YELLOW o GREEN según corresponda.


#### Lógica del programa

La lógica del programa se basa en realizar un chequeo de la tensión de línea cada un segundo (se utiliza un delay con pyb.delay(1000)). Luego se enciende el led del color que corresponde 
según el resultado del chequeo y en el caso de falla (baja o sobre tensión) se comenzará a incrementar el contador "failureCounter", al llegar al valor de FAILURE_TIMEOUT, se apagará el relé
y se cargará el contador con FAILURE_TIMEOUT para que no se siga incrementando en cada loop.

En el caso de que el chequeo sea correcto (la función devuelve GREEN) el contador se decrementa hasta alcanzar el cero, cuando esto ocurre, se enciende el relé.

```python
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
```

El uso del contador permite un retardo en la activación y desactivación del relé frente a las variaciones de tensión de línea.

