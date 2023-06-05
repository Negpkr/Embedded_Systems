
#include <PietteTech_DHT.h>
#include <MQTT.h>

  /*
  # Editor     : NEGIN PAKROOH
  
  # the sensor value description
  # 0  ~400     dry soil
  # 400~1500     humid soil
  # 1500~2500     in water
  */


const char* Broker = "broker.emqx.io";
const int Port = 1883;
const char* ClientId = "mqttx_2ca754c2";
const char* Topic = "SIT210/Project";

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

int LED1 = D5;
int LED2 = D6;
int soil_moisture_1 = A1;
int soil_moisture_2 = A2;
#define DHTTYPE  DHT11   
#define DHTPIN   D3 

PietteTech_DHT DHT(DHTPIN, DHTTYPE);

int msg_time = 12000;

void setup() 
{
    client.connect(ClientId + String(Time.now()));

    if (client.isConnected()) 
    {
        Particle.publish("Connected", PUBLIC);
    }
    
    pinMode(soil_moisture_1, INPUT);
    pinMode(soil_moisture_2, INPUT);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    
}

void loop() 
{
    
    //SENSOR PART
    int SMdata1 = analogRead(soil_moisture_1); //connect sensor1 to Analog 1
    int SMdata2 = analogRead(soil_moisture_2); //connect sensor2 to Analog 2
    
    //int result = DHT.acquireAndWait(3000); // wait up to 3 sec
    int temp = DHT.getCelsius();

    delay(3000);               // Wait
    
    Particle.publish("Soil Moisture 1: ", String (SMdata1), PRIVATE);
    Particle.publish("Soil Moisture 2: ", String (SMdata2), PRIVATE);
    Particle.publish("Tempreture (C): ", String (temp), PRIVATE);
    
    // Only try to send messages if mqtt is connected
    if (client.isConnected())
    {
        client.publish(Topic, String(SMdata1) + "," + String(SMdata2) + "," + String(temp));
        
        client.loop();
    }
    
    watering_time_on(temp, SMdata1, LED1);
    watering_time_on(temp, SMdata2, LED2);
    
    watering_time_off(temp, SMdata1, LED1);
    watering_time_off(temp, SMdata2, LED2);
    Particle.publish(String(millis()), PRIVATE);

    
    if (millis() >= msg_time && millis() <= msg_time + 3000) 
    {
    
        if (watering_time_on(temp, SMdata1, LED1))
        {
            Particle.publish("plant", "Plant 1 needs water! ", PRIVATE);
        }
    
        if (watering_time_on(temp, SMdata2, LED2))
        {
            Particle.publish("plant", "Plant 2 needs water! ", PRIVATE);
        }
        msg_time = msg_time + 1800000;  // add 30 min = 1800000 ms
    }
}

bool watering_time_on(int temp, int SMdata, int LED)
{
    if (temp > 30 )
    {
        if (SMdata < 700)
        {
            digitalWrite(LED,HIGH);
            return true;
        }
    }
    else if (temp < 20)
    {
        if (SMdata < 400)
        {
            digitalWrite(LED,HIGH);
            return true;
        }
    }
    else
    {
        if (SMdata < 550)
        {
            digitalWrite(LED,HIGH);
            return true;
        }
    }
    return false;
}

void watering_time_off(int temp, int SMdata, int LED)
{
    if (temp < 20 )
    {
        if (SMdata >= 400)
        {
            digitalWrite(LED,LOW);
        }
    }
    else if (temp > 30)
    {
        if (SMdata >= 200)
        {
            digitalWrite(LED,LOW);
        }
        
    }
    else
    {
        if (SMdata >= 300)
        {
            digitalWrite(LED,LOW);
        }
    }
}
