# Proyecto demo: Secuenciados de LEDs
Hacer un programa que le pida al usuario que ingrese la secuencia de leds que se encenderan de a uno, cada 1 segundo. (EL ingreso sera 1,2 o 3) 
al ingresar la palabra "fin" el programa comenzara a ejecutar la secuencia programada.

### Clases utilizadas
  - pyb.LED: Utilizamos el led 1.

### El codigo

Comenzamos incluyendo el modulo pyb y creando un objeto "led" por cada led de la placa:

```python
import pyb

led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
```

Definimos una funcion que apagara los 3 leds, ya que la usaremos en varias partes del programa:

```python
def apagoTodo():
	led1.off()
	led2.off()
	led3.off()
```

Ejecutamos la funcion y creamos una lista donde se almacenaran los valores de los leds a encender en la secuencia:

```python
apagoTodo()
secuencia = list()
```

Dentro de un bloque WHILE pedimos al usuario que ingrese el numero de led a agregar enla secuencia o la palabra "finalizar", luego chequeamos
que le valor ingresado sea correcto:

```python
while True:

	ln = input("ingrese led a encender [1,2,3,fin]:")

	if ln=="fin":
		break

	try:
		ln = int(ln)
	except:
		print("El valor debe ser numerico")
		continue

	if ln!= 1 and ln!=2 and ln!=3:
		print("El valor es incorrecto")
		continue
```

En el caso de ingresar "fin" se ejecutara la sentencia "break" para terminar el bloque WHILE. En el caso de que el valor no sea numerico
o no sea 1,2 o 3, se imprimira un error y se volvera a pedir el ingreso.

Si el valor ingresado es valido, lo agregamos a la lista "secuencia":

```python
	secuencia.append(ln)
```

Al finalizar el bucle WHILE, iteramos la lista "secuencia" mediente un bucle FOR y encendemos el led correspondiente segun el contenido de
la lista, esperando un segundo con la funcion "delay" entre cada iteracion:

```python
for ln in secuencia:

	apagoTodo()
	if ln==1:
		led1.on()
	elif ln==2:
		led2.on()
	elif ln==3:
		led3.on()

	pyb.delay(1000)

apagoTodo()
```










