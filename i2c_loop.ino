#include <Wire.h>

int address = 0;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  delay(2000);
  Serial.print("set i2c address is ");
  Serial.println(address);                    
}

void loop()
{
  while(true){
    if(Serial.available()) {
      String input = Serial.readStringUntil('\n');
      input.trim();
      input.toLowerCase();
      
      if (input.length() == 0) {
        Serial.println("No input detected. Try again:");
        continue;
      }
      if (input == "read") {
        readfromslave();
      }
      else if (input == "write"){
        writetoslave();
      }
      else {
        Serial.println("Unknown Command - Try Again");
      }
    }
  }
}

int waitForIntegerInput() {
  while (true) {
    if (Serial.available()) {
      String input = Serial.readStringUntil('\n');
      input.trim(); // remove whitespace and carriage return

      if (input.length() == 0) {
        Serial.println("No input detected. Try again:");
        continue;
      }

      int number = input.toInt();

      if (number == 0 && input != "0") {
        Serial.print("That's not a valid integer: ");
        Serial.println(input);
        Serial.println("Try again:");
      } else {
        Serial.print("your input was ");
        Serial.println(number);
        return number;
      }
    }
  }
}

void readfromslave() {
  address = waitForIntegerInput();
  Wire.beginTransmission(address);
  Serial.println("what address to read from?");
  Wire.write(waitForIntegerInput());
  Wire.endTransmission(false);

  Wire.requestFrom(address, 1);
  if(Wire.available()) {
    byte data = Wire.read();
    Serial.print("read data == ");
    Serial.println(data, BIN);
  } 
  else {
    Serial.println("No data received");
  };
  Serial.println("");
}

void writetoslave() {
  address = waitForIntegerInput();
  Serial.println("what address to write to?");
  unsigned char reg = waitForIntegerInput();
  Serial.println("what data to write?");
  unsigned char data = waitForIntegerInput();
  Wire.beginTransmission(address);
  Wire.write(reg);
  Wire.write(data);
  Wire.endTransmission();  
}