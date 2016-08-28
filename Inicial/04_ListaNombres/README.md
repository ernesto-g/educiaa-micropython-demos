# Proyecto demo: Lista de nombres
Preguntar al usuario nombres, los cuales se irán guardando en una lista. Cuando el usuario ingrese la palabra “salir” se imprimirá la 
cantidad de nombres ingresados y la lista de dichos nombres.

### Funciones utilizadas
  - print: Imprime un mensaje por pantalla.
  - input: Se queda esperando que se ingrese texto por el teclado y luego lo devuelve como string.
  - int: Convierte un string a int.
  - str: Convierte un int a string.
  - len: Devuelve el tamaño de una lista o array.

### Sentencias utilizadas
  - Bucle WHILE.
  - Condicional IF
  - Bucle FOR

### Objetos utilizados
  - List


### El código
Comenzamos construyendo un objeto "list" llamado "listaNombres" el cual es un array dinámico el cual tiene un tamaño de 0 items, al que podremos ir 
agregándole items en tiempo de ejecución.

```python
listaNombres = list()
```

Definimos un bucle WHILE para preguntar al usuario un nombre, y almacenarlo en la variable "nombre".

```python
while True:
    nombre = input("Ingresa un nombre:")
```

En el caso de que el usuario haya ingresado la palabra "salir" se deberá dejar de pedir nombres y terminar la ejecución de script, por lo que
mediante un bloque IF se pregunta si el valor ingresado es igual al string "salir", de ser así, se ejecuta la sentencia "break" que finaliza el
bucle WHILE y la ejecución del script continúa debajo de dicho bloque.

```python
    if nombre == "salir":
        break
```

Si el nombre ingresado no es la palabra "salir" guardamos dicho nombre en la lista de nombres "listaNombres" ejecutándole al objeto el método
"append" y pasando el item que queremos incorporar a la lista.

```python
    listaNombres.append(nombre)
```

Debajo del bloque WHILE, obtenemos el tamaño de la lista usando la función "len()" y lo almacenamos en la variable "cantidad", la cual es
impresa mediante la función "print()", transformándola en string previamente con la función "str()"

cantidad = len(listaNombres)
print("Cantidad de nombres:"+str(cantidad))

Por último, iteramos la lista mediante un bucle for, e imprimimos cada item obtenido:

```python
for n in listaNombres:
    print(n)
```

Por cada iteración del bucle FOR, se irá cargando en la variable "n" un item de la lista "listaNombres".






