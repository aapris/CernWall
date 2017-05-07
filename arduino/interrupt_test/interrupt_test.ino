/****************************************************************************************************************************\
 *
 * Arduino interrupt tests, as simple and understandable as possible.
 * © Aapo Rista 2017, MIT license
 * Tested with Wemos ESP8266 D1 Mini PRO
 * https://www.wemos.cc/product/d1-mini-pro.html
 *
\*************************************************************************************************************************/

// const byte interruptPin = 2; // D4 on Wemos ESP8266
const byte interruptPin = D4; // If the board is correctly set in Arduino IDE, you can use D1, D2 etc. directly
volatile byte interruptCounter = 0;
int numberOfInterrupts = 0;
int state = 0;
 
void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.println("Start");
  // pinMode(interruptPin, INPUT_PULLUP);
  // Only one interrupt type can be attached to a GPIO pin at a time
  // attachInterrupt(digitalPinToInterrupt(interruptPin), handleInterrupt, FALLING);  
  // attachInterrupt(digitalPinToInterrupt(interruptPin), handleInterrupt, RISING);  
  attachInterrupt(digitalPinToInterrupt(interruptPin), handleInterrupt, CHANGE);
}
 
void handleInterrupt() {
  interruptCounter++;
  state = digitalRead(interruptPin);
}
 
void loop() {
 
  if(interruptCounter>0){
 
      interruptCounter--;
      numberOfInterrupts++;
 
      Serial.print("Interrupt ");
      if (state == 1) {
        Serial.print(" RISING");
      } else {
        Serial.print("FALLING");
      }
      Serial.print(" at ");
      Serial.print(millis());
      Serial.print(" ms uptime. Total: ");      
      Serial.println(numberOfInterrupts);
  }
 
}
