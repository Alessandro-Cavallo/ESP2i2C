#____Imports____
import serial
import time

#____Function____#
def read(ComPort, BaudRate, SlaveAddress, StartAddress, NoOfBytes):
    print("Read Function")#Debug

    #____Convert To Binary____#
    try:
        SlaveAddress = bin(SlaveAddress)[2:]
    except:
        SlaveAddress = int(SlaveAddress, 16)
        SlaveAddress = bin(SlaveAddress)[2:]

    try:
        StartAddress = bin(StartAddress)[2:]
    except:
        StartAddress = int(StartAddress, 16)
        StartAddress = bin(StartAddress)[2:]

    try:
        NoOfBytes = bin(NoOfBytes)[2:]
    except:
        NoOfBytes = int(NoOfBytes, 16)
        NoOfBytes = bin(NoOfBytes)[2:]
    
    print(f"Slave: {SlaveAddress} \n Start: {StartAddress} \n Bytes: {NoOfBytes}")


    # ____Serial____#
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = f"COM{ComPort}"
        ser.timeout = 10
        ser.open()
        ser.write(b'read')
        time.sleep(0.01)
        ser.write(SlaveAddress)
        
        time.sleep(0.01)
        ser.write(StartAddress)
        time.sleep(0.01)
        #ser.write(NoOfBytes.encode())
        time.sleep(0.01)
        Recived = ser.readline()
        time.sleep(0.01)
        ser.close()
    
    return Recived