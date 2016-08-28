# Secuenciador de leds programable en Micropython sobre EDUCIAA
import pyb

led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)

def apagoTodo():
	led1.off()
	led2.off()
	led3.off()


apagoTodo()
secuencia = list()

while True:

	ln = input("ingrese led a encender [1,2,3,fin]:")

	if ln=="fin":
		break

	try:
		ln = int(ln)
	except:
		print("El valor debe ser numerico")
		continue

	if ln!= 1 and ln!=2 and ln!=3:
		print("El valor es incorrecto")
		continue

	secuencia.append(ln)


# Ejecuto secuencia
for ln in secuencia:

	apagoTodo()
	if ln==1:
		led1.on()
	elif ln==2:
		led2.on()
	elif ln==3:
		led3.on()

	pyb.delay(1000)

apagoTodo()


            
                
