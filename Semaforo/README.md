# Proyecto demo: sem�foro simple
Implementaci�n de un sem�foro simple utilizando los leds de la placa.

##### Clases utilizadas
  - pyb.LED: Utilizamos el led 1,2 y 3 (rojo, amarillo y verde).
  - pyb.Timer: Se utiliza un timer para generar la espera entre las transiciones de colores.

### El c�digo

Comenzamos definiendo 3 variables que representar�n los colores

```python
RED=0
YELLOW=1
GREEN=2
```

Luego definimos 3 variables que contendr�n en milisegundos el tiempo de espera para cada color

```python
TIME_RED=10000
TIME_YELLOW=1000
TIME_GREEN=5000
```

Creamos los objetos que poseen interacci�n con el hardware: los 3 leds de la placa (objetos led1, led2 y led3) y un objeto Timer que utiliza el Timer 1 del microcontrolador.

```python
led1 = pyb.LED(2)
led2 = pyb.LED(1)
led3 = pyb.LED(3)
timer = pyb.Timer(1)
```

Escribimos a continuaci�n una funci�n que se encargar� de setear el led correspondiente seg�n el color pasado como argumento:

```python
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
```		

Ahora el ejecutar la funci�n "setLamp" y pasarle alguno de los 3 colores definidos previamente, se encender� en led correspondiente y se apagar�n los otros.
Ejemplo si queremos encender el amarillo:
```python
setLamp(YELLOW)
```

Por �ltimo, la l�gica del sem�foro ser� implementada mediante una m�quina de estados, es decir, se ejecutar� una funcion (que llamaremos callbackTimer) cada vez que se venza el timer,
all� decidiremos, seg�n en el estado que nos encontramos, cu�l ser� el pr�ximo estado.

Para ello usamos la variable "status" definida previamente e inicializada en 0. Cada vez que se ejecute callbackTimer, se preguntar� por el valor de la variable "status", se cambiar� al color que sigue en la secuencia, 
se cambiar� el valor de "status" al nuevo estado, y se configurar� el timer con el tiempo designado para ese color.

```python
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
```

Es importante destacar que para poder leer/escribir una variable global dentro de un callback, deberemos definir la variable dentro del callback con el modificador "global"

### Funcionamiento del timer en modo timeout

Utilizaremos el timer mediante el m�todo "timeout" el cual recibe un tiempo en milisegundos y una funci�n, la cual se ejecutar� solo una vez cuando se cumpla el tiempo designado.
Por esta raz�n cuando se ejecuta callbackTimer volvemos a configurar un nuevo timeout.
```python
timer.timeout(TIME_GREEN,callbackTimer)
```

Por �ltimo, lanzamos el timer por primera vez, y hacemos un loop sin c�digo ( con un delay ) para que luego de ese tiempo se ejecute "callbackTimer" y comience la secuencia.

```python
#inicio del programa
setLamp(RED)
timer.timeout(TIME_RED,callbackTimer)

while(True):
    pyb.delay(1000)
```



