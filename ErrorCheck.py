from PyQt5.QtWidgets import QMessageBox
def check(Value, Value_Type):
    match Value_Type:
        case "Decimal":
            try:
                Value = int(Value)
            except:
                QMessageBox.critical(None, "An error has occured", "Please ensure that the value is a decimal or change the data type.")
                return False
            if Value > 255 or Value < 0:
                QMessageBox.critical(None, "An error has occured", "Please ensure that the Decimal Value is < 256 and => 0")
                return False
            

        case "Binary":
            if len(Value) != 8:
                QMessageBox.critical(None, "An error has occured", "Please ensure that the Binary Value is 8 bits")
                return False
            for char in Value:
                if char != "1" and char != "0":
                    print(char)#debug
                    QMessageBox.critical(None, "An error has occured", "Please ensure that Binary Value only contains '1' and '0'")
                    return False
            

        case "Hex":
            if len(Value) != 2:
                QMessageBox.critical(None, "An error has occured", "Please ensure that the Hex value has only 2 hex digits")
                return False
            HexDigts = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","a","b","c","d","e","f"]
            FirstValueValid = False
            SecondValueValid = False
            
            for i in HexDigts:
                if Value[0] == i:
                    FirstValueValid = True
                if Value[1] == i:
                    SecondValueValid = True
            
            if FirstValueValid == False or SecondValueValid == False:
                QMessageBox.critical(None, "An error has occured", f"Please ensure that the Hex value only has hex digits \n eg {HexDigts}")
                return False

            Value = str(Value)
            Value = ' '.join(format(ord(d), '08b') for d in Value)
            return Value
            
