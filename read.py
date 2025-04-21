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
        SlaveAddress = int(SlaveAddress, 16)
        SlaveAddress = bin(SlaveAddress)

    try:
        StartAddress = bin(StartAddress)
    except:
        StartAddress = int(StartAddress, 16)
        StartAddress = bin(StartAddress)

    try:
        NoOfBytes = bin(NoOfBytes)
    except:
        NoOfBytes = int(NoOfBytes, 16)
        NoOfBytes = bin(NoOfBytes)
    
    print(f"{SlaveAddress} \n {StartAddress} \n {NoOfBytes}")

    # ____Serial____
    with serial.Serial() as ser:
        ser.baudrate = int(BaudRate)
        ser.port = ComPort
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