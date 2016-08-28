# Manejo de LED On Off con Micropython sobre EDUCIAA
import pyb
print("LED ON OFF")

led = pyb.LED(1)

while True:
	stat = input("Ingresa el estado del LED [ON/OFF]:")

	if stat == "ON" :
		led.on()
	else:
		led.off()
