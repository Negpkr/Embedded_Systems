import RPi.GPIO as GPIO
import time

# --> BCM GPIO
GPIO.setmode(GPIO.BCM)

# Pins
BUZZER_PIN = 25
TRIGGER_PIN = 23
ECHO_PIN = 24

GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# return distance in cm
def measureDistance():
    # trigger ultrasonic signal for 10 microseconds
    GPIO.output(TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, False)

    # save the current time in variables
    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start = time.time()

    while GPIO.input(ECHO_PIN) == 1: 
        stop = time.time()

    # (time the wave goes and back) * speed of sound (33112) --> 2 way distance
    distance = ((stop - start) * 33112)/2 #one way distance

    print("Distance : ", distance)

    return distance



def buzzer_beep(pause):
    GPIO.output(BUZZER_PIN, True)
    time.sleep(0.25) 
    GPIO.output(BUZZER_PIN, False)
    time.sleep(pause)  # Pause between beeps

def buzzer_act():
    # Measure the distance
    sensorDist = measureDistance()

    if sensorDist <= 10:
        #  --> Constant beeping
        GPIO.output(BUZZER_PIN, True)
        time.sleep(0.25)
        
    elif sensorDist > 10 and sensorDist <= 20:
		#  --> fast beeping
        buzzer_beep(0.25)
        
    elif sensorDist > 20 and sensorDist <= 30:
        buzzer_beep(0.5)
        
    elif sensorDist > 30 and sensorDist <= 40:
        buzzer_beep(0.75)
        
    elif sensorDist > 40 and sensorDist <= 50:
		#  --> slow beeping
        buzzer_beep(1)
        
    else: 
        # Distance > 50cm --> No beeping
        GPIO.output(BUZZER_PIN, False)
        time.sleep(0.25)


def main():
    try:
        # same as loop
        while True:
            buzzer_act()
    
    except KeyboardInterrupt:
		# Stop beeping
        GPIO.output(BUZZER_PIN, False)
        
        GPIO.cleanup()


if __name__ == "__main__":
    main()