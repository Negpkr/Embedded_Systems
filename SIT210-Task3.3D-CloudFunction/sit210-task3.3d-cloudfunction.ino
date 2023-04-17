
#include <HC_SR04.h>
#include <MQTT.h>


const char* Broker = "broker.emqx.io";
const int Port = 1883;
const char* ClientId = "mqttx_890383bf";
const char* Topic = "SIT210/wave";


int TRIG_PIN = D2;
int ECHO_PIN = D6;
int LED = D0;

void callback(char* topic, byte* payload, unsigned int length);
MQTT client(Broker, Port, callback);

// recieve message
void callback(char* topic, byte* payload, unsigned int length) 
{
    char p[length + 1];
    memcpy(p, payload, length);
    p[length] = NULL;

    if (!strcmp(p, "RED"))
    RGB.color(255, 0, 0);
    else if (!strcmp(p, "GREEN"))
    RGB.color(0, 255, 0);
    else if (!strcmp(p, "BLUE"))
    RGB.color(0, 0, 255);
    else
    RGB.color(255, 255, 255);
    delay(1000);
}


void setup()
{
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(LED, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    digitalWrite(TRIG_PIN, LOW);
    
    RGB.control(true);
    
    // connect to the server
    client.connect(ClientId + String(Time.now()));

    if (client.isConnected()) 
    {
        Particle.publish("Connected", PUBLIC);
        client.subscribe(Topic);
        client.publish(Topic,"Welcome!");
    }
}

void loop()
{
    float sensorDist = measureDistance();

    if (sensorDist < 6)
    {
        if (pat_wave())
        {
            // Publish message to MQTT topic
            client.publish(Topic, "Negin");
            Particle.publish("Wave detected, published message to SIT210/wave", PUBLIC);
            flash_pat();
        }
        else
        {
            flash_wave();
        }

    } 
    else 
    {
        digitalWrite(LED, LOW);
    }
    
    if (client.isConnected())
        client.loop();

    Particle.publish("rate", String(sensorDist), PUBLIC);
    delay(500); //read data every 0.5 second
    
}

bool pat_wave()
{
    for (int i = 0; i < 10; i++) //detect pat only if the distance remains close for 5 seconds
    {
        float sensorDist = measureDistance();
        delay(500);
        if (sensorDist > 6)
        {
            return false;
        }
    }
    return true;
}

void flash_wave()
{
    for (int i = 0; i < 3; i++) 
    {
        digitalWrite(LED, HIGH);
        delay(50);
        digitalWrite(LED, LOW);
        delay(50);
    }
}

void flash_pat()
{
    for (int i = 0; i < 2; i++) 
    {
        digitalWrite(LED, HIGH);
        delay(500);
        digitalWrite(LED, LOW);
        delay(50);
    }
}

// HC-SR04 ultrasonic sensor rate
float measureDistance() 
{

    unsigned long start_time, end_time, pulse_time;

    // trigger ultrasonic signal for 10 microseconds
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // wait until echo received 
    while (digitalRead(ECHO_PIN) == 0);

    // measure how long echo lasts (pulse time)
    start_time = micros(); // get start time (in microseconds)
    while (digitalRead(ECHO_PIN) == 1); // wait until echo ends
    end_time = micros(); // get end time
    pulse_time = end_time - start_time; // subtract to get duration

    //maximum distance = 23200
    if (pulse_time > 23200) pulse_time = 23200;

    // calculate distance
    float dist_in = pulse_time / 148.0; // in inches
    float dist_cm = pulse_time / 58.0; // in centimeters

    delay(60); //delay between ultrasonic readings
    
    return dist_in; // or can return dist_cm
}