# Proyecto demo: Destello de LED con tiempo programable


### Clases utilizadas
  - pyb.LED: Utilizamos el led 1.

### El código

Comenzamos incluyendo el módulo pyb y creando un objeto "led" que representa el led1 de la placa:

```python
import pyb
led = pyb.LED(1)
```

A continuación dentro de un bucle WHILE preguntamos al usuario por un tiempo en milisegundos y lo convertimos a "int" mediante la función "int()"
en el caso de que el valor ingresado como string no sea un número, la función "int()" lanzará una "exception" la cual es capturada por el bloque
try-except, ejecutándose en dicho caso las líneas de código escritas en el bloque "except", las cuales imprimen un mensaje de error y vuelven 
a ejecutar el bucle WHILE desde el principio usando la sentencia "continue"

```python
while True:
	d = input("ingrese el tiempo de destello [ms]:")
	try:
		d = int(d)
	except:
		print("El valor debe ser numerico")
		continue
```

En el caso de que el valor ingresado pudo ser convertido a número sin inconvenientes, se encenderá el led y se esperará el tiempo ingresado
mediante la llamada a la función "delay", luego el led se apagará.

```python
	led.on()
	pyb.delay(d)
	led.off()
```









