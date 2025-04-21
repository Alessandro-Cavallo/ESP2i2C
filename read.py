#____Imports____
import serial
import time

#____Function____
def read(ComPort, BaudRate, SlaveAddress, StartAddress, NoOfBytes):
    print("Read Function")#Debug

    #____Convert To Binary____#
    try:
        SlaveAddress = bin(SlaveAddress)
    except:
        SlaveAddress = int(SlaveAddress)
        SlaveAddress = bin(SlaveAddress)

    try:
        StartAddress = bin(StartAddress)
    except:
        StartAddress = int(StartAddress)
        StartAddress = bin(StartAddress)

    try:
        NoOfBytes = bin(NoOfBytes)
    except:
        NoOfBytes = int(NoOfBytes)
        NoOfBytes = bin(NoOfBytes)

    #____Serial____
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = int(ComPort)
        ser.open()
        ser.write(b'read')
        time.sleep(0.01)
        ser.write(SlaveAddress)
        time.sleep(0.01)
        ser.write(StartAddress)
        time.sleep(0.01)
        ser.write(NoOfBytes)
        time.sleep(0.01)
        Recived = ser.read_all()
        time.sleep(0.01)
        ser.close()
    
    return Recived