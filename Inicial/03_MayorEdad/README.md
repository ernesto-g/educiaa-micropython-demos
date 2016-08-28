# Proyecto demo: Indicador de mayor de edad
Preguntar al usuario un nombre y una edad, luego imprimir el nombre y si es mayor de edad o no. Al terminar volver a comenzar.

### Funciones utilizadas
  - print: Imprime un mensaje por pantalla.
  - input: Se queda esperando que se ingrese texto por el teclado y luego lo devuelve como string.
  - int: Convierte un string a int.

### Sentencias utilizadas
  - Bucle WHILE.
  - Condicional IF

### El código

Comenzamos definiendo un bucle WHILE ya que el programa deberá realizar el pedido del nombre y la edad una y otra vez.
Dentro del bucle pedimos al usuario que ingrese un nombre, el cual se guardará como un tipo "string" en la variable "nombre", 
luego pedimos al usuario que ingrese una edad, la cual almacenamos en la variable "edad",en la línea siguiente convertimos dicho valor en una 
variable del tipo "int" mediante la función "int()".

```python
while True:
    nombre = input("Ingresa un nombre:")
    edad = input("Ingresa una edad:")
    edad = int(edad)
```

A continuación, realizamos el análisis de si la edad es mayor o igual a 18, para ello, utilizamos el operador ">=" (mayor igual) dentro de un
bloque IF, e imprimimos la variable "nombre" junto con la leyenda de si es mayor de edad o no.


```python
    if edad >=18:
        print(nombre+" es mayor de edad")
    else:
        print(nombre+" es menor de edad")
```

