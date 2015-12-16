# Proyecto demo: Suma de dos números
Programa que le pide al usuario que ingrese dos números e imprime la suma

### Funciones utilizadas
  - print: Imprime un mensaje por pantalla.
  - input: Se queda esperando que se ingrese texto por el teclado y luego lo devuelve como string.
  - int: Convierte un string a int.
  - str: Convierte un int a string.

### El código

Comenzamos utilizando la función input para quedarnos esperando que se ingrese un texto. El texto que se le pasa como argumento a la función, será impreso por la consola.

```python
n1 = input("Ingresa un numero:")
```

Guardamos los dos números ingresados en las variables n1 y n2, ambas serán de tipo String, por lo que deberemos convertirlas a int para poder sumarlas

```python
sum = int(n1) + int(n2) 
```

Por último imprimimos el resultado, para ello convertimos la variable numérica "sum" a string mediante la función "str"

```python
print("la suma es:"+str(sum))
```