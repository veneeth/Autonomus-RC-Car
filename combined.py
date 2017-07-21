# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO
import socket
from driver import *


class Hiroshima:
        global mes
        global mes2
        mes='GO FROM CAM'
        mes2='GO FROM USS'
        def __init__(self):
                
                self.red_light=0
                self.stop_sign=0
                self.distance=600
                self.a=0#GO
                self.b=0#GO
                 
        def Classify(self):
                
                traffic_cascade=cv2.CascadeClassifier('/home/pi/Desktop/Project1/traffic_light.xml')
                Stop_cascade=cv2.CascadeClassifier('/home/pi/Desktop/Project1/stop_sign.xml')

                # initialize the camera and grab a reference to the raw camera capture
                camera=PiCamera()
                camera.resolution=(640, 480)
                camera.framerate=32
                rawCapture = PiRGBArray(camera, size=(640, 480))
                 
                # allow the camera to warmup
                time.sleep(0.1)
                 
                # capture frames from the camera
                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                        # grab the raw NumPy array representing the image, then initialize the timestamp
                        # and occupied/unoccupied text
                        image = frame.array
                        #Custom
                        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                        light=traffic_cascade.detectMultiScale(gray,1.1,9)
                        sign=Stop_cascade.detectMultiScale(gray,1.1,15)
                        self.red_light=len(light)
                        self.stop_sign=len(sign)
                        print 'RedLight->'+str(self.red_light)
                        print 'StopSign->'+str(self.stop_sign)
                        if (((self.red_light >0 or self.stop_sign >0) and mes2=='GO FROM USS') or ((self.red_light >0 or self.stop_sign >0) and mes2=='STOP2\t\t\t\t\t\t')): 
                                mes='STOP1\t\t\t\t\t\t\t\t'
                                self.a=1
                        else:
                                mes='GO FROM CAM'
                                self.a=0
                        tup=(light,sign)
                        for i in tup:
                                for (x,y,w,h) in i:
                                                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                                                roi_gray = gray[y:y+h, x:x+w]
                                                roi_color =image[y:y+h, x:x+w]
                               
                        
                        # show the frame
                        cv2.imshow("Frame", image)
                        key = cv2.waitKey(1) & 0xFF
                 
                        # clear the stream in preparation for the next frame
                        rawCapture.truncate(0)
                 
                        # if the `q` key was pressed, break from the loop
                        if key == ord("q"):
                                break
        def weclassify(self):
                                                                               
                traffic_cascade=cv2.CascadeClassifier('/home/pi/Downloads/Project/traffic_light.xml')
                Stop_cascade=cv2.CascadeClassifier('/home/pi/Downloads/Project/stop_sign.xml')
                cap=cv2.VideoCapture(0)
                #time.sleep(3)
                while 1:
                        ret, img = cap.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        stop = Stop_cascade.detectMultiScale(gray, 1.1, 9)
                        signal = traffic_cascade.detectMultiScale(gray, 1.3, 5)
                        red_light=len(signal)
                        stop_sign=len(stop)
                        print 'RedLight->'+str(red_light)
                        print 'StopSign->'+str(stop_sign)
                        if red_light >0 or stop_sign >0:
                                mes='STOP1\t\t\t\t\t\t\t\t'
                        else:
                                mes='GO FROM CAM'
                        tup=(stop,signal)
                        for i in tup:
                                for (x,y,w,h) in i:
                                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                                        roi_gray = gray[y:y+h, x:x+w]
                                        roi_color =img[y:y+h, x:x+w]
                        cv2.imshow("Frame",img)
                        key = cv2.waitKey(1) & 0xFF
                        # if the `q` key was pressed, break from the loop
                        if key == ord("q"):
                                 break
                            
             
        
    



        def ulsense(self):
                #d=Drive()
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

                  self.distance = pulse_duration * 17150        
                  self.distance = round(self.distance, 2)            

                  if (((self.distance > 2 and self.distance < 30)and mes=='GO FROM CAM')and((self.distance > 2 and self.distance < 150)or mes=='STOP1\t\t\t\t\t\t\t\t')):      
                    print "Distance:",self.distance - 0.5,"cm"
                    mes2='STOP2\t\t\t\t\t\t'
                    self.b=1
                    
                    
                  else:
                        mes2='GO FROM USS'
                        self.b=0

        def DriverHandle(self):
                d=Drive()
                while True:
                        if((self.a==1 and self.b==0) or (self.a==0 and self.b==1) or (self.a==1 and self.b==1)):
                                d.stop_RC()
                                if(self.a==1 and self.b==0):
                                        mes1='STOP FROM CAM'+'\nRedLight->'+str(self.red_light)+'\nStopSign->'+str(self.stop_sign)

                                elif(self.a==1 and self.b==1):
                                        mes1='STOP FROM BOTH'+"\nDistance:"+str(self.distance - 0.5)+"cm"+'\nRedLight->'+str(self.red_light)+'\nStopSign->'+str(self.stop_sign)
                                        
                                else:
                                        mes1='STOP FROM SENSOR'+"\nDistance:"+str(self.distance - 0.5)+"cm"
                                print mes1

                        else:
                                d.start_RC()
                                mes1='GO'
                                print mes1
                



        
                          
                  

                        

                


        



                        
