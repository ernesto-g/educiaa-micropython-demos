# Proyecto demo: Juego adivinar el color
En este juego los 3 leds se encender�n a gran velocidad y al presionar el pulsador TEC1 se frenar� la secuencia en el color que estaba encendido en ese instante. 
El jugador deber� elegir un color y luego presionar el pulsador.
Al presionar el pulsador TEC2 el juego se reanudar�.

### Clases utilizadas
  - pyb.LED: Utilizamos el led 1,2 y 3 (rojo, amarillo y verde).

### El c�digo

Comenzamos definiendo 3 variables que representar�n los colores

```python
RED=0
YELLOW=1
GREEN=2
```

Creamos los objetos que poseen interacci�n con el hardware: los 3 leds de la placa (objetos led1, led2 y led3) y los dos pulsadores.

```python
led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
switch1 = pyb.Switch(1) # TEC1: stop
switch2 = pyb.Switch(2) # TEC2: restart
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

Ahora al ejecutar la funci�n "setLamp" y pasarle alguno de los 3 colores definidos previamente, se encender� en led correspondiente y se apagar�n los otros.
Ejemplo si queremos encender el amarillo:
```python
setLamp(YELLOW)
```

Escribimos una funci�n que pregunte si se presion� el pulsador TEC1, de ser as�, la variable "val" se cargar� con un "1" y se entrar� al "if".

```python
def checkStop(currentColor):
    # pregunta estado pulsador
    val = switch1.switch()
    if val==1:
        while switch2.switch()==0:
            setLamp(currentColor)
```

Al entrar al "if" se ejecutar� un buble "while" el cual eval�a el estado del pulsador TEC2 para salir, mientras tanto el bucle se ejecutar� y se encender� el led del color pasado por argumento,
debido a la llamada de la funci�n "setLamp". Al presionar TEC2, se saldr� del bucle y la funci�n terminar�.

Por �ltimo, la l�gica del juego se realiza en un bucle principal, donde se van encendiendo los leds, luego se ejecuta un peque�o delay y luego la funci�n que pregunta si se presion� el pulsador que detiene la secuencia.

```python
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
```	
	
