#____Imports____
import serial
import time

#____Function____#
def read(ComPort, BaudRate, SlaveAddress, StartAddress, NoOfBytes):
    print("Read Function")#Debug

    # ____Serial____#
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = f"COM{ComPort}"
        ser.timeout = 10
        ser.open()
        ser.write(b'read')
        ser.write(b'\n')
        time.sleep(0.01)
        ser.write(SlaveAddress)
        ser.write(b'\n')
        time.sleep(0.01)
        ser.write(StartAddress)
        ser.write(b'\n')
        time.sleep(0.01)
        #ser.write(NoOfBytes.encode())
        time.sleep(0.01)
        Recived = ser.readline()
        time.sleep(0.01)
        ser.close()
    
    return Recived