#____Imports____
import serial

#____Function____
def write(ComPort, BaudRate, SlaveAddress, RegAddress, Data):
    print("write Function")#debug
    
    #____Convert to Binary____
    try:
        SlaveAddress = bin(SlaveAddress)
    except:
        SlaveAddress = int(SlaveAddress)
        SlaveAddress = bin(SlaveAddress)
    
    try:
        RegAddress = bin(RegAddress)
    except:
        RegAddress = int(RegAddress)
        RegAddress = bin(RegAddress)

    try:
        Data = bin(Data)
    except:
        Data = int(Data)
        Data = bin(Data)
    
    #____Serial____
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = int(ComPort)
        ser.open()
        ser.write(b'write')
        ser.write(SlaveAddress)
        ser.write(RegAddress)
        ser.write(Data)
        ser.close()
        