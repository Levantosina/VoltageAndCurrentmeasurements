const int voltagePin = A0; // Analog pin for voltage measurement
const int currentPin = A1; // Analog pin for current measurement

void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < 10; i++) {
    // Read voltage and current values
    float voltage = analogRead(voltagePin) * (5.0 / 1023.0); // Convert analog value to voltage
    float current = analogRead(currentPin) * (5.0 / 1023.0); // Convert analog value to voltage
    
    // Send data to Python script
    Serial.print(voltage);
    Serial.print(",");
    Serial.println(current);

    delay(1000); // Delay before sending the next set of data
  }
  
  // Pause for 30 seconds before sending the next set of data
  delay(30000);
}
