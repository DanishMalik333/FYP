#include <Arduino.h>
#include <Servo.h>
char inChar;
String inString = "", a1 = "" , a2 = "", a3 = "", a4 = "";
int flag = 1;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
void setup() 
{
  Serial.begin(9600);
} 
void loop()
{  
  while (Serial.available() > 0) {
    inChar = Serial.read();
    inString += inChar;
  }
  for(int i = 0; i < inString.length(); i++)
  {
    if (inString[i] == '+')
    {
      flag += 1;
      continue;
    }
    switch (flag)
    {
    case 1:
      a1 += inString[i];
      break;
    case 2:
      a2 += inString[i];
      break;
    case 3:
      a3 += inString[i];
      break;
    case 4:
      a4 += inString[i];
      break;
    }
  }
  
  int angle1 = a1.toInt();
  int angle2 = a2.toInt();
  int angle3 = a3.toInt();
  int angle4 = a4.toInt();

  servo1.attach(3);
  servo1.write(angle1);
  delay(100);
  servo2.attach(5);
  servo2.write(angle2);
  delay(100); 
  servo3.attach(9);
  servo3.write(angle3);
  delay(100);
  servo4.attach(11);
  servo4.write(angle4);

}
