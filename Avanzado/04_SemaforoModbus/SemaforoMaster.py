# Semaforo con Micropython sobre EDUCIAA
import pyb
import ModBus

RED=0
YELLOW=1
GREEN=2

TIME_RED=10000
TIME_YELLOW=1000
TIME_GREEN=5000

uart = pyb.UART(0) #0:rs485. 1:uart
uart.init(115200,packet_mode=True)
slaveSemaphore = ModBus.Instrument(uart,0x55,mode=ModBus.MODE_ASCII)


led1 = pyb.LED(2)
led2 = pyb.LED(1)
led3 = pyb.LED(3)
timer = pyb.Timer(1)

status=RED
status0=GREEN

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

def callbackTimer(timer):
    global status
    global RED
    global YELLOW
    global GREEN
        
    if status==RED:
        #paso a amarillo        
        status=YELLOW
        timer.timeout(TIME_YELLOW,callbackTimer)   
    elif status==YELLOW:
        #paso a verde
        status=GREEN
        timer.timeout(TIME_GREEN,callbackTimer)
    elif status==GREEN:
        #paso a rojo
        status=RED
        timer.timeout(TIME_RED,callbackTimer)

#inicio del programa
setLamp(RED)
timer.timeout(TIME_RED,callbackTimer)


while(True):
    if status!=status0:
        status0=status
        setLamp(status)
        
        statusSlave=RED
        if status == RED:
            statusSlave = GREEN
        elif status == YELLOW:
            statusSlave = YELLOW
            
        try:
            slaveSemaphore.write_register(0x4000,statusSlave)
        except Exception as e:
            print(e)

    pyb.delay(10)
            
                
