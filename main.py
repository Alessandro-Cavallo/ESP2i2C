#____Imports____#
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from GUI import *
import read
import write
import ErrorCheck

#____Backend____#
class ESP2i2c(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #____Buttons____#
        self.ui.pb_Read.clicked.connect(self.Read)
        self.ui.pb_Write.clicked.connect(self.Write)
    
    def Read(self):
        print("Read")#Debug
        Valid = 0 #needs to be 3 for the system to function, increments after each item is validated

        ComPort = int(self.ui.cb_ComPort.currentText())
        BaudRate = int(self.ui.cb_BaudRate.currentText())

        #____Slave Address____#
        SlaveAddr = self.ui.le_SlaveAddress.text()
        SlaveAddr_Type = self.ui.cb_Address.currentText()
        if ErrorCheck.check(SlaveAddr, SlaveAddr_Type):
            Valid += 1
        
        #____Start Address____#
        StartAddr = self.ui.le_StAddr.text()
        StartAddr_Type = self.ui.cb_StAddr.currentText()
        if ErrorCheck.check(StartAddr, StartAddr_Type):
            Valid +=1
        
        #____No. Of Bytes____#
        NoBytes = self.ui.le_NoBytes.text()
        NoBytes_Type = self.ui.cb_NoBytes.currentText()
        if ErrorCheck.check(NoBytes, NoBytes_Type):
            Valid += 1

        if Valid == 3:
            Recieved = read.read(ComPort, BaudRate, SlaveAddr, StartAddr, NoBytes)
            self.ui.le_Binary.setText(str(Recieved))
            self.ui.le_Decimal.setText(str(int(str(Recieved), 2)))
            self.ui.le_Decimal.setText(str(hex(int(str(Recieved), 2))))

    
    def Write(self):
        print("Write")#Debug
        Valid = 0 #needs to be 3 for the system to function, increments after each item is validated

        ComPort = int(self.ui.cb_ComPort.currentText())
        BaudRate = int(self.ui.cb_BaudRate.currentText())

        #____Slave Address____#
        SlaveAddr = self.ui.le_SlaveAddress.text()
        SlaveAddr_Type = self.ui.cb_Address.currentText()
        if ErrorCheck.check(SlaveAddr, SlaveAddr_Type):
            Valid += 1

        #____Reg Address____#
        RegAddr = self.ui.le_RegAddr.text()
        RegAddr_Type = self.ui.cb_RegAddr.currentText()
        if ErrorCheck.check(RegAddr, RegAddr_Type):
            Valid += 1 #increments valid if the data is validated
        
        #____Data____#
        Data = self.ui.le_Data.text()
        Data_Type = self.ui.cb_Data.currentText()
        if ErrorCheck.check(Data, Data_Type):
            Valid += 1

        if Valid == 3:
            write.write(ComPort, BaudRate, SlaveAddr, RegAddr, Data)



#____Run Application____#
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = ESP2i2c()
    w.show()
    sys.exit(app.exec())
