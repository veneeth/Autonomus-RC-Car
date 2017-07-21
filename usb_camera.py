import time
import cv2


traffic_cascade=cv2.CascadeClassifier('/home/pi/Downloads/Project/traffic_light.xml')
Stop_cascade=cv2.CascadeClassifier('/home/pi/Downloads/Project/stop_sign.xml')
cap=cv2.VideoCapture(0)
#time.sleep(3)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop = Stop_cascade.detectMultiScale(gray, 1.3, 5)
    signal = traffic_cascade.detectMultiScale(gray, 1.3, 5)
    red_light=len(signal)
    stop_sign=len(stop)
    print 'RedLight->'+str(red_light)
    print 'StopSign->'+str(stop_sign)
    tup=(stop,signal)
    for i in tup:
        for (x,y,w,h) in i:
             cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             roi_gray = gray[y:y+h, x:x+w]
             roi_color =img[y:y+h, x:x+w]

    #cv2.imshow("Frame",img)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
 
                   

