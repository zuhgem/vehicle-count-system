import cv2

cap=cv2.VideoCapture('C:/Users/HP/Desktop/Car-Detection-Basic-Open-CV-master/carv2.mp4')

car_cascade=cv2.CascadeClassifier('C:/Users/HP/Desktop/Car-Detection-Basic-Open-CV-master/carx.xml')

count=0

while(True):
    ret,frame=cap.read()
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    height,width,_=frame.shape
    
    cv2.putText(frame,'count=',(40,40), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
    
    cars=car_cascade.detectMultiScale(grey,1.1,1)
    
    for(x,y,w,h) in cars:
        
        car_cnt=int(y + h/2)
        cnt_line=height-20
        
        if(car_cnt<cnt_line+10 and car_cnt>cnt_line-10):
           
            count=count+1
            
            print(count)
        
        cv2.rectangle(frame,(x,y),(x+w-8,y+h-8),(0,0,0),2)
        cv2.putText(frame,str(count),(300,45), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

        
