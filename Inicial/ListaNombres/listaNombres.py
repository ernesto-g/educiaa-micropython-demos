# Lista de nombres con Micropython sobre EDUCIAA
print("Lista de nombres")

listaNombres = list()

while True:
	nombre = input("Ingresa un nombre:")

	if nombre == "salir":
		break

	listaNombres.append(nombre)


cantidad = len(listaNombres)
print("Cantidad de nombres:"+str(cantidad))

for n in listaNombres:
    print(n)