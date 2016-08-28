# Proyecto demo: Destello de LED con tiempo programable


### Clases utilizadas
  - pyb.LED: Utilizamos el led 1.

### El codigo

Comenzamos incluyendo el modulo pyb y creando un objeto "led" que representa el led1 de la placa:

```python
import pyb
led = pyb.LED(1)
```

A continuacion dentro de un bucle WHILE preguntamos al usuario por un tiempo en milisegundos y lo convertimos a "int" mediante la funcion "int()"
en el caso de que el valor ingresado como string no sea un numero, la funcion "int()" lanzara una exception la cual es capturada por el bloque
try-except, ejecutandose en dicho caso las lineas de codigo escritas en el bloque "except", las cuales imprimen un mensaje de error y vuelven 
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

En el caso de que el valor ingresado pudo ser convertido a numero sin inconvenientes, se encendera el led y se esperara el tiempo ingresado
mediante la llamada a la funcion "delay" luego el led se apagara.

```python
	led.on()
	pyb.delay(d)
	led.off()
```









