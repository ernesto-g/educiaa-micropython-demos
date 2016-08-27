# Indicador Par o Impar con Micropython sobre EDUCIAA
print("Indicador Par o Impar")

while True:
	nStr = input("Ingresa un numero:")
	nInt = int(nStr)

	if (nInt & 0x0001) == 0x0001:
		print("El numero es impar")
	else:
		print("El numero es par")

	print("\n")

