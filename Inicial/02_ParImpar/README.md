# Proyecto demo: Indicador Par o Impar
Preguntar al usuario un numero, luego imprimir un mensaje indicando si el numero es par o impar. 
Al finalizar volver a preguntar un numero.


### Funciones utilizadas
  - print: Imprime un mensaje por pantalla.
  - input: Se queda esperando que se ingrese texto por el teclado y luego lo devuelve como string.
  - int: Convierte un string a int.
  - str: Convierte un int a string.

### Sentencias utilizadas
  - Bucle WHILE.
  - Condicional IF

### El código

Comenzamos definiendo un bucle WHILE ya que el programa debera realizar el pedido de un numero y su posterior analisis una y otra vez.
Dentro del bucle pedimos al usuario que ingrese un numero, el cual se guardara como un tipo "string" en la variable "nStr", en la linea siguiente
convertimos dicho valor en una variable del tipo "int" mediante la funcion "int()".

```python
while True:
	nStr = input("Ingresa un numero:")
	nInt = int(nStr)
```

A continuacion, realizamos el analisis de si el numero almacenado en la variable "nInt" es par o impar, para ello, realizamos la operacion
logica AND entre dicho valor y el valor 0x0001. En el caso de que el numero sea par, el resulado de la operacion es 0x0001, de lo contrario el
resultado es 0x0000. Por lo que evaluamos el resultado comparandolo con 0x0001 en un bloque IF, para decidir que mensaje imprimir.


```python
	if (nInt & 0x0001) == 0x0001:
		print("El numero es impar")
	else:
		print("El numero es par")
```

