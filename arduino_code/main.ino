String incomingByte; //data that comes from the python program

void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT); // Pin 9 connected to red LED
  pinMode(13, OUTPUT); // Pin 13 connected to green LED

}
void loop() {
  if (Serial.available() > 0) {
  incomingByte = Serial.readStringUntil('\n');
    if (incomingByte == "yes") {
      //Light up the green LED
      digitalWrite(13, HIGH);
      digitalWrite(9, LOW);
    }
    else if (incomingByte == "no") {
      //Light up the red LED
      digitalWrite(9, HIGH);
      digitalWrite(13, LOW);
    }
    else{
     // Turn both LEDs off
     digitalWrite(13, LOW);
     digitalWrite(9, LOW);
    }
  }
}
