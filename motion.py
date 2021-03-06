# Pyhton program to implement
# WebCam Motion Detector
import time
import cv2, capture_car, time, os

def count_nxt(turn):
    pass



def motion(sigt=25,strt = time.time(),turn=1,flag=0):

    # importing OpenCV, time and Pandas library
    
    #from threading import Thread

    #print("Time alloted:",str(sigt))

    # Assigning our static_back to None
    static_back = None

    # Capturing video
    video = cv2.VideoCapture(0)
    count=0
    frame_count=0
    # Infinite while loop to treat stack of image as video

    while (time.time() -strt ) <= sigt:
        # Reading frame(image) from video
        check, frame = video.read()
        # Initializing motionFound = 0(no motion)
        motionFound = 0
        print("Time elapsed:",str(round((time.time()-strt),1)),end="\r")

        ### Calling the yolo object detector to count the number of vehicles on the next lane to go green.
        if round((sigt-(time.time()-strt)),1) <25 and flag==0:
            flag=1
            #Thread(target=count_nxt,args=(turn))
            count_nxt(turn)


        if check:

            # Converting color image to gray_scale image

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # In first iteration we assign the value
            # of static_back to our first frame
            #if static_back is None:
            if count == 0:
                static_back = gray
                count= (count+1)%20
                continue

            count= (count+1)%20

            if frame_count<10:
                frame_count+=1
                continue
            # Difference between static background
            # and current frame(which is GaussianBlur)
            diff_frame = cv2.absdiff(static_back, gray)

            # If change in between static background and
            # current frame is greater than 30 it will show white color(255)
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

            # Finding contour of moving object
            (cnts, _) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in cnts:
                if cv2.contourArea(contour) < 10000:
                    continue
                motionFound = 1

                print("\n Movement Detected.", end= " ")

                #Release resources
                video.release()

                # Destroying all the windows
                cv2.destroyAllWindows()

                #capture_car.take_pic(sigt,strt,turn,flag)
                motion(sigt,strt,turn,flag)
                break

            # Displaying the black and white image in which if
            # intencity difference greater than 30 it will appear white
            cv2.imshow("Threshold Frame", thresh_frame)

            # Displaying color frame with contour of motion of object
            cv2.imshow("Color Frame", frame)

            key = cv2.waitKey(1)
            # if q entered whole process will stop
            if key == ord('q'):
                # if something is movingthen it append the end time of movement
                if motionFound == 1:
                    time.append(datetime.now())
                break

    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import time
    motion(sigt=15,strt = time.time(),turn=1)
