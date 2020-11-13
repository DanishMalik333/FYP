#include <Servo.h>

Servo servo1;  
Servo servo2;  
Servo servo3;
Servo servo4;

void setup() {
  servo1.attach(3);
  servo1.write(0);
  delay(100);
  servo2.attach(5); 
  servo2.write(0);
  delay(100);
  servo3.attach(9); 
  servo3.write(0);
  delay(100);
  servo4.attach(11); 
  servo4.write(0);
}

void loop() {}
