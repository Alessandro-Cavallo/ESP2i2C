#____Imports____
import serial
import time

#____Function____#
def read(ComPort, BaudRate, SlaveAddress, StartAddress):
    print("Read Function")#Debug
    print(f"Slave {SlaveAddress} \n Start {StartAddress}")

    # ____Serial____#
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = f"COM{ComPort}"
        ser.timeout = 10
        ser.open()
        ser.write(b'read \n')
        time.sleep(0.01)
        ser.write(SlaveAddress)
        time.sleep(0.01)
        ser.write(StartAddress)
        time.sleep(0.01)
        Recived = ser.readline()
        time.sleep(0.01)
        ser.close()
    
    return Recived