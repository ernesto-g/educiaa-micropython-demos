# Proyecto demo: semáforo simple
Implementación de un semáforo simple utilizando los leds de la placa.

##### Clases utilizadas
  - pyb.LED: Utilizamos el led 1,2 y 3 (rojo, amarillo y verde).
  - pyb.Timer: Se utiliza un timer para generar la espera entre las transiciones de colores.

### El código

Comenzamos definiendo 3 variables que representarán los colores

```python
RED=0
YELLOW=1
GREEN=2
```

Luego definimos 3 variables que contendrán en milisegundos el tiempo de espera para cada color

```python
TIME_RED=10000
TIME_YELLOW=1000
TIME_GREEN=5000
```

Creamos los objetos que poseen interacción con el hardware: los 3 leds de la placa (objetos led1, led2 y led3) y un objeto Timer que utiliza el Timer 1 del microcontrolador.

```python
led1 = pyb.LED(2)
led2 = pyb.LED(1)
led3 = pyb.LED(3)
timer = pyb.Timer(1)
```

Escribimos a continuación una función que se encargará de setear el led correspondiente según el color pasado como argumento:

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

Ahora el ejecutar la función "setLamp" y pasarle alguno de los 3 colores definidos previamente, se encenderá en led correspondiente y se apagarán los otros.
Ejemplo si queremos encender el amarillo:
```python
setLamp(YELLOW)
```

Por último, la lógica del semáforo será implementada mediante una máquina de estados, es decir, se ejecutará una funcion (que llamaremos callbackTimer) cada vez que se venza el timer,
allí decidiremos, según en el estado que nos encontramos, cuál será el próximo estado.

Para ello usamos la variable "status" definida previamente e inicializada en 0. Cada vez que se ejecute callbackTimer, se preguntará por el valor de la variable "status", se cambiará al color que sigue en la secuencia, 
se cambiará el valor de "status" al nuevo estado, y se configurará el timer con el tiempo designado para ese color.

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

Utilizaremos el timer mediante el método "timeout" el cual recibe un tiempo en milisegundos y una función, la cual se ejecutará solo una vez cuando se cumpla el tiempo designado.
Por esta razón cuando se ejecuta callbackTimer volvemos a configurar un nuevo timeout.
```python
timer.timeout(TIME_GREEN,callbackTimer)
```

Por último, lanzamos el timer por primera vez, y hacemos un loop sin código ( con un delay ) para que luego de ese tiempo se ejecute "callbackTimer" y comience la secuencia.

```python
#inicio del programa
setLamp(RED)
timer.timeout(TIME_RED,callbackTimer)

while(True):
    pyb.delay(1000)
```



