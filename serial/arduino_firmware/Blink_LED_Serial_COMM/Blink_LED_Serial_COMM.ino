#define LED_PIN LED_BUILTIN

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN,OUTPUT);
  digitalWrite(LED_PIN, LOW); // starts with LED off

  Serial.begin(115200); // start serial at same baud rate of serial monitor tool
  while(!Serial);   // wait for serial to be ready
  Serial.println("Ready for commands");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    String command = Serial.readStringUntil('\n'); // reads until you print newline
    command.trim(); // removes whitespace

    if (command == "on"){
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED turned ON");
    }
    else if (command == "off"){
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED turned OFF");
    }
    else {
      Serial.println("Invalid command");
    }
  }
  
}
