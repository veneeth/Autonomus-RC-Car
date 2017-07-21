import os
from driver import *
from Hiroshima import *
import time
import  threading
from multiprocessing import Process


class Master(object):
    p=Hiroshima()
    def __init__(self):
        self.h=Hiroshima()
        self.q=Hiroshima()
        self.d=Drive()

    def RunCam(self):
            self.p.Classify()
            
    def RunULtra(self):
            self.p.ulsense()
            
    def RunCar(self):
        self.p.DriverHandle()
        
            

if __name__=='__main__':
    m=Master()
    n=Master()
    o=Master()
    cam = threading.Thread(name ='Camera',target =m.RunCam )
    sen = threading.Thread(name = 'SEnsor', target =n.RunULtra)
    han=threading.Thread(name='Drive',target=o.RunCar)
    cam.start()
    sen.start()
    han.start()
    
  






    
     
            
   
        
       
            
    
        
        
            
    
        
    
