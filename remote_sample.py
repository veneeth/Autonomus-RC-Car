import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(26, GPIO.OUT) 
GPIO.setup(21, GPIO.OUT) 
GPIO.output(21,True)
GPIO.output(26,True)
#reverse


