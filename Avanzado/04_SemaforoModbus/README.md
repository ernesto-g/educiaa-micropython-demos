# Proyecto demo: Control de 2 semaforos utilizando Modbus
El proyecto necesita dos placas EDU-CIAA. Una de ellas (Master) controla el estado del semaforo y envia tramas a la placa slave mediante el
protocolo Modbus para cambiar su estado. La segunda placa recibe los comandos y modifica el estado de los leds.

### Clases utilizadas
  - LED : Se utilizan los 3 leds rojo, verde y amarillo para la indicación del nivel de tensión.
  - Uart : Se utiliza un puerto serie para comunicar las dos placas (Puede ser el 0 o el 3)
  - ModBus.Instrument : Mediante este objeto en envian los tramas ModBus al slave.
  - ModBus.Slave : Mediante este objeto se reciben las tramas ModBus.
  
  
### El código

#### Master
En este programa se crea el objeto slaveSemaphore mediante el cual se envia una trama de escritura del registro del slave que posee la direccion
0x4000. Los valores que se escriben en el registro son las constantes RED, YELLOW y GREEN (0, 1 o 2)

```python
uart = pyb.UART(0)
uart.init(115200,packet_mode=True)
slaveSemaphore = ModBus.Instrument(uart,0x55,mode=ModBus.MODE_ASCII)
```
Inicializamos la UART en modo "packet" para recibir las tramas en un buffer en lugar de leer byte a byte, utilizando la UART0 que es la
interface RS-485.

En el bucle principal del programa se observa como se ejecuta el metodo write_register escribiendo en el registro del slave el valor
statusSlave previamente calculado segun el valor de la variable status.

```python
        statusSlave=RED
        if status == RED:
            statusSlave = GREEN
        elif status == YELLOW:
            statusSlave = YELLOW
            
        try:
            slaveSemaphore.write_register(0x4000,statusSlave)
        except Exception as e:
            print(e)
```
Se recuerda que ambos semaforos no se encienden de la misma manera, es decir, cuando el status es RED (el semaforo master esta en rojo) entonces
el semaforo slave estara en GREEN



#### Slave
En la placa Slave, se define un diccionario (mappedRegs) con un solo item, representando el registro del dispositivo slave.
Luego se crea el objeto Slave pasandole como argumento dicho diccionario. Al recibir la trama ModBus para escribir el registro, cambiara el valor
del item del diccionario.

```python
mappedRegs = {0x4000:RED}

uart = pyb.UART(0)
uart.init(115200,packet_mode=True)
slaveSemaphore = ModBus.Slave(uart,0x55,mappedRegs,mode=ModBus.MODE_ASCII)
```

En el bucle principal del programa, se ejecuta el metodo receive mediante el cual se reciben las tramas y se modifica el diccionario, en dicho caso
el metodo devuelve True, y se actualiza el estado de la lampara, ejecutando setLamp y pasando el nuevo estado del registro mediante mappedRegs.

```python
while(True):
    if slaveSemaphore.receive():
        setLamp(mappedRegs[0x4000])
```

