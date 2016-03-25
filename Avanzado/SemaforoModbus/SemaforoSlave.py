# Semaforo Slave con Micropython sobre EDUCIAA
# Tramas que recibe
# Seteo en rojo    :  :55104000000102000256<CR><LF>
# Seteo en amarillo:  :55104000000102000157<CR><LF>
# Seteo en verde   :  :55104000000102000058<CR><LF>

import pyb
import ModBus

RED=0
YELLOW=1
GREEN=2

mappedRegs = {0x4000:RED}

uart = pyb.UART(3)
uart.init(115200)
slaveSemaphore = ModBus.Slave(uart,0x55,mappedRegs,mode=ModBus.MODE_ASCII)

led1 = pyb.LED(2)
led2 = pyb.LED(1)
led3 = pyb.LED(3)

def setLamp(color):   
    if color==RED:
        led1.on()
        led2.off()
        led3.off()
    elif color==YELLOW:
        led1.off()
        led2.on()
        led3.off()
    elif color==GREEN:
        led1.off()
        led2.off()
        led3.on()

#inicio del programa
setLamp(mappedRegs[0x4000])


while(True):
    if slaveSemaphore.receive():
        setLamp(mappedRegs[0x4000])
        
