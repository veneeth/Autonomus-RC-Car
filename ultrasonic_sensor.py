import RPi.GPIO as GPIO                    
import time
class Ultra():
    def __init__(self):
        self.m =0

        
    def ulsense(self):


        GPIO.setmode(GPIO.BCM)                     

        TRIG = 23                                  
        ECHO = 24                                  
        print "Distance measurement in progress"

        GPIO.setup(TRIG,GPIO.OUT)                  
        GPIO.setup(ECHO,GPIO.IN)                   

        while True:


          GPIO.output(TRIG, False)                 
          print "Waitng For Sensor To Settle"
          time.sleep(2)                            

          GPIO.output(TRIG, True)                  
          time.sleep(0.00001)                      
          GPIO.output(TRIG, False)                 

          while GPIO.input(ECHO)==0:               
            pulse_start = time.time()              

          while GPIO.input(ECHO)==1:               
            pulse_end = time.time()                

          pulse_duration = pulse_end - pulse_start 

          distance = pulse_duration * 17150        
          distance = round(distance, 2)            

          if distance > 2 and distance < 300:      
            print "Distance:",distance - 0.5,"cm"

a=Ultra()
a.ulsense()
          
            
