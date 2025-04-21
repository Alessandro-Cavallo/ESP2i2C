#____Imports____
import serial
import time

#____Function____
def write(ComPort, BaudRate, SlaveAddress, RegAddress, Data):
    print("write Function")#debug
    
    #____Convert to Binary____
    try:
        SlaveAddress = bin(SlaveAddress)
    except:
        SlaveAddress = int(SlaveAddress, 16)
        SlaveAddress = bin(SlaveAddress)
    
    try:
        RegAddress = bin(RegAddress)
    except:
        RegAddress = int(RegAddress, 16)
        RegAddress = bin(RegAddress)

    try:
        Data = bin(Data)
    except:
        Data = int(Data, 16)
        Data = bin(Data)
    
    #____Serial____
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = int(ComPort)
        ser.open()
        ser.write(b'write')
        time.sleep(0.01)
        ser.write(SlaveAddress)
        time.sleep(0.01)
        ser.write(RegAddress)
        time.sleep(0.01)
        ser.write(Data)
        time.sleep(0.01)
        ser.close()
        