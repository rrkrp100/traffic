#!Python3

def start():
    import cv2
    import numpy as np

    counter=0
    cap = cv2.VideoCapture('GenYoutube.net_Cars_moving_on_road_Stock_Footage_-_Free_Download.mp4.mp4')
    car=cv2.CascadeClassifier('cars.xml')
    while True:
        ret, frame = cap.read()
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.line(frame,(0,60),(160,60),(0,255,0),1)
        cars=car.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            #To find the Centroid
            x1 = w/2
            y1 = h/2
            cx = x + x1
            cy = y + y1
            centroid = (cx,cy)
            cv2.circle(frame,(int(cx),int(cy)),2,(0,0,255),-1)
            if centroid >(127,38) and centroid <(134,108):
                counter+=1
            cv2.putText(frame,str(counter),(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),5)
        cv2.imshow('OUTPUT',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
               break

    cap.release()
    cv2.destroyAllWindows()
    return (counter)
