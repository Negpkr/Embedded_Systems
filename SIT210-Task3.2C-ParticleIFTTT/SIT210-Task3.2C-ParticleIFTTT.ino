
//LED pins
int led = D7;
int photoresistor = A0;

int analogvalue;     

void setup() {
    pinMode(led,OUTPUT);
    pinMode(A5,OUTPUT);
    pinMode(photoresistor, INPUT);
    
    digitalWrite(A5,HIGH);
}


void loop() {
    
    analogvalue = analogRead(photoresistor);
    delay(100);
    // Get some data
    
    if (analogvalue < 60){

        // Trigger the integration
        Particle.publish("light","Sunlight is low!", PRIVATE);
        digitalWrite(led,HIGH);
        delay(40000);
        //delay(900000);
    }
    else {

        // Trigger the integration
        Particle.publish("light", "Sunlight hits your terrarium!", PRIVATE);
        digitalWrite(led,LOW);
        delay(40000);
        //delay(900000);
        
    }
    
}
    
