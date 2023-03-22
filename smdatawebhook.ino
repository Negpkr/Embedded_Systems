  /*
  # Editor     : NEGIN PAKROOH
  
  # the sensor value description
  # 0  ~300     dry soil
  # 300~700     humid soil
  # 700~950     in water
  */
int Moisture = A1;
int led = D7;  // The on-board LED
void setup() 
{
  pinMode(Moisture, INPUT);
  pinMode(led, OUTPUT);
}

void loop() 
{

  digitalWrite(led, HIGH);   // Turn ON the LED
  //SENSOR PART
  String SMdata = String(analogRead(1)); //connect sensor to Analog 1
  Particle.publish("SMdata", SMdata, PRIVATE);
  delay(1000);               // Wait for 1 seconds

  digitalWrite(led, LOW);    // Turn OFF the LED
  delay(1000);   
}
