import RPi.GPIO as GPIO
import time
 

def laser_shot():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT) 
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.1)               
    GPIO.cleanup()
    time.sleep(0.1)
    
laser_shot()
