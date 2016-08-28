# Proyecto demo: LED ON OFF
Preguntar al usuario el estado del LED 1 de la placa, los valores posibles son ON y OFF, luego segun el valor ingresado encender o apagar el led
y volver a preguntar el estado.

### Funciones utilizadas
  - print: Imprime un mensaje por pantalla.
  - input: Se queda esperando que se ingrese texto por el teclado y luego lo devuelve como string.

### Sentencias utilizadas
  - Bucle WHILE.
  - Condicional IF

### Objetos utilizados
  - Clase LED del modulo pyb


### El código
Comenzamos incluyendo el modulo pyb, el cual posee las clases que representan a los perifericos de la placa. Luego creamos un objeto de la 
clase LED que representa al led 1 en la placa.

```python
import pyb
led = pyb.LED(1)
```

A continuacion definimos un bucle WHILE en el cual preguntamos al usuario el estado requerido para el led, y luego avaluamos el valor ingresado,
en el caso de que el valor sea la palabra "ON", ejecutamos el metodo "on()" del objeto "led", de la contrario ejecutamos el metodo "off()".

```python
while True:
    stat = input("Ingresa el estado del LED [ON/OFF]:")

    if stat == "ON" :
        led.on()
    else:
        led.off()
```




