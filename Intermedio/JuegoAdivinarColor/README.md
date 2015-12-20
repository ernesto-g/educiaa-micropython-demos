# Proyecto demo: Juego adivinar el color
En este juego los 3 leds se encenderán a gran velocidad y al presionar el pulsador TEC1 se frenará la secuencia en el color que estaba encendido en ese instante. 
El jugador deberá elegir un color y luego presionar el pulsador.
Al presionar el pulsador TEC2 el juego se reanudará.

### Clases utilizadas
  - pyb.LED: Utilizamos el led 1,2 y 3 (rojo, amarillo y verde).

### El código

Comenzamos definiendo 3 variables que representarán los colores

```python
RED=0
YELLOW=1
GREEN=2
```

Creamos los objetos que poseen interacción con el hardware: los 3 leds de la placa (objetos led1, led2 y led3) y los dos pulsadores.

```python
led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
switch1 = pyb.Switch(1) # TEC1: stop
switch2 = pyb.Switch(2) # TEC2: restart
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

Ahora al ejecutar la función "setLamp" y pasarle alguno de los 3 colores definidos previamente, se encenderá en led correspondiente y se apagarán los otros.
Ejemplo si queremos encender el amarillo:
```python
setLamp(YELLOW)
```

Escribimos una función que pregunte si se presionó el pulsador TEC1, de ser así, la variable "val" se cargará con un "1" y se entrará al "if".

```python
def checkStop(currentColor):
    # pregunta estado pulsador
    val = switch1.switch()
    if val==1:
        while switch2.switch()==0:
            setLamp(currentColor)
```

Al entrar al "if" se ejecutará un buble "while" el cual evalúa el estado del pulsador TEC2 para salir, mientras tanto el bucle se ejecutará y se encenderá el led del color pasado por argumento,
debido a la llamada de la función "setLamp". Al presionar TEC2, se saldrá del bucle y la función terminará.

Por último, la lógica del juego se realiza en un bucle principal, donde se van encendiendo los leds, luego se ejecuta un pequeño delay y luego la función que pregunta si se presionó el pulsador que detiene la secuencia.

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
	
