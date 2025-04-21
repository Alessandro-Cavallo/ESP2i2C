def DecimalToAscii(Value):
    Value = str(Value)
    Value = [bin(ord(digit))[2:].zfill(8) for digit in Value]
    tempValue = Value[1]
    Value = Value[0]
    Value = Value + " " + tempValue + " " + "00001010"
    return Value

def HexToAscii(Value):
    Value = int(Value, 16)
    Value = DecimalToAscii(Value)
    return Value

def BinaryToAscii(Value):
    Value = int(Value, 2)
    Value = DecimalToAscii(Value)
    return Value

def typeChecker(Value, ValueType):
    match ValueType:
        case "Decimal":
            return DecimalToAscii(Value)
        case "Binary":
            return BinaryToAscii(Value)
        case "Hex":
            return HexToAscii(Value)

