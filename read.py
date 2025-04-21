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
        ser.port = f"COM{ComPort}"
        ser.open()
        ser.write('read')
        time.sleep(0.01)
        ser.write(SlaveAddress.encode())
        time.sleep(0.01)
        ser.write(StartAddress.encode())
        time.sleep(0.01)
        ser.write(NoOfBytes.encode())
        time.sleep(0.01)
        Recived = ser.readline()
        time.sleep(0.01)
        ser.close()
    
    return Recived