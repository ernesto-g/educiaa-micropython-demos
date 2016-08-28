# Proyecto demo: Indicador Par o Impar
Preguntar al usuario un número, luego imprimir un mensaje indicando si el número es par o impar. 
Al finalizar volver a preguntar un número.


### Funciones utilizadas
  - print: Imprime un mensaje por pantalla.
  - input: Se queda esperando que se ingrese texto por el teclado y luego lo devuelve como string.
  - int: Convierte un string a int.
  - str: Convierte un int a string.

### Sentencias utilizadas
  - Bucle WHILE.
  - Condicional IF

### El código

Comenzamos definiendo un bucle WHILE ya que el programa debera realizar el pedido de un número y su posterior análisis una y otra vez.
Dentro del bucle pedimos al usuario que ingrese un número, el cual se guardará como un tipo "string" en la variable "nStr", en la línea siguiente
convertimos dicho valor en una variable del tipo "int" mediante la función "int()".

```python
while True:
	nStr = input("Ingresa un numero:")
	nInt = int(nStr)
```

A continuación, realizamos el análisis de si el número almacenado en la variable "nInt" es par o impar, para ello, realizamos la operación
lógica AND entre dicho valor y el valor 0x0001. En el caso de que el número sea par, el resulado de la operación es 0x0001, de lo contrario el
resultado es 0x0000. Por lo que evaluamos el resultado comparándolo con 0x0001 en un bloque IF, para decidir qué mensaje imprimir.


```python
	if (nInt & 0x0001) == 0x0001:
		print("El numero es impar")
	else:
		print("El numero es par")
```

