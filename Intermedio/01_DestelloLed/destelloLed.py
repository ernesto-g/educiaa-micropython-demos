# Destelo de LED con tiempo programable en Micropython sobre EDUCIAA
import pyb

led = pyb.LED(1)

while True:
	d = input("ingrese el tiempo de destello [ms]:")
	try:
		d = int(d)
	except:
		print("El valor debe ser numerico")
		continue

	led.on()
	pyb.delay(d)
	led.off()

            
                
