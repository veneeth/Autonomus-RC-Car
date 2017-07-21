import RPi.GPIO as GPIO
import time

class Drive :
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        FRONT=21
        BACK=26
        GPIO.setup(FRONT,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(BACK,GPIO.OUT)
        
        
    def stop_RC(self):
        GPIO.output(21,True)
        GPIO.output(26,True)

    def start_RC(self):
        GPIO.output(21,True)
        GPIO.output(26,False)

#d=Drive()
#d.start_RC()
#d.stop_RC()

                    
                    
   




    
    
    
    
    
    
    
    


    
