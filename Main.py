import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#ultrasonic sensor setup
TRIG = 4
ECHO = 18

#LED
LEDPIN = 21

MAX_DISTANCE_THRESHOLD = 10.0

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.output(LEDPIN, GPIO.LOW) #Turn off in the beginning

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    sig_time = end-start
    
    #in inches
    distance = sig_time/0.000148
    
    if(distance < MAX_DISTANCE_THRESHOLD):
        if GPIO.input(LEDPIN) == GPIO.LOW:
            #print('LED is on')
            GPIO.output(LEDPIN, GPIO.HIGH)
        else: 
            #print('LED is off')
            GPIO.output(LEDPIN, GPIO.LOW)
                    
    print('distance: {} inches' .format(distance))
    #return distance

#main program
while True:
    get_distance()
    time.sleep(0.5)

