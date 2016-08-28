# Indicador de mayor de edad con Micropython sobre EDUCIAA
print("Indicador de mayor de edad")

while True:
	nombre = input("Ingresa un nombre:")
	edad = input("Ingresa una edad:")
	edad = int(edad)

	if edad >=18:
		print(nombre+" es mayor de edad")
	else:
		print(nombre+" es menor de edad")

