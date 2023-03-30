// ------------
// Blink an LED
// ------------
//Negin Pakroohjahromi (student ID: 222393187)
/*-------------

It blinks the D7 LED on the Particle device. Also, an LED wired to D0 to blink.

-------------*/


int led1 = D0; // led1


int led2 = D7; // led2 (The little blue LED on your board) 


int buttonPin = D3; //push botton --> reset the LED


void dash(){
    // To blink the LED, first we'll turn it on...
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    delay(3000);

    // Then we'll turn it off...
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    delay(1000);}
    
void dot(){
    // To blink the LED, first we'll turn it on...
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    delay(1000);

    // Then we'll turn it off...
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    delay(1000);}



void a(){
    dot();
    dash();
    delay(2000);}

void b(){
    dash();
    dot();
    dot();
    dot();
    delay(2000);}

void n(){
    dash();
    dot();
    delay(2000);}

void e(){
    dot();
    delay(2000);}

void g(){
    dash();
    dash();
    dot();
    delay(2000);}

void i(){
    dot();
    dot();
    delay(2000);}
    
// And continue creating procedures for other letters!


void setup() {

  // We are going to tell the device that D0 and D7 (which we named led1 and led2 respectively) are going to be output
  //(That means that we will be sending voltage to them, rather than monitoring voltage that comes from them)
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  // sets pin as input
  pinMode( buttonPin , INPUT_PULLUP); 
}


void loop() {
   // find out if the button is pushed or not by reading from it.
   int buttonState = digitalRead( buttonPin );

   if( buttonState == HIGH ){
    // turn the LEDs On based on the name we input;
       n();
       e();
       g();
       i();
       n();
   }
   else{
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
   }
}

